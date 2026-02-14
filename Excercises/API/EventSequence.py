from datetime import datetime


class EventSequence:
    def __init__(self, events):
        self.events = events

    def validate_user_journey_events(self):
        invalid_users = []
        user_groups = {}

        for event in self.events:
            user_id = event["user_id"]
            if user_id not in user_groups:
                user_groups[user_id] = []
            user_groups[user_id].append(event)

        print(f"User groups with events: {user_groups}")

        for user_id, user_events in user_groups.items():
            sorted_events = sorted(
                user_events,
                key=lambda x: datetime.fromisoformat(x["timestamp"].replace('Z', '+00.00'))
            )

            first_action = sorted_events[0]["action"].upper()

            if first_action != "LOGIN":
                invalid_users.append(user_id)

        return invalid_users

if __name__ == "__main__":
    events = [
        {"user_id": "A", "timestamp": "2026-02-14T10:00:00Z", "action": "LOGIN"},
        {"user_id": "B", "timestamp": "2026-02-14T10:05:00Z", "action": "PLAY_SONG"},
        {"user_id": "A", "timestamp": "2026-02-14T10:10:00Z", "action": "PLAY_SONG"},
        {"user_id": "B", "timestamp": "2026-02-14T10:01:00Z", "action": "LOGIN"},  # B logged in AFTER playing
    ]

    eventsSequence = EventSequence(events)
    print(eventsSequence.validate_user_journey_events())




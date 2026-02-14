class ErrorLogs:
    def __init__(self, logs):
        self.logs = logs

    def get_high_failure_rates(self, threshold):
        user_stats = {}

        for log in self.logs:
            log_data = log.split("|")
            if len(log_data) < 3:
                continue

            user_id = log_data[0]
            action_status = log_data[-1].upper()

            if user_id not in user_stats:
                user_stats[user_id] = [0, 0]

            user_stats[user_id][1] += 1
            if action_status == "FAIL":
                user_stats[user_id][0] += 1

        print(f"User Stats: {user_stats}")

        high_failure_users = []
        for user_id, counts in user_stats.items():
            fails = counts[0]
            total = counts[1]

            error_rate = fails / total if total > 0 else 0

            if error_rate > threshold:
                high_failure_users.append(user_id)

        return high_failure_users


if __name__ == "__main__":
    logs = [
        "user_1|play|SUCCESS",
        "user_2|play|SUCCESS",
        "user_1|play|FAIL",
        "user_3|play|SUCCESS",
        "user_2|play|FAIL",
        "user_1|play|FAIL",
        "user_4|play|SUCCESS",
        "user_2|play|SUCCESS",
        "user_1|play|SUCCESS",
        "user_3|play|FAIL"
    ]

    monitor = ErrorLogs(logs)
    print(monitor.get_high_failure_rates(0.20))












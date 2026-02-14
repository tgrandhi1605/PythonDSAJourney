class MostPlayedSongs:
    def __init__(self, events):
        self.events = events

    def get_top_k_songs(self, k):
        song_group = {}

        for event in self.events:
            if event["song"] not in song_group:
                song_group[event["song"]] = 0
            song_group[event["song"]] += 1

        print(f"Song and their frequencies: {song_group}")

        sorted_songs = sorted(song_group.items(),
                              key = lambda x: x[1], reverse = True)

        return [item[0] for item in sorted_songs[0:k]]

if __name__== "__main__":

    events = [
        {"song": "Blinding Lights"},
        {"song": "Cruel Summer"},
        {"song": "Blinding Lights"},
        {"song": "Cruel Summer"},
        {"song": "Cruel Summer"},
        {"song": "Flowers"},
        {"song": "Flowers"},
        {"song": "Flowers"},
        {"song": "Flowers"},
        {"song": "Anti-Hero"}
    ]

    top_songs = MostPlayedSongs(events)
    print(top_songs.get_top_k_songs(3))

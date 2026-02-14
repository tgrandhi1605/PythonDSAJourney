class StringSequence:
    def __init__(self, string):
        self.string = string

    def get_sequence(self):
        if not self.string:
            return []

        sequence = []
        count = 1

        for i in range(len(self.string) - 1):
            if self.string[i] == self.string[i + 1]:
                count += 1
            else:
                sequence.append(self.string[i] + str(count))
                count = 1

        sequence.append(self.string[-1]  + str(count))

        return sequence

if __name__ == "__main__":
    stringy = None
    string_sequence = StringSequence(stringy)
    print(string_sequence.get_sequence())




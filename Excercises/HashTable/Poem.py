import string


class Poem:
    def __init__(self):
        self.poem_data = {}

    def get_poem_data(self, file_path):
        table = str.maketrans('', '', string.punctuation)
        with open(file_path, 'r') as file:
            for line in file:
                clean_line = line.translate(table).lower().split()
                for word in clean_line:
                    if word in self.poem_data:
                        self.poem_data[word] +=1
                    else:
                        self.poem_data[word] = 1
            return self.poem_data


if __name__ == "__main__":
    poem = Poem()
    data = poem.get_poem_data('poem.txt')
    print(data)

    sorted_words = sorted(data.items(), key=lambda item: item[1], reverse=True)
    print("Most used word: ", sorted_words[0])
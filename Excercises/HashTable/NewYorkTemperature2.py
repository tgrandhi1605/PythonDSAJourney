class NewYorkTemperature2:
    def __init__(self):
        self.temperature_data = {}

    def get_data(self, file_path):
        with open(file_path, 'r') as file:
            next(file)
            for line in file:
                day, temperature = line.strip().split(',')
                self.temperature_data[day] = temperature
            return   self.temperature_data


if __name__ == "__main__":
    weather = NewYorkTemperature2()
    data = weather.get_data('nyc_weather.csv')
    print("Full data", data)

    # What was the temperature on Jan 9?
    for day, temperature in data.items():
        if day == 'Jan 9':
            print(f"Temperature on Jan 9: {temperature}")

            # What was the temperature on Jan 4?
    for day, temperature in data.items():
        if day == 'Jan 4':
            print(f"Temperature on Jan 4: {temperature}")
class NewYorkWeather:
    def __init__(self):
        self.temperature_data = []

    def get_data(self, file_path):
        with open(file_path, 'r') as file:
            next(file)
            for line in file:
                self.temperature_data.append(int(line.strip().split(',')[1]))
            return  self.temperature_data



if __name__ == "__main__":
    weather = NewYorkWeather()
    data = weather.get_data('nyc_weather.csv')
    print(data)

    # What was the average temperature in first week of Jan
    one_week_temperature = data[0:7]
    average_temperature = sum(one_week_temperature)/len(one_week_temperature)
    print(f"Average temperature in first week of Jan: {average_temperature}")

    # What was the maximum temperature in first 10 days of Jan
    max_temperature = max(data[0:10])
    print(f"Maximum temperature in first 10 days of Jan: {max_temperature}")
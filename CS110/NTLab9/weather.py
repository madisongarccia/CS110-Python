# App to Get Temperature Data from "Open Weather Map" Service
import pyowm

#Define global variable to store OWM weather-query object
owm = pyowm.OWM('0156b4aea5bd76accbe65ea205c43871')
wman = owm.weather_manager()

#Function that gets weather info from API - DO NOT EDIT
#  Returns results in dictionary with
#  keys 'temp', 'temp_max', 'temp_min'
#  and values that are floats
#  DO NOT EDIT THIS FUNCTION
def getWeather(city, country):
    location = city+','+country
    observation = wman.weather_at_place(location).weather
    return observation.temperature('fahrenheit')

def f_to_c(temp):
    c_temp=(temp-32)*(5/9)
    return c_temp

def main():
    while True:
        print('Enter a location where you would like to see the temperature.')
        city=input('Enter a city: ')
        country=input('Enter country: ')
        weather=getWeather(city,country)
        max_c=f_to_c(weather['temp_max'])
        temp_c=f_to_c(weather['temp'])
        min_c=f_to_c(weather['temp_min'])
        print(f"Max temperature: {weather['temp_max']:.2f}F {max_c:.2f}C")
        print(f"Current temperature: {weather['temp']:.2f}F {temp_c:.2f}C")
        print(f"Minimum temperature: {weather['temp_min']:.2f}F {min_c:.2f}C")
        while True:
            valid_inputs=['Y', 'N']
            user_input=input('Would you like to check another city? (Y/N)')
            if user_input not in valid_inputs:
                print('Please enter a valid input')
                continue
            elif user_input=='Y':
                break
            else:
                exit()
    # Add code that prints program's purpose, then:
    #   1. Prompts user for city and country
    #   2. Calls getWeather with city and country and saves returned dictionary
    #   3. Uses keys "temp_max", "temp", and "temp_min" to extract temperatures
    #   4. Prints the temperatures
    #   5. Asks if user wants to check another city (Y or N)
    #   6. Validates user response
    #   7. If Y, loop back to step 1
#Start the app
main()

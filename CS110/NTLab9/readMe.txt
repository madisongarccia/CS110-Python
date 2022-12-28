MADISON WOZNIAK

SOURCES:
openweathermap.org/appid for API key
NTLab 9 instruction page

By referencing OpenWeatherMap.org, thsi program tells the user the max, min, and current temperature in the city they have chosen, in terms of both Celsius and Fahrenheit. 

HOW IT WORKS:
First the program needed to import the pyowm module to access its data, and to do so I needed to register for an API key that I used to get the data. The main function Asks the user which city they would like to get information on. Next, to specify which country the city is in, it asks which country the city is in. With this information, the main() function calls the getweather() function. In the getweather() function, it takes parameters city and country, and adds them to a variable location, which is used to find the correct values from the API. These are returned as keys 'temp', 'temp_max', 'temp_min' with corresponding float values representing degrees fahrenheit. To add celcius measurements, the main() function assigns celsius values to each fahrenheit value using the function f_to_c() that takes 'temp' as a parameter and returns 'c_temp' - a formula to convert fahrenheit to celsius. Next, the main() function prints the max, current, and min temperatures. Next, a while loop that asks if the user would like to see the temperature of another place by responding Y or N. Based on the response, the main() function either goes back to the first while loop or exits the program. 
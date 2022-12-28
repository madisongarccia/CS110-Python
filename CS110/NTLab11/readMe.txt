MADISON WOZNIAK

SOURCES
instructions page

The purpose of this app is to return to the user information about the current stock market values for a given symbol representing a company. It will include the current price, high, low, and the previous day's price.

The program has both a main function and a getStock() function. The getStock() function uses my API key and the website's URL to access the data needed regarding stock market prices. The main() function starts by printing to the screen 'check stock prices' and asks the user for a stock symbol. with this, we call the getStock() function passing the symbol as a parameter which returns the stock price values for that symbol. Next I separated the csv string into a list of two strings, the first being the names of each category, and the second holds the values. Next the program is supposed to return to the user the previous closing value, open value, high value, low value, and current value to the user as long as the symbol was valid and the list has only two items. This information is outputted to a separate text file called stock_prices.txt. Finally the app asks the user if they would like to check another stock price by entering either Y or N in which case the program will repeate or end. 

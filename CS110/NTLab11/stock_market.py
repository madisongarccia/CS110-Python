# Web App to Get Stock Market Data from AlphaVantage Service
import requests

#Function that gets stock info from API
#  Returns results in list of two strings
#  DO NOT EDIT THIS FUNCTION EXCEPT TO INSERT YOUR API KEY WHERE INDICATED
def getStock(symbol):
    baseURL = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&datatype=csv"
    keyPart = "&apikey=" + "BH519MSCWNXQJK00" #Add API key
    symbolPart = "&symbol=" + symbol
    stockResponse = requests.get(baseURL+keyPart+symbolPart)
    return stockResponse.text  #Return only text part of response

#Function that computes and displays results
def main():
    file=open("stock_prices.txt",'a')
    print("Check stock prices.")
    running=True
    while running==True:
        symbolInput=input("Please provide a stock symbol: ")
        stock_price_data=getStock(symbolInput)
        stock_price_data=stock_price_data.split()
        while len(stock_price_data)!=2:
            symbolInput=input('Symbol not found. Enter a new symbol: ')
            stock_price_data=getStock(symbolInput)
            stock_price_data=stock_price_data.split()

        category=stock_price_data[0].split(',')
        values=stock_price_data[1].split(',')
        d={}
        for name in category:
            for num in values:
                d[name]=num
                values.remove(num)
                break

        print('Stock symbol: ', d['symbol'])
        print('Last Close: ',d['previousClose'])
        print("Open:",d['open'])
        print('High: ',d["high"])
        print('Low: ',d['low'])
        print('Current: ',d['price'])

    
        file.write('Stock symbol: '+d['symbol']+'\n')
        file.write('Last Close: '+d['previousClose']+'\n')
        file.write('Open: '+d['open']+'\n')
        file.write('High: '+d['open']+'\n')
        file.write('Low: '+d['low']+'\n')
        file.write('Current: '+d['price']+'\n')
        file.write('============================\n')

        inputs=['y','Y','N','n']
        userIn=input('Check another stock price?(Y or N):' )
        if userIn not in inputs:
            print('Invalid input (Y or N')
        elif userIn =='y' or userIn=='Y':
            running=True
        else:
            running=False

    file.close()
main()
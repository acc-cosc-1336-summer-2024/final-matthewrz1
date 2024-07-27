#write functions here, don't add input('') statements here!

class Stock:

    def __init__(self,symbol,company_name):
        
        self.__symbol = symbol
        self.__company_name = company_name

    def return_symbol(self):
        return self.__symbol
    
    def return_company_name(self):
        return self.__company_name
    

def stock_purchase_history():

    apple = Stock('AAPL','Apple Inc')
    caterpillar = Stock('CAT','Caterpillar')
    eastman_kodak = Stock('EK','Eastman Kodak')
    google = Stock('GOOG','Google')
    microsoft = Stock('MSFT','Microsoft')

    stock_dict = {}

    stock_dict[apple.return_symbol()] = apple.return_company_name()
    stock_dict[caterpillar.return_symbol()] = caterpillar.return_company_name()
    stock_dict[eastman_kodak.return_symbol()] = eastman_kodak.return_company_name()
    stock_dict[google.return_symbol()] = google.return_company_name()
    stock_dict[microsoft.return_symbol()] = microsoft.return_company_name()


    print("Stock List", "\n")
    print("Symbol  Company Name", "\n")

    for key,value in stock_dict.items():
        print(f"{key}...{value}")


#print(stock_purchase_history())
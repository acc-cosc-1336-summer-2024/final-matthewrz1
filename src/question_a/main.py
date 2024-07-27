#add import

from question_a import Stock

def main():

    company_list = []

    apple = Stock('APPL','Apple Inc')
    caterpillar = Stock('CAT','Caterpillar')
    eastman_kodak = Stock('EK','Eastman Kodak')
    google = Stock('GOOG','Google')
    microsoft = Stock('MSFT','Microsoft')

    company_list.append(apple)
    company_list.append(caterpillar)
    company_list.append(eastman_kodak)
    company_list.append(google)
    company_list.append(microsoft)

    print('Stock', 'Report: \n', sep = ' ')
    print('Company', 'Symbol: \n', sep = '...')
    for stock in company_list:
        print(stock.get_company_name(), stock.get_symbol(), sep='...')

if __name__ == '__main__':
    main()
        





#Pandas practice
import pandas as pd

path=["C:/Users/Linda/Desktop/State_MedianListingPricePerSqft_AllHomes.csv",
      "C:/Users/Linda/Desktop/MarketHealthIndex_County.csv",
      "C:/Users/Linda/Desktop/County_PriceToRentRatio_AllHomes.csv",
      "C:/Users/Linda/Desktop/BuyerSellerIndex_Zip.csv"]

df=[pd.read_csv(path[0]),
    pd.read_csv(path[1]),
    pd.read_csv(path[2]),
    pd.read_csv(path[3])]

def statePricePerSqft(df):
    #Create datafram of state and current month
    x=df.loc[:,['RegionName','2018-07']]

    #Rename to Place and Price
    x.columns=['Place', 'Price']

    #Filter only newEngland Counties
    newEngland=x[x['Place'].isin(['Connecticut',
                                  'Massachusetts',
                                  'Rhode Island',
                                  'New Hampshire',
                                  'Vermont', 'Maine'])]

    #Filter Places where the Price is > 100k
    greaterThan100=newEngland[newEngland.Price>100]

    #Sort by price
    greaterThan100=greaterThan100.sort_values(by=['Price'])


    #Filter Places where the Price is > 500k
    greaterThan500=newEngland[newEngland.Price>500]


    #Print the Results
    print('State_MedianListingPricePerSqft_NewEngland\n')
    print('Greater than $100/sqft')
    print(greaterThan100)
    print()
    print('Greater than $500/sqft') 
    print(greaterThan500)


 
def zillowHealthIndex(df):
    #Create datafram of state and current month
    x=df.loc[:,['RegionName', 'State', 'ZHVI']]

    #Rename to Place and Price
    x.columns=['Place', 'State', 'Score']

    #Filter only newEngland Counties
    newEngland=x[x['State'].isin(sl)]

    #Filter Places where the Score is > 200k
    greaterThan200=newEngland[newEngland.Score>200000]

    #Sort by state and then by score
    greaterThan200=greaterThan200.sort_values(by=['State','Score'])

    #Filter Places where the Score is > 1Million
    greaterThanMil=newEngland[newEngland.Score>1000000]
    
    #Print the Results
    print('MarketHealthIndex_NewEngland\n')
    print('Greater than $200k ZHVI')
    print(greaterThan200)
    print()
    print('Greater than $1Million ZHVI')
    print(greaterThanMil)



def rentToPriceRatio(df):
    #Create datafram of state and current month
    x=df.loc[:,['RegionName', 'State', '2018-07']]

    #Rename to Place and Price
    x.columns=['Place', 'State', 'Ratio']

    #Filter only newEngland Counties
    newEngland=x[x['State'].isin(sl)]

    #Filter only CT
    #CT=newEngland[newEngland['State'].isin(['MA'])]

    #Filter Places where the Ratio is > 5
    greaterThan5=newEngland[newEngland.Ratio>5]
    #Filter Places where the Ratio is also less than 10
    greaterThan5LessThan10=greaterThan5[greaterThan5.Ratio<10]

    #Filter Places where the Ratio is > 10
    greaterThan10=newEngland[newEngland.Ratio>10]

    #Sort the columns by state and then ratio
    greaterThan10=greaterThan10.sort_values(by=['State', 'Ratio'])
    
    #Print the Results
    print('rentToPriceRatio_NewEngland\n')
    print('Ratio Greater than 5 and Less than 10')
    print(greaterThan5LessThan10)
    print()
    print('Ratio Greater than 10')
    print(greaterThan10)

def buyerSellerIndex(df):
       
    #Create datafram of state and current month
    x=df.loc[:,['CBSA Title', 'State', 'BuyerSellerIndex']]

    #Rename to Place and Price
    x.columns=['Place', 'State', 'Index']

    #Filter only newEngland Counties
    newEngland=x[x['State'].isin(sl)]

    #Filter only CT
    #CT=newEngland[newEngland['State'].isin(['MA'])]

    #Filter Places where the Index is <5
    lessThan5=newEngland[newEngland.Index<5]

    #Sort the columns by state and then index
    lessThan5=lessThan5.sort_values(by=['State', 'Index'])

    #Filter Places where the Ratio is > 9
    greaterThan9=newEngland[newEngland.Index>9]

    #Sort the columns by state and then index
    greaterThan9=greaterThan9.sort_values(by=['State', 'Index'])
    
    #Print the Results
    print('buyerSellerIndex_NewEngland\n')
    print('Index less than 5')
    print(lessThan5)
    print()
    print('Index Greater than 9')
    print(greaterThan9)
    
def main():
    #Global list of bewEngland states
    global sl
    sl=['CT', 'MA', 'RI', 'NH', 'VT', 'MN']

    #Retrieve report for median square foot price per state   
    statePricePerSqft(df[0])
    print('\n------------------------------------\n')

    #Retrieve report for newEngland ZHVI by county   
    zillowHealthIndex(df[1])
    print('\n------------------------------------\n')

    #Retrieve report for newEngland rentToPriceRatio by county   
    rentToPriceRatio(df[2])
    print('\n------------------------------------\n')

    #Retrieve report for newEngland buyerSellerIndex by zip   
    buyerSellerIndex(df[3])
    print('\n------------------------------------\n')

if __name__=='__main__':
    main()

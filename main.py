"""
Main cli or app entry point
"""

import pandas as pd

def analyze() -> pd.core.frame.DataFrame:
    '''
    Function that analyze the csv file using pandas
    '''
    #read the csv file
    marketing_data = pd.read_csv("data/ifood_df.csv")

    #data manipulation
    marketing_data['TotalSpending'] = marketing_data['MntWines'] + marketing_data['MntFruits'] + marketing_data['MntMeatProducts'] + marketing_data['MntFishProducts'] + marketing_data['MntSweetProducts']
    marketing_data['AcceptedOffer'] = marketing_data['AcceptedCmp1'] + marketing_data['AcceptedCmp2'] + marketing_data['AcceptedCmp3'] + marketing_data['AcceptedCmp4'] + marketing_data['AcceptedCmp5']
    marketing_data = marketing_data[['Income', 'TotalSpending', 'AcceptedOffer', 'MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts','MntSweetProducts']]
    marketing_data.describe()

    #data visualization
    marketing_data.plot.scatter(x = 'Income', y = 'TotalSpending', c = 'AcceptedOffer', cmap='viridis')
    marketing_data.plot.scatter(x = 'Income', y = 'MntWines', c = 'AcceptedOffer', cmap='viridis')
    marketing_data.plot.scatter(x = 'Income', y = 'MntFruits', c = 'AcceptedOffer', cmap='viridis')
    marketing_data.plot.scatter(x = 'Income', y = 'MntMeatProducts', c = 'AcceptedOffer', cmap='viridis')
    marketing_data.plot.scatter(x = 'Income', y = 'MntFishProducts', c = 'AcceptedOffer', cmap='viridis') 
    marketing_data.plot.scatter(x = 'Income', y = 'MntSweetProducts', c = 'AcceptedOffer', cmap='viridis')  
    
    #return the dataframe
    return marketing_data
  
   


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    analyze()

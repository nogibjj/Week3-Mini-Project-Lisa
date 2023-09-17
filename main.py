import polars as pl
import seaborn as sns

def analyze() -> pl.DataFrame:
    '''
    Function that analyzes the csv file using polars
    '''
    # Read the csv file
    marketing_data = pl.read_csv("mydata/ifood_df.csv")

    # Data manipulation
    marketing_data = marketing_data.with_columns(
        TotalSpending = 
        pl.col("MntWines")
        + pl.col("MntFruits")
        + pl.col("MntMeatProducts")
        + pl.col("MntFishProducts")
        + pl.col("MntSweetProducts")
    )
    marketing_data = marketing_data.with_columns(
        AcceptedOffer = 
        pl.col("AcceptedCmp1")
        + pl.col("AcceptedCmp2")
        + pl.col("AcceptedCmp3")
        + pl.col("AcceptedCmp4")
        + pl.col("AcceptedCmp5")
    )
    marketing_data = marketing_data.select([
        "Income",
        "TotalSpending",
        "AcceptedOffer",
        "MntWines",
        "MntFruits",
        "MntMeatProducts",
        "MntFishProducts",
        "MntSweetProducts",
    ])
    marketing_data.describe()

    # Data visualization
    sns.scatterplot(data=marketing_data, x="Income", y="TotalSpending", hue="AcceptedOffer")
    sns.scatterplot(data=marketing_data, x="Income", y="MntWines", hue="AcceptedOffer")
    sns.scatterplot(data=marketing_data, x="Income", y="MntFruits", hue="AcceptedOffer")
    sns.scatterplot(data=marketing_data, x="Income", y="MntMeatProducts", hue="AcceptedOffer")
    sns.scatterplot(data=marketing_data, x="Income", y="MntFishProducts", hue="AcceptedOffer")
    sns.scatterplot(data=marketing_data, x="Income", y="MntSweetProducts", hue="AcceptedOffer")
    # Return the DataFrame
    return marketing_data


if __name__ == "__main__":
    analyze()
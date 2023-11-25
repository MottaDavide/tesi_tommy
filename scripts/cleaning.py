import pandas as pd


def group(df):
    df = df.groupby(by = list(df.columns.drop(['sku','year_month', 'order_quantity', 'size', 'model'])), as_index=False)['order_quantity'].sum()

    return df
    
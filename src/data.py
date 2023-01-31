import pandas as pd


def create_unique_list_of_currencies(df: pd.DataFrame):
    '''
    Function created to make a list of unique currency codes that are needed for dropdown in the dash app
    :param df:
    :return:
    '''
    list_of_currency_codes = df['currency_code'].unique().tolist()
    list_of_currency_codes = list(sorted(list_of_currency_codes))
    return list_of_currency_codes


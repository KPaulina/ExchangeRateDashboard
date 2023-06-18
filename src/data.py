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


def take_only_part_of_date(df: pd.DataFrame) -> pd.DataFrame:
    df['time_last_update_utc'] = df['time_last_update_utc'].str[:-15]
    return df


def pivoted_data(df: pd.DataFrame):
    # df[(df['B'] == 'Blue') & (df['C'] == 'Green')]
    df = df[(df['currency_code'] == 'USD') | (df['currency_code'] == 'EUR') | (df['currency_code'] == 'NOK')
        | (df['currency_code'] == 'SEK') | (df['currency_code'] == 'DKK')]
    heatmap_data = df.pivot(index='id', columns='currency_code', values='rates')
    return heatmap_data
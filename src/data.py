import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from consts import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT


def get_data_from_postgres_database() -> pd.DataFrame:
    '''
    Function created to get data from database
    :return: pd.Dataframe
    '''
    url = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    engine = create_engine(url)

    sql = """
        SELECT id, currency_code, provider, time_last_update_utc, rates, updated_at
        FROM public.exchange_rate_pln;
    """

    with engine.connect().execution_options(autocommit=True) as conn:
        query = conn.execute(text(sql))
    return pd.DataFrame(query.fetchall())


def create_unique_list_of_currencies(df: pd.DataFrame) -> list[str]:
    '''
    Function created to make a list of unique currency codes that are needed for dropdown in the dash app
    :param df:
    :return:
    '''
    list_of_currency_codes = df['currency_code'].unique().tolist()
    list_of_currency_codes = list(sorted(list_of_currency_codes))
    return list_of_currency_codes

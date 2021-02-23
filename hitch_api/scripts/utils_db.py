import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame


def df_to_sql(df: DataFrame, engine, column_name: str, new_name: str, drop: bool = False) -> None:
    """
    method to fill the database tables with a dataframe
    """
    if drop:
        df = df[[column_name]].drop_duplicates().rename(
            columns={column_name: new_name}).dropna()
    else:
        df = df[[column_name]].drop_duplicates().rename(
            columns={column_name: new_name})
    df.to_sql(f'nba_api_{column_name.lower()}',
              engine, if_exists='append', index=False)


def factorize_columns(df: DataFrame) -> None:
    """
    method to change the values of the foreign keys by its numeric id
    in the table player
    """
    df['Position'] = pd.factorize(df.Position)[0] + 1
    df['Team'] = pd.factorize(df.Team)[0] + 1
    df['College'] = pd.factorize(df.College)[0] + 1
    df['College'] = df['College'].replace(0, np.nan)


def set_columns_names(df: DataFrame) -> dict:
    """
    method to get a dictionary with the new names for the table player
    """
    new_names = {}
    for col in df.columns:
        if col in ['College', 'Position', 'Team']:
            new_names.setdefault(col, f'{col.lower()}_id')
        new_names.setdefault(col, col.lower())
    new_names.update({'Name': 'full_name'})
    return new_names


"""
Second Part: Create your code.

In this module you should implement a code that reads the file
nba.xlsx (taken from https://www.geeksforgeeks.org/python-pandas-dataframe/)
and import it as a pandas dataframe and process it.

There should be functions or methods that:

0) Read and import excel file into pandas dataframe (df)
1) Prints the df
2) Return a df with a single given column from the original df
3) Return a list or array (explain choise) from a given column
4) Return a sub-dataframe filtered by a column value
5) Return the merge of two dataframes (you can use the nba2.xlsx)
   with an inner join.
6) Output a given dataframe to an excel file.


Third Part: Challenge yourself
            Implement a simple API in Django with a storage
            in Postgresql that uses the methods for processing
            developed with pandas.
"""
import pandas as pd
from pandas.core.frame import DataFrame
from typing import Any


class DataProcessing:
   """
   class to perform data processing with pandas
   """
   def __init__(self, file_path: str = './data/nba.xlsx') -> None:
      """
      class constructor.
      @file_path: path of the excel file
      """
      self.df = pd.read_excel(file_path)

   def get_column(self, column_name: str) -> Any:
      """
      method to get a single column from a dataframe
      @column_name: column name of the dataframe
      """
      col_df = self.df.get(column_name)
      return col_df if col_df is not None else None

   def to_array(self, column_name: str='', dup: bool=True) -> Any:
      """
      Returning a numpy array because it's efficient processing large data
      and it has many methods to implement over the data.
      @column_name: column name of the dataframe
      @dup: if False, the return is made with no duplicate values
      """
      df_col = self.get_column(column_name)
      if df_col is None:
         return None
      return df_col.values if dup else df_col.drop_duplicates().values

   def sub_df(self, column_name: str, column_value: Any) -> Any:
      """
      Method that returns a sub-dataframe filtered by a column value
      """
      col = self.get_column(column_name)
      return self.df[col == column_value] if col is not None else None

   def merge_df(self, df2: DataFrame) -> DataFrame:
      return pd.merge(self.df, df2)

   @staticmethod
   def to_excel(df, name: str='df_to_excel'):
      if not isinstance(name, str):
         raise TypeError('Name must be a string')
      name = name.split('.')
      return df.to_excel(f'{name[0]}.xlsx')

if __name__ == '__main__':
    df1 = DataProcessing()
    print("*"*100)
    print(df1.df)
    df_col = df1.get_column('Age')
    print("*"*100)
    print(df_col, type(df_col))
    df_to_array = df1.to_array('Team')
    print("*"*100)
    print(df_to_array, type(df_to_array))
    sub_df = df1.sub_df('Number', 99)
    print("*"*100)
    print(sub_df)
    df2 = DataProcessing('./data/nba2.xlsx')
    print("*"*100)
    print(df2.df)
    print(type(df1.merge_df(df2.df)))
    df_merged = df1.merge_df(df2.df)
    DataProcessing.to_excel(df_merged, 'new_df')

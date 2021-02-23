from sqlalchemy import create_engine
from pandasPractice import DataProcessing
from utils_db import df_to_sql, factorize_columns, set_columns_names


engine = create_engine('postgresql://nba_user:nba_pass@localhost:5432/nba_db')
df = DataProcessing()

df_to_sql(df.df, engine, 'Team', 'name')
df_to_sql(df.df, engine, 'Position', 'position')
df_to_sql(df.df, engine,  'College', 'name', True)

factorize_columns(df.df)

players = df.df.rename(columns=set_columns_names(df.df))

# new_order = ['full_name', 'number', 'age', 'height', 'weight',
#              'salary', 'college_id', 'position_id', 'team_id']
# players = players[new_order]
players.to_sql('nba_api_player', engine, if_exists='append', index=False)

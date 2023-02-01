# import pandas library
import pandas as pd

# load sample csv file into dataframe and count rows loaded
df = pd.read_csv('E:/Projects/python-pandas/GHCND_sample_csv.csv')
print(f'There are {len(df)} lines in the dataset.')

# inspect dataset structure interpred by pandas
df.info()

# inspect dataset first 10 lines
print(df.head(5))

# projection relational operation
df_proj = df[['STATION_NAME', 'DATE', 'TMAX', 'TMIN']]

# inspect first 5 lines of the projected dataframe
df_proj.head(5)

# save
df_proj.to_csv('E:/Projects/python-pandas/GHCND_sample_projected.csv')
print(f'There are {len(df_proj)} lines in the dataset.')
print(f'There are {len(df_proj.columns)} columns in the dataset.')
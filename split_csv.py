import pandas as pd

filename= "df_final"
source_path = ".\\files2\\" + filename + ".csv"
for i,chunk in enumerate(pd.read_csv(source_path, chunksize=40000)):
    chunk.to_csv('.\\files\\'+ filename + '\\'+ filename + '_{}.csv'.format(i), index=False)
import pandas as pd
from pathlib import Path


filename= "df_edges_full"
source_path = "C:\\Users\\steph\\Desktop\\" + filename + ".csv"
dest_path = '.\\files2\\'+ filename + '\\'+ filename + '_{}.csv'

Path(".\\files2\\"+ filename).mkdir(parents=True, exist_ok=True)

for i,chunk in enumerate(pd.read_csv(source_path, chunksize=40000)):
    chunk.to_csv(dest_path.format(i), index=False)
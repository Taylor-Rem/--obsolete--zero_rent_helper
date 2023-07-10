import pandas as pd
from create_folder import file_path

df = pd.read_csv(file_path)

properties = df.filter(like="Property Name").values.flatten().tolist()
units = df.filter(like="Space Number").values.flatten().tolist()

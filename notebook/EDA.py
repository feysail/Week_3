import pandas as pd
def load_data(file_path):
    return pd.read_csv(file_path,sep='|',on_bad_lines='skip')
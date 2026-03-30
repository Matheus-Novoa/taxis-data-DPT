import pandas as pd
from pathlib import Path
from tqdm import tqdm


def load_data(*file_list) -> pd.DataFrame | None:
    '''
    Loads data from CSV files in the specified directory. If no file names are provided, it loads all CSV files in the directory.
    Parameters:
        *file_list: A variable number of file names to load.
    Returns:
        A pandas DataFrame containing the loaded data, or None if an error occurs.'''
    data_dir = Path("data")
    
    if not file_list:
        df_list = pd.DataFrame()
        for file_name in tqdm(data_dir.glob("*.csv")):
            try:
                data = pd.read_csv(file_name)
                df_list = pd.concat([df_list, data], ignore_index=True)
            except Exception as e:
                print(f"An error occurred while loading the data: {e}")
                return None
        return df_list
    else:
        df_list = pd.DataFrame()
        for file_name in tqdm(file_list):
            try:
                data = pd.read_csv(data_dir / file_name)
                df_list = pd.concat([df_list, data], ignore_index=True)
            except Exception as e:
                print(f"An error occurred while loading the data: {e}")
                return None
        return df_list
    

if __name__ == "__main__":
    data = load_data('yellow_tripdata_2015-01.csv')
    if data is not None:
        print(data.head())

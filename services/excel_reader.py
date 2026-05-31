import pandas as pd
import os
from services.validators import (
validate_hours_file,
validate_hours_values,
)


# wczytaj pliki hours
def load_hours_files(folder_path):
    dataframes = []


    for file_name in os.listdir(folder_path):
        if not file_name.endswith(".xlsx"):
            continue

        if file_name == "employees.xlsx":
            continue

        file_path = os.path.join(folder_path, file_name)

        df = pd.read_excel(file_path)
        validate_hours_file(df)
        validate_hours_values(df)
        dataframes.append(df)

    return dataframes

# połącz pliki hours
def combine_hours_data(hours_dataframes):
    combined_df = pd.concat(
        hours_dataframes,
        ignore_index=True
    )
    return combined_df
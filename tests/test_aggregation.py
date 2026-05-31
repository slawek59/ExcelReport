import pandas as pd
from services.excel_reader import(
combine_hours_data)

def test_combine_hours_data():
    df1 = pd.DataFrame({
        "EmployeeId": [1],
        "Hours": [160]
    })

    df2 = pd.DataFrame({
        "EmployeeId": [2],
        "Hours": [170]
    })

    result = combine_hours_data([df1, df2])

    assert len(result) == 2
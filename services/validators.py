import pandas as pd

REQUIRED_EMPLOYEES_COLUMNS = [
    "EmployeeId",
    "Name",
    "Department",
    "HourlyRate"
]

REQUIRED_HOURS_COLUMNS = [
    "EmployeeId",
    "Hours"
]

# sprawdź czy plik zawiera poprawne kolumny
def validate_employee_file(df):
    missing_columns = []

    for column in REQUIRED_EMPLOYEES_COLUMNS:
        if column not in df.columns:
            missing_columns.append(column)

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

# sprawdź czy plik zawiera poprawne kolumny
def validate_hours_file(df):
    missing_columns = []

    for column in REQUIRED_HOURS_COLUMNS:
        if column not in df.columns:
            missing_columns.append(column)

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

# sprawdź czy plik zawiera poprawne wartości
def validate_hours_values(df):
    invalid_rows = df[
        pd.to_numeric(
            df["Hours"],
            errors="coerce"
        ).isna()
    ]
    if not invalid_rows.empty:
        raise ValueError(
            "Hours column contains incorrect values."
        )
# sprawdź czy plik zawiera poprawne wartości

def validate_employee_ids_values(df):
    invalid_rows = df[
        pd.to_numeric(
            df["EmployeeId"],
            errors="coerce"
        ).isna()
    ]
    if not invalid_rows.empty:
        raise ValueError(
            "Employee ID column contains incorrect values."
        )

# sprawdź czy id w plikach się zgadzają
def validate_employee_ids(
        employees_df,
        hours_df
):
    valid_ids = set(
        employees_df["EmployeeId"]
    )

    invalid_ids = hours_df[
        ~hours_df["EmployeeId"].isin(valid_ids)
    ]

    if not invalid_ids.empty:
        raise ValueError(
            f"Found not existing EmployeeId: {invalid_ids}"
        )

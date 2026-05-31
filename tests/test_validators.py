import pandas as pd
import pytest

from services.validators import (
validate_employee_file,
validate_hours_file,
validate_hours_values,
validate_employee_ids
)

def test_validate_employee_file_success():
    df = pd.DataFrame({
    "EmployeeId": [1],
    "Name": ["Jan"],
    "Department": ["IT"],
    "HourlyRate": [50]
    })

    validate_employee_file(df)

def test_validate_employee_file_missing_column():
    df = pd.DataFrame({
    "EmployeeId": [1],
    "Name": ["Jan"]
})

    with pytest.raises(ValueError):
        validate_employee_file(df)

def test_validate_hours_file_success():
    df = pd.DataFrame({
    "EmployeeId": [1],
    "Hours": [160]
    })

    validate_hours_file(df)

def test_validate_hours_values_invalid():
    df = pd.DataFrame({
    "EmployeeId": [1],
    "Hours": ["abc"]
    })

    with pytest.raises(ValueError):
        validate_hours_values(df)

def test_validate_employee_ids_success():
    employees = pd.DataFrame({
    "EmployeeId": [1, 2]
})

    hours = pd.DataFrame({
        "EmployeeId": [1, 2]
    })

    validate_employee_ids(employees, hours)

def test_validate_employee_ids_invalid():
    employees = pd.DataFrame({
    "EmployeeId": [1, 2]
    })

    hours = pd.DataFrame({
        "EmployeeId": [1, 3]
    })

    with pytest.raises(ValueError):
     validate_employee_ids(employees, hours)
import pandas as pd
from services.validators import (
validate_employee_file,
validate_employee_ids,
validate_employee_ids_values
)
from services.excel_reader import(
load_hours_files,
combine_hours_data
)
from services.report_generator import(
generate_report
)

try:
    #wczytanie plików i walidacja
    employees = pd.read_excel("data/employees.xlsx")

    validate_employee_file(employees)
    validate_employee_ids_values(employees)
    hours_dataframes = load_hours_files("data")
    combined_hours = combine_hours_data(hours_dataframes)
    validate_employee_ids(employees, combined_hours)

    #podliczenie godzin dla pracownika
    hours_summary = (
        combined_hours
        .groupby("EmployeeId")["Hours"]
        .sum()
        .reset_index()
    )

    #połączenie employees i hours summary
    report_df = pd.merge(
        employees,
        hours_summary,
        on="EmployeeId",
        how="left"
    )

    #podliczenie wynagrozenia
    report_df["Salary"] = (
            report_df["Hours"]
            *
            report_df["HourlyRate"]
    )

    #podliczenie dla departamentu
    department_summary = (
        report_df
        .groupby("Department")
        .agg(
            TotalHours=("Hours", "sum"),
            TotalSalary=("Salary", "sum")
        )
        .reset_index())

    #wygenerowanie raportu
    generate_report(report_df, department_summary)

except Exception as ex:
    print(f"Error: {ex}")

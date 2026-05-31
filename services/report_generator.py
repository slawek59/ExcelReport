import pandas as pd
from datetime import datetime

# tworzenie i zapisanie raportu
def generate_report(
        report_df,
        department_summary
):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = f"output/final_report_{timestamp}.xlsx"

    # utworzenie pliku
    with pd.ExcelWriter(
            filepath,
            engine="xlsxwriter") as writer:

        # zapisanie raportu pracowników
        report_df.to_excel(
            writer,
            sheet_name="EmployeeReport",
            index=False
        )

        # zapisanie podsumowania działów
        department_summary.to_excel(
            writer,
            sheet_name="DepartmentSummary",
            index=False
        )

        workbook = writer.book

        currency_format = workbook.add_format(
            {
                "num_format": "#,##0.00zł"
            }
        )

        # pobranie arkuszy
        employee_sheet = writer.sheets["EmployeeReport"]
        department_sheet = writer.sheets["DepartmentSummary"]

        employee_sheet.set_column("A:F", 20)
        employee_sheet.set_column("F:F", 20, currency_format)

        department_sheet.set_column("A:C", 20)
        department_sheet.set_column("C:C", 20, currency_format)

        header_format = workbook.add_format({
            "bold": True,
            "border": 1
        })


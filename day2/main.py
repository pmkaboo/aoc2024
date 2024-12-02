from .read_reports import read_reports
from .check_safety import check_safety
from .check_damped_safety import check_damped_safety

if __name__ == "__main__":
    reports = read_reports("day2/reports.txt")
    safe_count = 0
    damped_safe_count = 0
    for report in reports:
        if check_safety(report):
            safe_count += 1
        if check_damped_safety(report):
            damped_safe_count += 1
    print(f"safe count: {safe_count}")
    print(f"damped safe count: {damped_safe_count}")

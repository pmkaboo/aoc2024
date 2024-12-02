import copy

from .check_safety import check_safety

def check_damped_safety(report: list[int]) -> bool:
    result = check_safety(report)
    idx_to_del = 0

    while result == False and idx_to_del < len(report):
        damped_report = copy.copy(report)
        del damped_report[idx_to_del]
        result = check_safety(damped_report)
        idx_to_del += 1

    return result

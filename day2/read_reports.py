def read_reports(path: str) -> list[list[int]]:
    reports = []
    with open(path, "r") as file:
        for line in file.read().split("\n"):
            if line.strip(): # skip empty lines
                report = [int(x) for x in line.split(" ")]
                reports.append(report)
    return reports

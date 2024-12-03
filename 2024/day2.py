def is_safe(report: list):
    def check_gaps(lst):
        gaps = [lst[i] - lst[i - 1] for i in range(1, len(lst))]
        return (all(x > 0 for x in gaps) or all(x < 0 for x in gaps)) and all(abs(x) <= 3 for x in gaps)

    # Check if the original report is safe
    if check_gaps(report):
        return True
    
    # Try removing each element and check if it makes the report safe
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if check_gaps(modified_report):
            return True
    
    return False
    
if __name__ == '__main__':
    safe_report_count = 0
    with open("inputs/day2_input", "r") as infile:
        for reports in infile:
            report = [int(x) for x in reports.strip().split()]
            if is_safe(report):
                safe_report_count += 1
    print(safe_report_count)
                        


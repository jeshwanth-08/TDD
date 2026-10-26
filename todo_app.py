from datetime import datetime

def isOverdue(due_date_str, reference_date_str):
    date_format = "%Y-%m-%d"
    due_date = datetime.strptime(due_date_str, date_format).date()
    reference_date = datetime.strptime(reference_date_str, date_format).date()
    return due_date < reference_date
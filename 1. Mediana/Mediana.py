from statistics import median
from datetime import datetime


example_date_string = "2023-03"
print(example_date_string, type(example_date_string))

example_date_datetime = datetime.strptime(example_date_string, "%Y-%m")
print(example_date_datetime, type(example_date_datetime))

example_date_string = example_date_datetime.strftime("%Y-%m")
print(example_date_string, type(example_date_string))

example_day = "04"


def solution(example_month_and_year, example_current_day):
    list_of_medians = []
    number_day_of_first_sunday = 1 + (6 - example_month_and_year.weekday())
    print(number_day_of_first_sunday)
    example_current_day = int(example_current_day)
    if example_current_day <= number_day_of_first_sunday:
        list_of_values = [1, 2, 3, 4]
        current_median = median(list_of_values)
        list_of_medians.append(current_median)
        print(list_of_medians)
    pass


solution(example_date_datetime, example_day)

"""
def check_is_day_to_count(date):
    format_date = "%Y-%m-%d"
    date = datetime.strptime(date, format_date)
    print(date)
    # for day in date:
    #     print(day)
    pass
    
check_is_day_to_count(example_date)    
"""

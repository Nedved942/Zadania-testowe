from statistics import median
from datetime import datetime


expenses = {
    "2023-01": {
        "01": {
            "food": [22.11, 43, 11.72, 2.2, 36.29, 2.5, 19],
            "fuel": [210.22]
        },
        "09": {
            "food": [11.9],
            "fuel": [190.22]
        }
    },
    "2023-03": {
        "07": {
            "food": [20, 11.9, 30.20, 11.9]
        },
        "04": {
            "food": [10.20, 11.50, 2.5],
            "fuel": []
        }
    },
    "2023-04": {}
}


def solution(dict_with_expenses):
    result = None
    end_list = []
    for year_and_month, days_data in dict_with_expenses.items():
        year_and_month_datetime = datetime.strptime(year_and_month, "%Y-%m")
        number_day_of_first_sunday = 1 + (6 - year_and_month_datetime.weekday())
        for day, lists_of_values in days_data.items():
            current_day = int(day)
            if current_day <= number_day_of_first_sunday:
                current_list = []
                food_values = lists_of_values.get("food", [])
                fuel_values = lists_of_values.get("fuel", [])
                current_list.extend(food_values)
                current_list.extend(fuel_values)
                end_list.extend(current_list)
    result = median(end_list)
    return result


print(solution(expenses))

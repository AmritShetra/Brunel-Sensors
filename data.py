from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

def group_data(data, key_name):
    ''' Group data (input) according to a certain key (input). '''
    grouped_data = defaultdict(list)
    for data_point in data:
        key = data_point[key_name]
        grouped_data[key].append(data_point)
    return grouped_data

def sum_grouped_data(grouped_data, field_name):
    ''' Sums up the grouped data (input) using a provided field name [input]. '''
    summed_data = {}
    for key, data_points in grouped_data.items():
        total = 0
        for data_point in data_points:
            total += data_point[field_name]
        summed_data[key] = total
    return summed_data

def describe_data(data):
    ''' Sums up the data (input) using numpy statistics. '''
    print("Mean:", np.mean(data))
    print("Standard deviation:", np.std(data))
    print("Minimum:", np.min(data))
    print("Maximum:", np.max(data))

def example_method():    # Example usage of methods, with provided data
    data = [
        {"day": "Monday", "occupied": 20},
        {"day": "Tuesday", "occupied": 35},
        {"day": "Wednesday", "occupied": 12},
        {"day": "Thursday", "occupied": 17},
        {"day": "Thursday", "occupied": 18},
        {"day": "Thursday", "occupied": 30},
        {"day": "Friday", "occupied": 11}
        ]

    # Group the data according to the "day" key, which returns several lists
    grouped_data = group_data(data, "day")
    print(grouped_data["Thursday"])
    print(grouped_data["Friday"])
    # Calculate sum of each day/list's values
    total_minutes_by_day = sum_grouped_data(grouped_data, "occupied")
    print(total_minutes_by_day)
    # Get mean, std, min and max from the above list
    total_minutes = list(total_minutes_by_day.values())
    describe_data(total_minutes)
    plt.hist(total_minutes, bins = 3)
    plt.show()
    
    # Pie chart
    labels = list(total_minutes_by_day.keys())
    print(labels)
    sizes = total_minutes
    print(sizes)
    explode = (0, 0, 0, 0.1, 0)
    
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%.1f%%', shadow=True, explode=explode)
    ax.set_aspect('equal')
    plt.title("The usage of the meeting rooms across the week")
    plt.show()

example_method()
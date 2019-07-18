from collections import defaultdict
import numpy as np

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
    ''' Sums up the data using numpy statistics. '''
    print("Mean:", np.mean(data))
    print("Standard deviation:", np.std(data))
    print("Minimum:", np.min(data))
    print("Maximum:", np.max(data))

data = [
    {"day": "Thursday", "occupied": 17},
    {"day": "Thursday", "occupied": 18},
    {"day": "Friday", "occupied": 11}
    ]

grouped_data = group_data(data, "day")
print(grouped_data["Thursday"])
print(grouped_data["Friday"])


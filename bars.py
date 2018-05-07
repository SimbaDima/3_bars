import json
import math


def load_data(file_path_of_user):
    try:
        with open(file_path_of_user) as file_json_format:
            data_format_json = json.load(file_json_format)
    except FileNotFoundError:
        return None
    return data_format_json


def get_biggest_bar(data_format_json):
    features_data_json = data_format_json['features']
    biggest_bar = max(features_data_json, key=lambda x: x['properties']['Attributes']['SeatsCount'])
    return biggest_bar


def get_smallest_bar(data_format_json):
    features_data_json = data_format_json['features']
    smallest_bar = min(features_data_json, key=lambda x: x['properties']['Attributes']['SeatsCount'])
    return smallest_bar


def get_closest_bar(data_format_json, longitude, latitude):
    features_data_json = data_format_json['features']
    closest_bar = min(features_data_json, key=lambda x: math.fabs(longitude - x['geometry']['coordinates'][0] + math.fabs(latitude - x['geometry']['coordinates'][1])))
    return closest_bar


if __name__ == '__main__':
    print("enter path in file")
    path_in_file_of_user = input()
    data_format_json1 = load_data(path_in_file_of_user)
    print("biggest_bar:" + str(get_biggest_bar(data_format_json1)))
    print("smallest bar:" + str(get_smallest_bar(data_format_json1)))
    longitude = float(input("enter longitude: "))
    latitude = float(input("enter latitude: "))
    print(get_closest_bar(data_format_json1, longitude, latitude))

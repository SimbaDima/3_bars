import json
import math
import sys


def load_data_from_file(file_path_of_user):
    try:
        with open(file_path_of_user) as object_of_file:
            data_from_file = json.load(object_of_file)
            bars = data_from_file["features"]
            return bars
    except FileNotFoundError:
        return None


def get_biggest_bar(bars):
    biggest_bar = max(bars,
                      key=lambda x:
                      x['properties']['Attributes']['SeatsCount'])
    biggest_bar_address = biggest_bar["properties"]["Attributes"]["Address"]
    biggest_bar_name = biggest_bar["properties"]["Attributes"]["Name"]
    return biggest_bar_address, biggest_bar_name


def get_smallest_bar(bars):
    smallest_bar = min(bars,
                       key=lambda x:
                       x['properties']['Attributes']['SeatsCount'])
    smallest_bar_address = smallest_bar["properties"]["Attributes"]["Address"]
    smallest_bar_name = smallest_bar["properties"]["Attributes"]["Name"]
    return smallest_bar_address, smallest_bar_name


def get_closest_bar(bars, longitude, latitude):
    try:
        closest_bar = min(
            bars,
            key=lambda x: math.fabs(
                longitude - x["geometry"]["coordinates"][0] + math.fabs(
                    latitude - x["geometry"]["coordinates"][1])))
        closes_bar_address = closest_bar["properties"]["Attributes"]["Address"]
        closest_bar_name = closest_bar["properties"]["Attributes"]["Name"]
        return closes_bar_address, closest_bar_name
    except TypeError:
        return None


if __name__ == '__main__':
    path_in_file_of_user = sys.argv[1]
    data_format_json1 = load_data_from_file(path_in_file_of_user)
    print("biggest bar: in Moscow, him address and name: {}"
          .format(str(get_biggest_bar(data_format_json1))))
    print("smallest bar: in Moscow, him address and name: {}"
          .format(get_smallest_bar(data_format_json1)))
    try:
        longitude = float(sys.argv[2])
        latitude = float(sys.argv[3])
        print("closest bar: in Moscow, him address and name: {}"
              .format(get_closest_bar(data_format_json1, longitude, latitude)))
    except ValueError:
        print("longitude and latitude will be float")

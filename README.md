# What does the code do?
Finds on the input data in JSON format the largest and smallest bar, as well as the nearest bar by the given coordinates

# How to use 

In the console, enter the path to the file

```python 
print("enter path in file")
path_in_file_of_user = input()
```
After you enter the path to the file, and if such a file exists 

```python 
load_data(file_path_of_user):
    try:
        with open(file_path_of_user) as file_json_format:
            data_format_json = json.load(file_json_format)
    except FileNotFoundError:
        return None
    return data_format_json
```
function will return `data_format_json`. If the file does not exist, then an exception will pop up `except FileNotFoundError`

To find the largest bar, you need to use the function
```python
get_biggest_bar(data_format_json):
    features_data_json = data_format_json['features']
    biggest_bar = max(features_data_json, key=lambda x: x['properties']['Attributes']['SeatsCount'])
    return biggest_bar
 ```    
 Using lambda expressions, we find the biggest bar, and return it.
 
 Almost also is the smallest bar 
 ```python
 get_smallest_bar(data_format_json):
    features_data_json = data_format_json['features']
    smallest_bar = min(features_data_json, key=lambda x: x['properties']['Attributes']['SeatsCount'])
    return smallest_bar
 ```
To find the nearest bar, the program request coordinates
 ```python
 longitude = float(input("enter longitude: "))
 latitude = float(input("enter latitude: "))
```

After you enter these coordinates, we call the function
```python 
get_closest_bar(data_format_json, longitude, latitude):
    features_data_json = data_format_json['features']
    closest_bar = min(features_data_json, key=lambda x: math.fabs(longitude - x['geometry']['coordinates'][0] + math.fabs(latitude - x['geometry']['coordinates'][1])))
    return closest_bar
 ```
 which returns the closest bar.
 
# How to start

The script requires the installed Python interpreter version 3.5

Running on Linux:

```bash

$ python bars.py # possibly requires call of python3 executive instead of just python
# FIXME вывести пример ответа скрипта

```

Running on Windows is similar.

# Project Objectives

The code was created for educational purposes. In the framework of the training course on web development- [DEVMAN.org](https://devman.org)

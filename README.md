# Что делает код 
Находит по входным данным в формате JSON самый большой и маленький бар, а также самый близкий бар по заданным координатам 

# Как использовать 

В консоли выведется введите путь к файлу

```python 
print("enter path in file")
path_in_file_of_user = input()
```
После того, как вы введете путь к файлу, и если такой файл существует 

```python 
load_data(file_path_of_user):
    try:
        with open(file_path_of_user) as file_json_format:
            data_format_json = json.load(file_json_format)
    except FileNotFoundError:
        return None
    return data_format_json
```
функция вернет `data_format_json`. Если файла нет, то выскачит исключение `except FileNotFoundError`

Чтобы найти самый большой бар, надо воспользоваться функцией 
```python
get_biggest_bar(data_format_json):
    features_data_json = data_format_json['features']
    biggest_bar = max(features_data_json, key=lambda x: x['properties']['Attributes']['SeatsCount'])
    return biggest_bar
 ```    
 При помощи лямбда выражений, находим самый большой бар, и возвращаем его.
 
 Почти также находится самый маленький бар 
 ```python
 get_smallest_bar(data_format_json):
    features_data_json = data_format_json['features']
    smallest_bar = min(features_data_json, key=lambda x: x['properties']['Attributes']['SeatsCount'])
    return smallest_bar
 ```
 
 Для того чтобы найти самый близкий пар, программа запросить координаты
 ```python
 longitude = float(input("enter longitude: "))
 latitude = float(input("enter latitude: "))
```

И после того как вы введете эти координаты, вызываем функцию
```python 
get_closest_bar(data_format_json, longitude, latitude):
    features_data_json = data_format_json['features']
    closest_bar = min(features_data_json, key=lambda x: math.fabs(longitude - x['geometry']['coordinates'][0] + math.fabs(latitude - x['geometry']['coordinates'][1])))
    return closest_bar
 ```
 которая возвратит самый близкий бар.
 
# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash

$ python bars.py # possibly requires call of python3 executive instead of just python
# FIXME вывести пример ответа скрипта

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)

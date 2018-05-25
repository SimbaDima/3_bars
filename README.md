# What does script do?
These is script helps to find biggest, smallest and closest bar. You need to enter name of file, which contains data about bars in format JSON. Then it is necessary to enter the longitude and latitude for find closest bar. 

# How to use 
In the console the first parameter these is interpreter, second parameter these is path of our script, that enter in function
```python

load_data_from_file(file_path_of_user)

```
then the file is copied in `object_of_file`, after the data is loaded in format JSON 
 ```python 
 
 data_from_file = json.load(object_of_file)

```
These is function return all information about `bars`, from file of user, in format JSON. 
```python

return bars

```
`bars` will be in all next function as parameter


then the bars go into functions
```python 

get_biggest_bar(bars)
get_smallest_bar(bars)

```
also in console we enter parameter: `longitude`, `latitude` for find the function 
```python 

get_closest_bar(bars, longitude, latitude)

```

# Example

I use OS Windows and command line cmd
For start to me need to go in the directory in which is contain file in format JSON and script 

```bash

>cd C:/Users/User/PycharmProjects/firstTask

```
For example script will be called `main5.py`, file in which contains data about bars in format JSON will be called `jsonBar.txt`.
`Longitude` these is third parameter and `latitude` fourth parameter in console.
`longitude = 37.000000000000001`, `latitude = 55.000000000000001`

```bash

>cd C:/Users/User/PycharmProjects/firstTask
>python main5.py jsonBar.txt 37.0000000000000001 55.000000000000001

```
After start we will see in console

```bash

>cd C:/Users/User/PycharmProjects/firstTask
>python main5.py jsonBar.txt 37.0000000000000001 55.000000000000001
biggest bar: in Moscow, him address and name: ('Автозаводская улица, дом 23, строение 1', 'Спорт бар «Красная машина»')
smallest bar: in Moscow, him address and name: ('Дубравная улица, дом 34/29', 'БАР. СОКИ')
coordinates closest bar in Moscow: (36.900000000253, 55.303299999814)
```

# Project Objectives

The code was created for educational purposes. In the framework of the training course on web development- [DEVMAN.org](https://devman.org)

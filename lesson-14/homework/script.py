# 1-write a Python script that reads the students.jon JSON file and prints details of each student.

import json  #importing module Json

with open("students.json") as f: #open .json file as f name
    students = json.load(f)   #using json.load(f) to convert dates from json to python
for student in students["students"]:  
    print("id: ", student["id"])
    print("Name: ", student["name"])
    print("age: ", student["age"])
    print("grade: ", student["grade"])
    print("subjects: ", student["subjects"])
    print("address: ", student["address"])



# 2- 1.1 Use this url : https://openweathermap.org/
#2-1.2 Use the requests library to fetch weather data for a specific city(ex. your hometown: Tashkent) and print relevant information (temperature, humidity, etc.).

import re
import requests
import json
# city = input("input city name: ")
# api_key = input("enter API key: ")
# units = input("enter unit to measurement: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={'Tashkent'}&appid={'9025d3b130efa74bff12dfaca9825907'}&units={'metric'}"

respons = requests.get(url)
data = respons.json()

city = data['name']
country = data['sys']['country']
temperature = data['main']['temp']
feels_like = data['main']['feels_like']
humidity = data['main']['humidity']
wind_speed = data['wind']['speed']
description = data['weather'][0]['description']





#3-  Write a program that allows users to add new books, update existing book information, and delete books from the books.json JSON file.
import json
book_id = input("input book id: ")
book_name = input("input book name: ")
book_author = input("input book author: ")
input_data = {'book_id': book_id,'name' : book_name,'author_name' : book_author}
list_books = []
with open('library.json') as f:
    books = json.load(f)

books.append(input_data)  # assuming books is a list

with open('library.json', 'w') as f:
    json.dump(books, f, indent=4)





"""4-Use this url http://www.omdbapi.com/ to fetch information about movies.
Create a program that asks users for a movie genre and recommends a random movie from that genre."""

import random

genre = input("Enter movie genre: ").lower()

sample_movies = {
    "action": ["Mad Max", "John Wick", "Die Hard"],
    "comedy": ["The Mask", "Step Brothers", "Superbad"],
    "sci-fi": ["Interstellar", "Inception", "The Matrix"]
}

if genre in sample_movies:
    title = random.choice(sample_movies[genre])
    url = f"http://www.omdbapi.com/?apikey=8883064d&t={title}"
    res = requests.get(url)
    data = res.json()
    print("🎬", data["Title"])
    print("Plot:", data["Plot"])
    print("IMDB Rating:", data["imdbRating"])
else:
    print("Genre not found.")


    
        




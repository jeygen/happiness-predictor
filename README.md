# happiness-predictor

## Overview
  
Unsure how you're feeling? Out of touch with your inner self? Look no further than the happiness-predictor!

The happiness-predictor is a lighthearted application that predicts the user's current happiness. </br>
  
- By combining the user's local weather, the price of bitcoin, and cultural sentiment, a score between -1 (bad) </br>
 and 1 (good) is calculated by a state-of-the-art algorithm. 
- The scores and time are saved in a local database, as well as a local csv file. 
- The gui has the option to view a plot of the most recent entries, delete the save files, calculate the </br>
user's happiness score, or exit the program. </br>

This project is an excercise in familiarizing myself with the basics of web scraping, interacting with APIs, </br>
frontend creation, saving/deleting/retrieving data, natural languaging processing, and data visualization. </br>

The location, weather, and bitcoin price are an excercise in APIs. The New York Times and a randomly selected poem </br>
are used to practice web scraping scraping and language processing. The gui is frontend practice and the backend </br>
is an excercise in CRUD. 

![happiness-predictor]('screenshot.png)

## Getting Started

After forking/cloning the repo, the program will run by executing the gui.py module. </br>

**Neccesary depedencies:** pandas, matplotlib, json, requests, sqlite3, datetime, time, os, numpy, beautifulsoup4 , </br>
vaderSentiment, tkinter, pillow </br>
  
  
  


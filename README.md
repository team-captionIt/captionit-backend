# captionit-backend


***CONSISTS OF TWO BACKEND FILES NAMELY first.py and rev_1f-Copy.py***


## Pre-requisites for backend


Download data set from https://www.kaggle.com/manann/quotes-500k?select=quotes.csv and ensure its location as C:/quotes1.csv


Run following codes on terminal to install pre-requisites if not present

`pip install spacy`


`python -m spacy download en_core_web_sm`

`pip install flask flask-cors`

## Installation
Clone this repository and run first.py


## Details 
In the rev_1f-Copy.py file, we have the main backend code which handles the Natural Language Processing(NLP) algorithm.
This file uses the "spacy" library to find necessary keywords from a given statement. Using this, we are able to parse
keywords from the information extracted from the image.


After the keywords are found, they are searched throughout the dataset using the "pandas" library and the most appropriate quotes(having maximum corresponding keywords) are stored in a list.
In the first.py file, we have the flask app which is used to process the API request given by the extension. 
Using this, we define routes which output the relevant quotes.

# captionit-backend
***CONSISTS OF TWO BACKEND FILES NAMELY first.py and rev_1f-Copy.py***
In the rev_1f-Copy.py file, we have the main backend code which handles the Natural Language Processing(NLP) algorithm.
This file uses the "spacy" library to find necessary keywords from a given statement. Using this, we are able to parse
keywords from the information extracted from the image.


After the keywords are found, they are searched throughout the dataset using the "pandas" library and the most appropriate quotes(having maximum corresponding keywords) are stored in a list.
In the first.py file, we have the flask app which is used to process the API request given by the extension. 
Using this, we define routes which output the relevant quotes.

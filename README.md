# Meme Generator

This program is a Meme Generator complying with the project Motivational Meme Generator specs from Udacity Nanodegree Intermediate Python

## Project Overview:

The project offers to the users two ways to interact with the Meme Generator:

    - Via Command line by executing the command python3 meme.py with three optional arguments:
        --body: The quote body
        --author: The quote author
        --path: The path to the image file to use for the meme.
      If the optional arguments are not provided, the meme will be created by randomly choosing quotes and images from a set available in the project. This sample set of images and quotes are inspired in Homer Simpson character.
      The command returns the path to the generated meme if the result is successful.

    - Via web interface by accessing in a web browser http://localhost:3000/
        The web inteface offers the user two possibilities:
            * Generate the meme randomly, in the same fashion as when the user don't provide the optional arguments on the command line interface. 
            * Create the meme with the details provided by the user on a form, in the same way as when the user provides the three optional arguments on the command line interface, except that for the image, it is not a path but an URL, from where, the image will be downloaded.
        In both cases if the meme is successfully generated, it will be displayed in the web browser, otherwise an error message will be displayed instead.

## Pre-requisites and instructions:

Prerequisites:

- This program depends on an external program to read PDF files named XpdfReader. Instructions for the instalation of XpdfReader utility can be found here https://www.xpdfreader.com/pdftotext-man.html  

- The python version used to develop and test the program is 3.10.7


Instructions:

It is recommended to use virtual environments to execute this program, although is not mandatory. To create your virtual environment just run python3 -m venv venv_name . Depending on the OS where the user runs the program, you may need to install a dependency before creating your virtual environment. More information here: https://docs.python.org/3/library/venv.html

The program has some dependencies that should be fulfilled before the program can be executed. A file requirements.txt is provided so that the user can install the dependencies easily by running the command pip install -r requirements.txt from src folder.

Once this is done the command line interface for the meme generator can be used.

For the web interface it is necessary to start the Flask server beforehand. To do so, just execute these two commands from your terminal from src folder: 
    export FLASK_APP=app.py
    flask run --host 0.0.0.0 --port 3000 --reload

Then on your browser navigate to localhost:3000 to access the web interface of the meme generator.


"""A module encapsulating a web application build with Flask to generate random memes or build them via user input data."""

import random
import os
import requests
from flask import Flask, render_template, abort, request

# Import your Ingestor and MemeEngine classes
from quote_engine import Ingestor
from MemeGenerator import MemeGenerator

app = Flask(__name__)

meme = MemeGenerator('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/SimpleLines/SimpleLines.txt',
                    './_data/SimpleLines/SimpleLines.docx',
                    './_data/SimpleLines/SimpleLines.pdf',
                    './_data/SimpleLines/SimpleLines.csv']

    # Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/hommer/"

    # Use the pythons standard library os class to find all
    # images within the images images_path directory
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array

    img = random.choice(imgs)
    quote = random.choice(quotes)
    try:
        path = meme.make_meme(img, quote.body, quote.author)
    except BaseException as ex:
        return render_template('meme.html', path='', error_msg=str(ex))
    else:
        return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.
    img_url = request.form.get('image_url')
    quote_body = request.form.get('body')
    quote_author = request.form.get('author')
    response = requests.get(img_url)
    isImage = response.headers['content-type'].startswith('image')
    if isImage:
        tmpImg = f'./tmp/{random.randint(0,100000000)}.jpg'

        try:
            with open(tmpImg, 'wb') as img:
                img.write(response.content)

            path = meme.make_meme(tmpImg, quote_body, quote_author)
        except BaseException as ex:
            return render_template('meme.html', path='', error_msg=str(ex))
        else:
            return render_template('meme.html', path=path)
        finally:
            os.remove(tmpImg)
    else:
        return render_template('meme.html', path='', error_msg='Invalid image provided.')


if __name__ == "__main__":
    app.run()

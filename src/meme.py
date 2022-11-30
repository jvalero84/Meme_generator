"""A module that allows a user to generate memes via Command Line."""

import os
import random
import argparse
from MemeGenerator import MemeGenerator

from quote_engine import QuoteModel, Ingestor

def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote."""
    img = None
    quote = None
    
    try:
        if path is None:
            images = "./_data/photos/hommer/"
            imgs = []
            for root, dirs, files in os.walk(images):
                imgs = [os.path.join(root, name) for name in files]

            img = random.choice(imgs)
        else:
            img = path

        if body is None:
            quote_files = ['./_data/SimpleLines/SimpleLines.txt',
                        './_data/SimpleLines/SimpleLines.docx',
                        './_data/SimpleLines/SimpleLines.pdf',
                        './_data/SimpleLines/SimpleLines.csv']
            quotes = []
            for f in quote_files:
                quotes.extend(Ingestor.parse(f))
            quote = random.choice(quotes)
        else:
            if author is None:
                raise Exception('Author Required if Body is Used')
            quote = QuoteModel(body, author)

        mg = MemeGenerator('./tmp')

        path = mg.make_meme(img, quote.body, quote.author)
    except BaseException as ex: 
        return str(ex)
    else:
        return path


if __name__ == "__main__":
    # Use ArgumentParser to parse the following CLI arguments
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image
    #args = None

    parser = argparse.ArgumentParser(description="Generate a Meme..")
    parser.add_argument('--body', type=str, help="string quote body")
    parser.add_argument('--author', type=str, help="string quote author")
    parser.add_argument('--path', type=str, help="path to image file")
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))

    
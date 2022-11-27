import os
import random
import argparse
from MemeGenerator import MemeGenerator

from quote_engine import QuoteModel, Ingestor

def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))
        print(f'Number of quotes collected: {len(quotes)} ')
        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    mg = MemeGenerator('./tmp')
    path = mg.make_meme(img, quote.body, quote.author)
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

    
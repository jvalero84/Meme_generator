"""A module containing a MemeGenerator class."""

from PIL import Image, ImageFont, ImageDraw
from quote_engine import QuoteModel
from pathlib import Path
import random

class MemeGenerator:
    """A class to handle the loading of images from disk and its manipulation to generate Memes."""

    def __init__(self, output_dir:str):
        """Construct a MemeGenerator object initializing its path attribute."""
        self.output_dir = output_dir
    
    def make_meme(self, img_path, text, author, width=500) -> str: 
        """Generate a meme with the image given, a max with defined by with argument and the quote provided."""
        try:
            with Image.open(img_path) as im:
                ratio = width/float(im.size[0])
                height = int(ratio*float(im.size[1]))
                im = im.resize((width, height), Image.NEAREST)

                if text is not None and author is not None:
                    font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=18)
                    d = ImageDraw.Draw(im)
                    quote = QuoteModel(text, author)
                    quote_width = font.getlength(str(quote))
                    x_pos = 5 if quote_width > im.size[0] else random.randint(0, im.size[0] - quote_width)
                    quote_text = f'{quote}' if quote_width < im.size[0] else f'\"{quote.body}\"\n - {quote.author}'
                    d.text((x_pos, random.randint(20,im.size[1]-40)), quote_text, font=font, fill='black')
                
                out_file = Path(self.output_dir) / f'{random.randint(1,1000)}.jpg'
                im.save(out_file)
        except BaseException as ex:
            print(ex)
            raise(Exception('Unable to generate Meme.'))
        return out_file
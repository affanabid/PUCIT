import string, random

import random
fruits = ['Apples',
'Apricots',
'Avocados'
'Bananas',
'Bing Cherry',
'Blueberries',
'Boysenberries',
'Cantaloupe',
'Cherries',
'Clementine',
'Crab apples',
'Cucumbers',
'Damson plum',
'Dates',
'Dewberries',
'Dinosaur Eggs',
'Dragon Fruit',
'Eggfruit',
'Elderberry',
'Entawak',
'Evergreen Huckleberry',
'Farkleberry',
'Fig',
'Finger Lime',
'Gooseberries',
'Grapefruit',
'Guava',
'Hackberry'
'Honeycrisp Apples',
'Imbe',
'Indonesian Lime',
'Jackfruit',
'Jambolan',
'Java Apple',
'Kaffir Lime',
'Kiwi',
'Kumquat'
'Lime (Lemon)',
'Longan',
'Loquat',
'Lychee',
'Mango',
'Melon',
'Mulberry',
'Nashi Pear',
'Navel Orange',
'Nectarine',
'Ogeechee Limes',
'Olive',
'Oranges',
'Oval Kumquat',
'Papaya',
'Paw Paw',
'Peach',
'Pineapple',
'Pomegranate',
'Prickly Pear',
'Quararibea cordata',
'Queen Anne Cherry',
'Quince',
'Rambutan',
'Raspberries',
'Star Fruit',
'Strawberries',
'Sugar Baby Watermelon',
'Tamarind',
'Tangerine',
'Tart Cherries',
'Tomato',
'Ugni',
'Uniq Fruit',
'Vanilla Bean',
'Velvet Pink Banana',
'Voavanga',
'Watermelon',
'White Mulberry',
'Wolfberry',
'Xango Mangosteen',
'Xigua',
'Ximenia caffra fruit',
'Yangmei',
'Yellow Passion Fruit',
'Yunnan Hackberry',
'Zig Zag Vine fruit',
'Zinfandel Grapes',
'Zucchini']

class Codec:

    def __init__(self) -> None:
        self.map = {}
        self.pool = string.ascii_lowercase + string.digits
        self.random_chars = random.choices(self.pool, k=5)
        self.random_string = ''.join(self.random_chars)

    def encode(self, fruit: str) -> str:
        shortURL = self.random_string
        self.map[shortURL] = fruit
        
        return 'http//tinyurl/' + shortURL        

    def decode(self, shortUrl: str) -> str:
        shortUrl = shortUrl.split('/')[-1]
        longURL = self.map[shortUrl]
        return longURL

s = Codec()     
for fruit in fruits:
    s.encode(fruit)
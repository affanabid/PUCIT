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


# print(fruits)
size = 900
hashtable = [None] * size
def hashfunction(fruit, size):
    
    hsh = 0
    i = 0
    for f in fruit:
        hsh += ord(f)
    salt = ord(fruit[-1]) + ord(fruit[-2])
    hsh += salt
    hsh += random.randint(0, 5)
    return hsh % size
    # start = fruit[0]
    # end = fruit[-1]
    # mid = fruit[len(fruit) // 2]
    # hsh = ord(start) + ord(end) + ord(mid)
    # return hsh % size

def insert(fruit, map, size):
    hsh = hashfunction(fruit, size)
    if map[hsh] is None:
        map[hsh] = fruit
        return True
    else:
        return False        

count = 0
for fruit in fruits:
    if insert(fruit, hashtable, size):
        count += 1
    else:
        break
print(count)
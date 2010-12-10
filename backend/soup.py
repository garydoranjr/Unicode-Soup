from random import sample
from backend import SOUP

def soupify(string):
    soupy = []
    for char in string:
        if char in SOUP:
            can = SOUP[char]
            soupy.extend(sample(can, 1))
        else:
            soupy.append(unicode(char))
    return u''.join(soupy)

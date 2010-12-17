#!/usr/bin/env python
import unicodedata
import string
import re

def get_characters(letter):
    print letter
    if letter in string.ascii_lowercase:
        search = r'SMALL LETTER %s\b' % letter.upper()
    else:
        search = r'CAPITAL LETTER %s\b' % letter

    characters = []
    for i in range(0xFFFFF):
        c = unichr(i)
        try:
            name = unicodedata.name(c)
        except ValueError as e:
            continue

        if re.search(search, name):
            characters.append(c)

    return ''.join(characters)

char_map = {}
for lower in string.ascii_letters:
    char_map[lower] = get_characters(lower)

for k,v in char_map.items():
    print "'%s' : u'%s'," % (k, v)

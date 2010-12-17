#!/usr/bin/env python
import unicodedata
import string

def get_characters(letter):
    if letter in string.ascii_lowercase:
        search = 'SMALL LETTER %s ' % letter.upper()
    else:
        search = 'CAPITAL LETTER %s ' % letter

    characters = []
    for i in range(0xFFFF):
        c = unichr(i)
        try:
            name = unicodedata.name(c)
        except ValueError as e:
            continue

        if name.find(search) >= 0:
            characters.append(c)

    return ''.join(characters)

char_map = {}
for lower in string.ascii_letters:
    char_map[lower] = get_characters(lower)

for k,v in char_map.items():
    print "'%s' : u'%s'," % (k, v)

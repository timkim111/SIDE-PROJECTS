#!/usr/bin/env python3

import sys
from ucb import main
from mr import values_by_key, emit
from itertools import permutations

tab = {'a': '._ ', 'b': '-... ', 'c': '-.-. ', 'd': '-.. ', 'e': '. ',
        'f': '..-. ', 'g': '--. ', 'h': '.... ', 'i': '.. ',
        'j': '.--- ', 'k': '-.- ', 'l': '.-.. ', 'm': '-- ',
        'n': '-, ', 'o': '--- ', 'p': '.--. ', 'q': '--.- ',
        'r': '.-. ', 's': '... ', 't': '- ', 'u': '..- ',
        'v': '...- ', 'w': '.-- ', 'x': '-..- ', 'y': '-.-- ',
        'z': '--.. ', '1': '.---- ', '2': '..--- ', '3': '...-- ',
        '4': '....- ', '5': '..... ', '6': '-....', '7': '--...',
        '8': '---.. ', '9': '----. ', '0': '----- ', ' ': '/ ', '.': '.-.-.- ', ',': '--..-- ', ':': '---... ', '?': '..--.. ', '\'': '.----. ', '-': '-....- ', '/': '-..-. ', '(': '-.--.- ', ')': '-.--.- ', '\"': '.-..-. ', '!': '-.-.-- ', ';': '-.-.-. ',

        }

tab_morse_and_len = {}
for item in tab:
    tab_morse_and_len[item] = (tab[item], len(tab[item]))

def translate(engstring):
    engstring = engstring.lower()
    translated = ''
    for char in engstring:
        if char in tab:
            translated += tab[char]
    return translated

def randomize(dct):
    """returns an iterator and
    it is an example of a generator function"""
    perms = permutations(dct, len(dct)) #perm is an iterator that contains a different mix of the keys of dct
    old_values = list(dct.values())
    for perm in perms:
        new_dct = {}    
        for char in perm:
            index = perm.index(char)
            new_value = old_values[index]
            new_dct[char] = new_value
        yield new_dct

@main
def run():
    perms = randomize(tab_morse_and_len)
    instances = {}
    num_morse_chars_lowest = 0
    trash = 0
    tab_lowest = tab_morse_and_len
    for key, value_iterator in values_by_key(sys.stdin):
        if key in tab_morse_and_len:
            num_instances_of_key = sum(value_iterator)
            instances[key] = num_instances_of_key
            num_morse_chars_lowest += num_instances_of_key * tab_morse_and_len[key][1]
        else:
            trash = sum(value_iterator) #if the value_iterator isnt used up infinite loop seems to occur
    morse_chars = 0 
#   emit('standard morse code', num_morse_chars_lowest)
    for inst in instances:
        emit(inst, instances[inst])
#   emit('here are the instances', instances)
    """
    for char in instances:
        morse_chars += instances[char] * tab_morse_and_len[char][1]
    try:
        for perm in perms:
            sum_chars = 0
            for char in instances:
                sum_chars += instances[char] * perm[char][1]
            if sum_chars < num_morse_chars_lowest:
                num_morse_chars_lowest = sum_chars
                tab_lowest = perm
            emit(perm, num_morse_chars_lowest)
        emit('Original morse code used this many lines', morse_chars)
        emit('The optimized morse code is', num_morse_chars_lowest)
        emit('The table for this was', tab_lowest)
    except KeyboardInterrupt as e:
        emit('Original morse code used this many lines', morse_chars)
        emit('The most efficient discovered morse code is', num_morse_chars_lowest)
        emit('The table for this was', tab_lowest)       
    """






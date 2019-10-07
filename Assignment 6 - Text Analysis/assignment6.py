"""
Swapnav Deka
COMP 130
Assignment 6

This assignment tests use of regular expressions among
other Python information.
"""

import re
import urllib2
import codeskulptor
from collections import Counter
from math import floor
from collections import defaultdict

############################################
# Helper functions from class assignments. #
###########################################

def is_punctuation(string):
    """
    Returns whether or not the given string consists only of punctuation.
    """
    for char in string:
        if char not in "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~":
            return False
        else:
            is_punk = True
    return is_punk

def words(string_list):
    """
    Takes a list of strings and returns a new list that contains all the 
    words and numbers.
    """
    newlist = []
    for string in string_list:
        if is_punctuation(string) == False:
            newlist.append(string)
    return newlist 

def word_no_longer_counts_file(filename, include_punc, is_case_sensitive):
    """
    Takes a filename, and booleans indicating whether or not to include
    punctuation and whether or not text is case-sensitive. It returns a
    list of all the words in the file.
    """
    a_file = urllib2.urlopen(codeskulptor.file2url(filename))
    text = a_file.read()
    if is_case_sensitive == False:
        text = text.lower()
    wordlist = re.findall(r"[?!]+|-+|\.+|[,:;\"'`()/&#]|-?[A-Za-z0-9]+(?:['\-.@/][A-Za-z0-9]+)*|-?\$?\d{1,3}(?:,?\d{3})*(?:\.\d+)?", text)
#    counter = Counter()
#    for word in wordlist:
#        if is_punctuation(word) == False:
#            counter[word] += 1
#    return counter
    if include_punc == False:
        wordlist = words(wordlist)
    return wordlist

def next_seq(prev_tuple, new_element):
    """
    Takes an n-pair, i.e., a tuple of n elements, (x0, x1, ..., xn). 
    It returns a pair (x1, x2, ..., xn, new_element)
    """
    mylist = list(prev_tuple)
    mylist.pop(0)
    mylist.append(new_element)
    mytuple = tuple(mylist)
    return mytuple

##########################
# Assignment 6 functions #
#########################

def findall_sl(text):
    """
    This function returns elements of a string that
    begin with 	'sl.'
    """
    pattern = r"\bsl+[a-z]+"
    return re.findall(pattern, text, re.I)
    
def findall_triple_vowel(text):
    """
    This function returns elements of a string that have
    three or more consecutive, identical vowels.
    """
    pattern = '[a-z]*[a]{3}[a-z]*|[a-z]*[e]{3}[a-z]*|[a-z]*[i]{3}[a-z]*|[a-z]*[o]{3}[a-z]*|[a-z]*[u]{3}[a-z]*'
    return re.findall(pattern, text, re.I)

def findall_80s(text):
    """
    This function returns elements of a string that contain 
    references to the 1980s.
    """
    pattern = '198[1-9]|[19]*80[s]*|eighties|nineteen eighty[-]?[a-z]*'
    return re.findall(pattern, text, re.I)

def count_distinct_words(filename):
    """
    This function returns a count of the number of distinct words 
    that occur in the provided text file.
    """
    data = urllib2.urlopen(codeskulptor.file2url(filename))
    text = data.read()
    newtext = "".join(char for char in text if char not in "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~")
    return len(set(re.findall('\w+', newtext.lower())))

def median_word(filename):
    """
    This function returns a word that has the median of all 
    the number of word occurrences.
    """
    data = urllib2.urlopen(codeskulptor.file2url(filename))
    text = data.read()
    newtext = "".join(char for char in text if char not in "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~")
    wordlist = re.findall('\w+', newtext.lower())
    counter = Counter()
    for word in wordlist:
        counter[word] += 1
    newlist = counter.most_common()
    length = len(newlist)
    index = floor(length / 2)
    return newlist[int(index)][0]

def wordseq_successor_counts(filename, seq_size, include_punc, is_case_sensitive):
    """
    This function returns a default dictionary, where each key is a 
    seq_size-element tuple of words. Each key's value is a Counter 
    mapping distinct successor words to their counts.
    """
    wordlist = word_no_longer_counts_file(filename, include_punc, is_case_sensitive)   
    counter = defaultdict(Counter)
    current = tuple(wordlist[:seq_size])
    next_ = wordlist[seq_size]
    counter[current][next_] = 1
    remaininglist = wordlist[seq_size+1:]
    for a_word in remaininglist:
        current = next_seq(current, next_)
        next_ = a_word
        counter[current][next_] += 1
    return counter   

def wordseq_successor_frequencies(filename, seq_size, include_punc, is_case_sensitive):
    """
    The function returns a default dictionary, where each key is a 
    seq_size-element tuple of words. Each key's value is a regular 
    (non-default) dictionary mapping distinct successor words to 
    their frequencies, i.e., their percentage of occurrence.
    """   
    map_ = defaultdict(dict)
    mycount = wordseq_successor_counts(filename, seq_size, include_punc, is_case_sensitive)
    for elem in mycount:
        total = sum(mycount[elem].values())
        for count in mycount[elem]:
            map_[elem][count] = float(mycount[elem][count]) / total
    return map_
"""
Swapnav Deka
COMP 130
Assignment 7: Text Riffing

This assignment tests knowledge of Markov chains among
other Python information.
"""

############################################
# Helper functions from class assignments. #
###########################################

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

def disjoint2(set1, set2):
    """
    This function returns a Boolean indicating whether the two sets 
    are disjoint.
    """
    for elem in set1:
        if elem in set2:
            return False
    return True

##########################
# Assignment 7 functions #
#########################

def random_choice_weighted(choices, random_fn):
    """
    This function takes a dictionary where each possible choice is 
    mapped to its probability and returns one of the choices picked 
    randomly with respect to the weighted probabilities. It takes a 
    function that takes no argument and returns a value from 0 to 1. 
    """
    choice = random_fn()
    pairs = choices.items()
    for key, value in pairs:
        if choice <= value:
            return key
        else:
            choice = choice - value

def generate_text(chain, num_words, starting_fn, random_fn):
    """
    This function, given a Markov chain, generates a random sequence of 
    the given number of words using an algorithm. The result can be shorter 
    than the specified number of words if the generation routine happens to 
    comes across a word sequence with no successor.  It returns a string of 
    the resulting text.
    """
    words = starting_fn(chain)
    chain_len = len(words)
    wordlist = []
    for word in words:
        wordlist.append(word)
    for num in range(num_words - chain_len):
        num = num
        if words in chain.keys():
            next_word = random_choice_weighted(chain[words], random_fn)
            words = next_seq(words, next_word) 
            wordlist.append(next_word)
        else:
            break
    return ' '.join(wordlist)

def neural_net(input_node_set, num_hidden_nodes, output_node_set):
    """
    This function takes two sets and one integer. It returns a directed graph, 
    which is a slightly simplified version of an artificial neural network.
    """
    if num_hidden_nodes <= 0:
        return None
    elif len(input_node_set) == 0:
        return None
    elif len(output_node_set) == 0:
        return None
    elif not disjoint2(input_node_set, output_node_set):
        return None
    else:
        mydict = {}
        empty_set = set([])
        nodes = range(num_hidden_nodes)
        for elem in input_node_set: 
            mydict[elem] = set(range(num_hidden_nodes))
        for elem in output_node_set:
            mydict[elem] = empty_set
        for elem in nodes:
            mydict[elem] = output_node_set
        return mydict


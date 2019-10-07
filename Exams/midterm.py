"""
Swapnav Deka (sd55)
COMP 130
Duncan Hall 1070
Tuesday, February 22, 2016

This is the first exam for COMP 130.

Honor Code: On my honor, I have neither given nor received any unauthorized
aid on this exam.
-Swapnav Deka
"""

##########################################################################
# TEXT PART

#################
# Problem 1 (10 points)
#
# What is the main point of writing a "recipe"?

# A recipe provides instructions on how to implement something. However,
# a recipe is not dependent on program code, so it should be able to be 
# translated to any other program language. A recipe is able to provide a 
# detailed outline of the function, including inputs, outputs, and a step-
# by-step process of how to produce the outputs from the inputs. Therefore, 
# a recipe can be used to easily recreate or understand the process that 
# is occurring in the function.


#############
# Problem 2 (10 points)
# With our first version of the predator-prey population-modelling code,
# we often saw negative populations.  Such data is impossible in real life.
# Assuming that the Lotka-Volterra equations accurately model the real world,
# describe in your own words why our initial code obtained anomalous results and
# why adding time steps alleviated this problem. 

# Logically, taking annual data is less efficient. When you take more 
# frequent time steps, the model is more accurate. Another reason (also 
# mentioned by my CAAM 210 TA) is that coding implementations often use 
# difference equations while an actual predator-prey model uses differential 
# equations. Differential equations describe continuous functions while 
# difference equations don't, so incorporating smaller time intervals make 
# the model more accurate by minimizing the difference between difference
# and differential equations.


##########################################################################
# PYTHON PART

# (5 points) Code style -- Checked by OwlTest/CanvasTest.

# (5 points) Docstrings -- Accurately and precisely describe each
# function's results.


#############
# Problem 1 (20 points)
#
# The Collatz conjecture is a funny little math problem.  The idea is
# that we'll start with a positive integer.  If it's even we'll
# divide it by 2, but if it's odd we'll multiply by 3 and then add 1.
# We then repeat.  We stop when we reach 1.  So, sometimes the number
# gets smaller, but sometimes it gets bigger.  The conjecture states
# that for any starting number, we eventually reach 1 and stop.  This
# conjecture has never been proven.
#
# Starting with the number 1, we immediately stop in 0 steps.
# Starting with the number 2, we get 1, and stop in 1 step.
# Starting with the number 3, we get 10, then 5, 16,
# 8, 4, 2, and finally 1.  That took 7 steps.
# Starting with the number 4, we get 2, 1, in 2 steps.
# ...
# Starting with the number 7, we get 22, 11, 34, 17, 52, 26, 13, 40,
# 20, 10, 5, 16, 8, 4, 2, 1.  That took 16 steps.
#
# For the version that you'll write, think of having a little
# Collatz machine that does the computation described above.
# We're going to give it a limit on how many times it is allowed
# to iterate the process.  Your function collatz_limit(limit),
# given a non-negative integer, will return the smallest integer that is
# still going when it runs into that limit.
#
# Example: collatz_limit(10) should return 7.  As shown above, starting
# with 1, 2, ..., 6 each is done within 10 steps.  Starting with 7,
# we haven't finished after 10 steps, so we stop and return 7.
# (Note that this description hints at how to decompose the problem.)
# 


def collatz(num):
    """
    This function computes the math problem 'The Collatz conjecture.' It
    is a helper function that is used in the following 'collatz_limit' function.
    It returns the number of steps taken by a non-negative number to reach 1
    following mathematical operations.
    """   
    steps = 0 #Counter for total steps taken for Collatz
    while num > 1: #Continues to run until number reaches 1
        if num % 2 == 0: #If num is even, applies the following
            num = num / 2
            steps = steps + 1 #Increments step counter
        else: #If num is odd, applies the following
            num = (3 * num) + 1
            steps = steps + 1 #Increments step counter
    return steps #Returns total number of steps taken


def collatz_limit(limit):
    """
    This function returns the smallest integer that has not yet been
    reduced to 1 when the number of steps taken (given by the preceeding helper
    function 'collatz') exceeds the limit.
    """
    num = 0 #Initial condition of helper function above
    while collatz(num) <= limit: #Continues to run while total steps has not
        #reached the specified limit
        num = num + 1 
        collatz(num)
        #If total steps is less than limit, num is incremented by 1 and 
        #collatz is calculated again. This repeats until the limit is reached.
    return num 
    #Returns value of num, smallest integer still going when limit is reached 
   
    
# For the next two problems, represent a 2-dimensional matrix as a
# list of lists of numbers.  For example, the matrix
# (1 2 3)
# (4 5 6)
# (7 8 9)
# would be represented as
# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]

    
#############
# Problem 2 (15 points)
#
# Define a function diag_matrix(diag_nums)
# that takes a list of numbers and returns a diagonal square matrix having
# those numbers along the diagonal.  A diagonal matrix has non-zero data
# only along the diagonal that starts in the upper-left.
#
# Example: diag_matrix([1, 2, 3]) should return
# [[1, 0, 0],
#  [0, 2, 0],
#  [0, 0, 3]]


def diag_matrix(diag_nums):
    """
    This function takes a list of numbers and returns a diagonal square
    matrix having those numbers along the diagonal.
    """    
    counter = len(diag_nums) #This counter contains the length of the 
    #input list 'diag_nums'
    mymatrix = [[0 for dummy_num in range(counter)] for dummy_num in range(counter)]
    #Creates a list containing 'counter' lists containing 'counter; # of zeros
    #Essentially, creates a matrix containing all zeros with dimensions 
    #'counter' x 'counter'
    matrixcounter = 1 
    while (counter - matrixcounter) >= 0: #This while loop makes use of both
        #counters. It runs while the value is not negative. 
        mymatrix[counter-matrixcounter][counter-matrixcounter] = diag_nums[counter-matrixcounter]
        #Replaces the index (counter-matrixcounter) in 'mymatrix' with the 
        #same index from 'diag_nums' 
        matrixcounter = matrixcounter + 1 #After each loop, matrixcounter is 
        #incremented by 1 so while loop stops before index is out of range.
    return mymatrix #returns the matrix


#############
# Problem 3 (15 points)
#
# Define a function sparse_matrix(matrix)
# that takes a rectangular matrix represented as a list of lists, as
# previously described, and returns the same matrix represented as a
# dictionary.  The dictionary maps (row,column) pairs to the corresponding
# matrix value, but only includes the non-zero values.  The dictionary
# also maps the special values "rows" and "columns" to the numbers of
# rows and columns, respectively, in the matrix.
#
# NOTE: Return a regular dictionary, not a default dictionary.
#
# Example: sparse_matrix([[1, 0, 0], [0, 0, 2], [3, 0, 0], [0, 0, 0]])
# should return {(0, 0): 1, (1, 2): 0, (2, 0): 3, "rows": 4, "columns": 3}


def sparse_matrix(matrix):
    """
    This function takes a rectangular matrix represented as a list of
    lists and returns the same matrix represented as a dictionary. The
    dictionary maps pairs of (row, column) indices to corresponding matrix
    values for non-zero components of the matrix.
    """    
    mydict = {} #Creates an empty dictionary
    mydict["rows"] = len(matrix) #Adds the key 'rows' to the dictionary
    #and its corresponding value, which is the length of the matrix
    for a_list in matrix: #Iterates over each list in the matrix
        mydict["columns"] = len(a_list) #Adds the key 'columns' to the 
        #dictionary and its corresponding value, which is the length of 
        #a list in the matrix
        for num in a_list: #Iterates over numbers in the lists
            if num != 0: #Disregards non-zero values
                dictuple = (matrix.index(a_list), a_list.index(num))
                #Creates a tuple of the (row, column) indices
                mydict[dictuple] = num #Adds each tuple as a key to
                #the dictionary and its corresponding number
    return mydict #returns the dictionary


#################
# Problem 4 (20 points)
#
# Think of shuffling a deck of cards.  We split the deck
# in half, or roughly so.  Then we interleave the cards
# from the two groups.  With sufficient practice, you
# can interleave the cards perfectly, alternating cards
# from the two groups.
#
# Write a function interleave() that takes two lists and
# creates a new list, alternating cards from the two lists.
# The resulting list starts with the first card from the
# longer list (or the first list, in the case of equal
# lengths).  Any "extra" elements of the longer list
# are put at the end of the new list.
#
# Example:  interleave(['a', 'b'], [1, 2, 3, 4]) should
# result in [1, 'a', 2, 'b', 3, 4].


def interleave(list1, list2):
    """
    This function takes two lists and creates a new list, alternating
    values from the two lists. The first element is from the longer
    list (or the first list if they are equal in length). Extra elements
    are added to the end of the resulting list.
    """
    copyoflist1 = list(list1) #In case input parameter mutation is disallowed
    copyoflist2 = list(list2) #In case input parameter mutation is disallowed
    cardlist = [] #Creates empty list
    list1_counter = 0 #Counter for the indices in first list
    list2_counter = 0 #Counter for the indices in second list
    if len(list1) < len(list2): #If 2nd list is longer
        while list1_counter <= len(list1) - 1: #While the index counter is
            #in the range of total indices (reason for -1)
            cardlist.append(copyoflist2[list2_counter])
            cardlist.append(copyoflist1[list1_counter])
            #Above commands alternatingly append elements of lists to
            #'cardlist' (from longer list first) 
            #Shorter list determines when to stop.
            copyoflist2.pop(list2_counter) #Removes elements from longer list as
            #they are appended to 'cardlist' so that only unused elements remain
            list1_counter = list1_counter + 1 #After each loop, the longer 
            #list counter is incremented by 1 so while loop stops before 
            #index is out of range
        return cardlist + copyoflist2 #Returns 'cardlist' with unused elements of
        #longer list appended to end
    elif len(list1) >= len(list2): #If first list is longer, or if equal
        while list2_counter <= len(list2) - 1: #While the index counter is
            #in the range of total indices (reason for -1)
            cardlist.append(copyoflist1[list1_counter])
            cardlist.append(copyoflist2[list2_counter])
            #Above commands alternatingly append elements of lists to
            #'cardlist' (from first/longer list first) 
            #Shorter list determines when to stop.
            copyoflist1.pop(list1_counter) #Removes elements from longer list as
            #they are appended to 'cardlist' so that only unused elements remain
            list2_counter = list2_counter + 1 #After each loop, the longer 
            #list counter is incremented by 1 so while loop stops before 
            #index is out of range
        return cardlist + copyoflist1 #Returns 'cardlist' with unused elements of
        #longer list appended to end

        
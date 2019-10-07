"""
This program performs various statistical analyses using lists of data.
"""
def arithmetic_mean(num_list):
        """
        This function takes a list of numbers and returns the mean,
        """
        if len(num_list) != 0:
            return (float(sum(num_list))) / (float(len(num_list)))
        else:
            return None

        
def variance(num_list):
    """
    This function calculates the variance of a list of numbers.
    """
    meanlist = []
    counter = 0
    while counter < len(num_list):
        meanlist.append(arithmetic_mean(num_list))
        counter = counter + 1
    zippedlist = zip(num_list,meanlist)
    newlist = []
    for (element1, element2) in zippedlist:
        newlist.append((element1 - element2)**2)
    return arithmetic_mean(newlist)      


def lower_median(num_list):
    """
    This function calculates the lower_median of a list of numbers.
    """
    numlist = list(num_list)
    if len(num_list) == 0:
        return None
    else:
        numlist.sort()
        if len(numlist) % 2 == 0:
            mid = (len(numlist) / 2) - 1
        else:
            mid = ((len(numlist) + 1) / 2) - 1
        return numlist[mid]


import random
def random_sample(data_list, sample_size):
    """
    This function takes n elements of the given list and creates
    a new list with the chosen elements.
    """
    data = list(data_list)
    newlist = []
    counter = 0 
    while counter < sample_size:
        num = random.choice(data)
        newlist.append(num)
        data.pop(data.index(num))
        counter = counter + 1
    return newlist
        

def hist_data(score_list):
    """
    This function takes a list of scores and determines how many 
    are in each of five equally sized ranges.
    """
    counter1 = 0
    counter2 = 0
    counter3 = 0
    counter4 = 0
    counter5 = 0
    for num in score_list:
        if num >= 0:
            if num < 20:
                counter1 = counter1 + 1
        if num >= 20:
            if num < 40:
                counter2 = counter2 + 1
        if num >= 40:
            if num < 60:
                counter3 = counter3 + 1
        if num >= 60:
            if num < 80:
                counter4 = counter4 + 1
        if num >= 80:
            if num < 100:
                counter5 = counter5 + 1
    histlist = [counter1, counter2, counter3, counter4, counter5]
    return histlist


import simpleplot
def plot_hist_data(score_list):
    """
    Shows a plot of the histogram data returned by hist_data().
    """
    simpleplot.plot_bars("Histogram", 400, 300,
                         "range", "count",
                         [zip([0, 20, 40, 60, 80],
                              hist_data(score_list))])
    

def sma(num_list, window_size):
    """
    This function calculates the simple moving average of a list of 
    numbers and a size n.
    """
    counter = 0
    newlist = []
    if window_size > len(num_list):
        window_size = len(num_list)
    while counter + window_size  < len(num_list) + 1:
        num = arithmetic_mean(num_list[counter : counter + window_size])
        newlist.append(num)
        counter = counter + 1
    return newlist


import math
def one_sample_t_test(num_list, sample_size):
    """
    This function computes a standard, one-sample t-test using given data.
    """
    sample = random_sample(num_list, sample_size)
    x_value = arithmetic_mean(sample)
    o_value = math.sqrt(variance(num_list))
    n_value = sample_size
    s_value = math.sqrt(variance(sample))
    z_value = x_value / (o_value / math.sqrt(n_value))
    t_value = z_value / s_value
    return t_value, sample
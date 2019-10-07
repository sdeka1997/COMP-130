"""
This assignment provides more detailed predator-prey modeling using the
studied Lotka-Volterra model. Increased detail is incorporated by the 
implementation of smaller intervals.
"""
def change_prey(birth, predation, prey, pred):
    """
    Returns the one-step change in prey population
    according to the Lotka-Volterra method.
    """
    return birth * prey - predation * prey * pred

def change_pred(growth, death, prey, pred):
    """
    Returns the one-step change in predator population
    according to the Lotka-Volterra method.
    """
    return growth * prey * pred - death * pred
 
#def pred_prey(birth, predation, growth, death, prey, pred, intervals):
#    """
#    Returns a list of (prey, pred) population pairs
#    for the given number of time intervals.
#    according to the Lotka-Volterra method.
#    """
#    pops = [(prey, pred)]
#    for i in range(intervals):
#        prey, pred = (prey + change_prey(birth, predation, prey, pred),
#                      pred + change_pred(growth, death, prey, pred))
#        pops.append((prey, pred))
#    return pops

import simpleplot

def pred_prey_intervals(birth, predation, growth, death, prey, pred, years, intervals):
    """
    This function gives the elapsed time and new prey/predator populations given the
    inputs of birth rate, predation rate, growth rate, death rate, initial populations,
    number of years, and size of interval.
    """
    starttime = 0.0
    population = [(starttime,prey,pred)]
    for index in range(years * intervals):
        newtime = population[0][0] + 1/float(intervals) * (index + 1)
        newprey = population[-1][1] + change_prey(float(birth)/intervals, float(predation)/intervals, population[-1][1], population[-1][2])
        newpred = population[-1][2] + change_pred(float(growth)/intervals, float(death)/intervals, population[-1][1], population[-1][2])
        population.append((newtime,newprey,newpred))
    return population

def plot_pred_prey(populations, pred_name, prey_name):
    """
    This function plots the prey populations (x-axis) vs. 
    the predator populations (y-axis).
    """
    newlist = []
    for item in populations:
        newlist.append((item[1],item[2]))
    simpleplot.plot_lines('Populations', 400, 400,
                          prey_name, pred_name,
                          [newlist])

def plot_time_populations(populations, pred_name, prey_name):
    """
    This function plots the predator and prey populations vs. 
    elapsed time.
    """
    pred_pops = [] 
    prey_pops = []
    for elapsedtime, preypop, predpop in populations:
        pred_pops.append((elapsedtime, predpop))
        prey_pops.append((elapsedtime, preypop))
    
    simpleplot.plot_lines('Populations', 400, 300,
                          'year', 'populations',
                          [pred_pops, prey_pops],
                           True,
                          [pred_name, prey_name])
    
def pred_prey_carrying(birth, predation, growth, death, carry_cap, prey, pred, years, intervals):
    """
    This function gives the elapsed time and new prey/predator populations given the
    inputs of birth rate, predation rate, growth rate, death rate, initial populations,
    number of years, and size of interval while also incorporating carrying capacity. 
    """
    starttime = 0.0
    population = [(starttime,prey,pred)]
    for index in range(years * intervals):
        newtime = population[0][0] + 1/float(intervals) * (index + 1)
        newprey = population[-1][1] + change_prey(float(birth)/intervals, float(predation)/intervals, population[-1][1], population[-1][2])
        newpred = population[-1][2] + change_pred(float(growth)/intervals, float(death)/intervals, population[-1][1], population[-1][2])
        if newprey > carry_cap:
            newprey = carry_cap
        population.append((newtime,newprey,newpred))
    return population
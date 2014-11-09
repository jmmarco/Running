# This module defines the different routines that can show up in a training plan
def tempo(distance):
    return ('Start with a warm up run for 15 to 20 minutes and then run:'+str(distance),'kilometers')
    
def interval(distance):
    return ('Start with a warm up run for 15 to 20 minutes and then run:'+str(distance),'kilometers')

def fartlek(distance):
    return ('Start with a warm up run for 15 to 20 minutes and then run:'+str(distance),'kilometers')

def stretch(minutes):
    return ('Just stretch for'+str(minutes),'minutes')

def progression(distance):
    return ('Start with a warm up run for 15 to 20 minutes and then run:'+str(distance),'kilometers')

def rest():
    return ('It\'s your day off! Enjoy and get some rest')

def resistance(minutes):
    return ('Start with a warm up run for 15 to 20 minutes and then run:'+str(minutes),'minutes')

def sprints(distance):
    return ('Start with a warm up run for 15 to 20 minutes followed by' distance/8'x'distance/6' meters sprints')

def cross_train(minutes)
    return ('Go for a bike ride or a swim for at least:'+str(minutes)'minutes')

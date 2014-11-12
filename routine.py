# This module defines the different routines that can show up in a custom training plan
def tempo(distance):
    return 'Tempo run: {} kilometers'.format(distance)

def interval(distance):
    return 'Interval run: {} kilometers'.format(distance)

def stretch(minutes):
    return 'Stretch for: {} minutes'.format(minutes)

def progression(distance):
    return 'Progression run: {} kilometers'.format(distance)

def rest():
    return ('Day off')

def sprints(amount):
    return '{} x 100 sprints'.format(amount)

def light_run(distance):
    return 'Light run: {} kilometers'.format(distance)

def run(distance):
    return 'Steady run: {} kilometers'.format(distance)

def cross_train(minutes):
    return 'Cross train: {} minutes'.format(minutes)

def hills(distance):
    return 'Climb hills: {} kilometers'.format(distance)

def speed(distance):
    return 'Speed work: {} kilometers'.format(distance)

def fartlek(distance):
    return 'Fartlek work: {} kilometers'.format(distance)

def race(distance):
    return 'Race pace: {} kilometers'.format(distance)

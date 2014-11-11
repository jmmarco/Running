# This module defines the different routines that can show up in a custom training plan
def tempo(distance):
    return 'Tempo run for: {} kilometers'.format(distance)

def interval(distance):
    return 'Distance run for: {} kilometers'.format(distance)

def stretch(minutes):
    return 'Stretch for: {} minutes'.format(minutes)

def progression(distance):
    return 'Progression run for: {} kilometers'.format(distance)

def rest():
    return ('Day off')

def resistance(minutes):
    return 'Run easy for: {} minutes'.format(minutes)

def sprints(amount):
    return 'Do {} x 80 sprints'.format(amount)

def race(distance):
    return 'Race day run for: {} kilometers!'.format(distance)

def light_run(distance):
    return 'Jog at an easy pace for: {} kilometers'.format(distance)

def run(distance):
    return 'Run for: {} kilometers'.format(distance)

def cross_train(minutes):
    return 'Run for: {} minutes'.format(minutes)

def hills(distance):
    return 'Climb hills for: {} kilometers'.format(distance)

def speed(distance):
    return 'Do speed work for: {} kilometers'.format(distance)

def fartlek(distance):
    return 'Try a Fartlek work for: {} kilometers'.format(distance)

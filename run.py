# import the required modules
import goal
import pprint
from routine import *

# Make a call to class Goal and assign the value
new_goal = goal.Goal()

# Get the distance and difficulty recorded by the user
selected_distance = new_goal.distance
selected_difficulty = new_goal.difficulty


# Based on the selected distance and difficulty choose the right plan
def final_plan():
    # Alternatives for a distance of 10K
    if selected_distance == '10' and selected_difficulty == 'Beginner':
        week_1 = [interval(1), rest(),rest(),cross_train(30 ),rest(),rest(),run(4)]
        week_2 = [rest(),interval(4),rest(),rest(),cross_train(45),rest(),run(5)]
        week_3 = [rest(),cross_train(30),rest(),rest(),sprints(6),rest(),run(5)]
        week_4 = [rest(),interval(4),rest(),cross_train(45),stretch(20),rest(),tempo(10)]   
        week_5 = [rest(),tempo(7),rest(),rest(),cross_train(45),rest(),run(8)]
        week_6 = [rest(),sprints(6),rest(),rest(),stretch(45),light_run(3),race(10)]
        plan = [week_1,week_2,week_3,week_4,week_5,week_6]

    elif selected_distance == '10' and selected_difficulty == 'Intermediate':
        week_1 = [interval(4),rest(),rest(),cross_train(30),rest(),rest(),run(4)]
        week_2 = [rest(),interval(4),rest(),rest(),cross_train(45),rest(),run(5)]
        week_3 = [rest(),cross_train(30),rest(),rest(),sprints(6),rest(),run(5)]
        week_4 = [rest(),interval(4),rest(),cross_train(45),stretch(10),rest(),run(10)]   
        week_5 = [rest(),tempo(7),rest(),rest(),cross_train(45),rest(),run(7)]
        week_6 = [rest(),sprints(6),rest(),rest(),cross_train(45),light_run(5),race(10)]
        plan = [week_1,week_2,week_3,week_4,week_5,week_6]
        
    elif selected_distance == '10' and selected_difficulty == 'Advanced':
        week_1 = [progression(1),rest(),rest(),run(2),cross_train(45),rest(),tempo(6)]
        week_2 = [rest(),progression(2),rest(),cross_train(45),sprints(6),rest(),tempo(8)]
        week_3 = [rest(),progression(3),rest(),cross_train(45),tempo(6),rest(),progression(10)]
        week_4 = [rest(),tempo(6),rest(),cross_train(45),run(6),rest(),tempo(12)]   
        week_5 = [rest(),tempo(5),rest(),cross_train(45),tempo(12),rest(),run(7)]
        week_6 = [rest(),tempo(7),rest(),stretch(45),light_run(4),rest(),race(10)]
        plan = [week_1,week_2,week_3,week_4,week_5,week_6]

    # Alternatives for a distance of 21K
    elif selected_distance == '21' and selected_difficulty == 'Beginner':
        week_1 = [rest(),cross_train(45),speed(4),rest(),interval(6),rest(),tempo(10)]
        week_2 = [rest(),speed(4),cross_train(45),rest(),stretch(20),rest(),tempo(12)]
        week_3 = [rest(),cross_train(30),fartlek(6),hills(3),run(5),rest(),interval(13)]
        week_4 = [rest(),speed(4),cross_train(45),interval(5),run(2),rest(),race(10)]   
        week_5 = [rest(),interval(6),run(2),interval(4),fartlek(6),rest(),tempo(15)]
        week_6 = [rest(),hills(2),speed(6),cross_train(45),sprints(4),rest(),race(10)]
        week_7 = [rest(),fartlek(6),stretch(45),race(6),hills(3),rest(),tempo(18)] 
        week_8 = [rest(),fartlek(3),rest(),speed(5),hills(6),rest(),race(12)]
        week_9 = [rest(),tempo(3),speed(2),tempo(3),race(2),rest(),race(10)]
        week_10 = [rest(),fartlek(6),rest(),interval(1),stretch(45),rest(),race(10)]
        week_11 = [rest(),speed(4),run(3),interval(5),stretch(45),rest(),tempo(18)]
        week_12 = [rest(),sprints(5),run(3),rest(),hills(2),rest(),race(8)]
        week_13 = [rest(),sprints(5),interval(6),cross_train(45),fartlek(8),rest(),race(10)]
        week_14 = [rest(),speed(5),sprints(5),cross_train(45),fartlek(8),rest(),race(10)]
        week_15 = [rest(),rest(),rest(),interval(2),stretch(30),rest(),race(21)]
        plan = [week_1,week_2,week_3,week_4,week_5,week_6,week_7,week_8,week_9,week_10,week_11,week_12,week_13,week_14,week_15]
        
    elif selected_distance == '21' and selected_difficulty == 'Intermediate':
        week_1 = [rest(),cross_train(45),speed(4),rest(),interval(6),rest(),tempo(10)]
        week_2 = [rest(),speed(4),cross_train(45),rest(),stretch(20),rest(),tempo(12)]
        week_3 = [rest(),cross_train(30),fartlek(6),hills(3),run(5),rest(),interval(13)]
        week_4 = [rest(),speed(4),cross_train(45),interval(5),run(2),rest(),race(10)]   
        week_5 = [rest(),interval(6),run(2),interval(4),fartlek(6),rest(),tempo(15)]
        week_6 = [rest(),hills(2),speed(6),cross_train(45),sprints(4),rest(),race(10)]
        week_7 = [rest(),fartlek(6),stretch(45),race(6),hills(3),rest(),tempo(18)] 
        week_8 = [rest(),fartlek(3),rest(),speed(5),hills(6),rest(),race(12)]
        week_9 = [rest(),tempo(3),speed(2),tempo(3),race(2),rest(),race(10)]
        week_10 = [rest(),fartlek(6),rest(),interval(1),stretch(45),rest(),race(10)]
        week_11 = [rest(),speed(4),run(3),interval(5),stretch(45),rest(),tempo(18)]
        week_12 = [rest(),sprint(5),run(3),rest(),hills(2),rest(),race(8)]
        week_13 = [rest(),sprints(5),interval(6),cross_train(45),fartlek(8),rest(),race(10)]
        week_14 = [rest(),speed(5),sprints(5),cross_train(45),farlek(8),rest(),race(10)]
        week_15 = [rest(),rest(),rest(),interval(2),stretch(30),rest(),race(21)]
        plan = [week_1,week_2,week_3,week_4,week_5,week_6,week_7,week_8,week_9,week_10,week_11,week_12,week_13,week_14,week_15]

    elif selected_distance == '21' and selected_difficulty == 'Advanced':
        week_1 = [light_run(5),cross_train(45),speed(6),rest(),sprints(6),rest(),tempo(18)]
        week_2 = [rest(),interval(10),speed(7),cross_train(45),sprints(6),rest(),tempo(22)]
        week_3 = [rest(),cross_train(45),tempo(15),hills(4),tempo(5),rest(),tempo(30)]
        week_4 = [rest(),speed(7),light_run(6),progression(12),light_run(5),rest(),tempo(21)]   
        week_5 = [rest(),interval(10),tempo(2),speed(10),progression(11),rest(),tempo(32)]
        week_6 = [rest(),hills(2),progression(18),cross_train(30),sprints(10),rest(),race(25)]
        week_7 = [rest(),light_run(18),tempo(7),race(10),progression(11),rest(),tempo(30)] 
        week_8 = [rest(),fartlek(3),rest(),speed(5),hills(6),rest(),race(12)]
        week_9 = [rest(),tempo(3),speed(2),tempo(3),race(2),rest(),race(10)]
        week_10 = [rest(),fartlek(6),rest(),interval(1),stretch(45),rest(),race(10)]
        week_11 = [rest(),speed(4),run(3),interval(5),stretch(45),rest(),tempo(18)]
        week_12 = [rest(),sprint(5),run(3),rest(),hills(2),rest(),race(8)]
        week_13 = [rest(),sprints(5),interval(6),cross_train(45),fartlek(8),rest(),race(10)]
        week_14 = [rest(),speed(5),sprints(5),cross_train(45),farlek(8),rest(),race(10)]
        week_15 = [rest(),rest(),rest(),interval(2),stretch(30),rest(),race(21)]
        plan = [week_1,week_2,week_3,week_4,week_5,week_6,week_7,week_8,week_9,week_10,week_11,week_12,week_13,week_14,week_15]

    # Alternatives for a distance of 42K
    elif selected_distance == '42' and selected_difficulty == 'Beginner':
        week_1 = [light_run(5),cross_train(45),run(3),rest(),sprints(5),rest(),tempo(12)]
        week_2 = [rest(),interval(7),speed(3),rest(),run(3),rest(),tempo(16)]
        week_3 = [rest(),cross_train(45),run(7),run(3),run(5),rest(),tempo(17)]
        week_4 = [rest(),run(5),rest(),run(6),light_run(2),rest(),tempo(21)]   
        week_5 = [rest(),hills(2.5),cross_train(45),rest(),run(6),rest(),tempo(19)]
        week_6 = [rest(),interval(6),cross_train(45),run(4),cross_train(30),rest(),tempo(22)]
        week_7 = [rest(),progression(7),cross_train(30),race(5),sprints(5),rest(),tempo(22)] 
        week_8 = [rest(),interval(4),speed(4),race(4),interval(4),rest(),tempo(24)]
        week_9 = [rest(),progression(6),rest(),tempo(4),stretch(10),rest(),tempo(10)]
        week_10 = [rest(),cross_train(45),progression(9),hills(3),run(3),rest(),tempo(17)]
        week_11 = [rest(),interval(3),speed(3),race(3),interval(3),rest(),tempo(28)]
        week_12 = [rest(),tempo(7),rest(),tempo(4),stretch(10),rest(),tempo(10)]
        week_13 = [rest(),light_run(5),progression(6),rest(),run(2),rest(),tempo(30)]
        week_14 = [rest(),speed(5),hills(4.5),cross_train(45),light_run(3),rest(),tempo(10)]
        week_15 = [run(5),stretch(15),rest(),stretch(30),rest(),light_run(5),race(42.2)]
        plan = [week_1,week_2,week_3,week_4,week_5,week_6,week_7,week_8,week_9,week_10,week_11,week_12,week_13,week_14,week_15]
        return plan

    elif selected_distance == '42' and selected_difficulty == 'Intermediate':
        week_1 = [light_run(5),cross_train(45),speed(6),rest(),sprints(6),rest(),tempo(18)]
        week_2 = [rest(),interval(10),tempo(7),cross_train(45),progression(11),rest(),tempo(22)]
        week_3 = [rest(),cross_train(45),tempo(15),hills(4),light_run(5),rest(),tempo(30)]
        week_4 = [rest(),speed(9),light_run(6),progression(12),light_run(5),rest(),tempo(25)]   
        week_5 = [rest(),interval(8),light_run(3),speed(10),progression(11),rest(),tempo(13)]
        week_6 = [rest(),light_run(15),progression(18),cross_train(45),sprints(5),rest(),tempo(20)]
        week_7 = [rest(),progression(11),light_run(7),race(16),progression(11),rest(),tempo(30)] 
        week_8 = [rest(),interval(8),light_run(3),speed(10),progression(11),rest(),race(30)]
        week_9 = [rest(),tempo(10),speed(10),tempo(10),race(10),rest(),tempo(40)]
        week_10 = [rest(),light_run(6),rest(),hills(1),interval(12),rest(),race(21)]
        week_11 = [rest(),progression(6),cross_train(45),interval(20),cross_train(30),rest(),tempo(35)]
        week_12 = [rest(),speed(9),interval(10),speed(9),light_run(10),rest(),tempo(40)]
        week_13 = [rest(),interval(8),light_run(3),speed(10),progression(8),rest(),race(30)]
        week_14 = [rest(),speed(5),rest(),cross_train(45),interval(8),rest(),tempo(10)]
        week_15 = [tempo(5),stretch(15),rest(),rest(),stretch(30),light_run(5),race(42.2)]
        plan = [week_1,week_2,week_3,week_4,week_5,week_6,week_7,week_8,week_9,week_10,week_11,week_12,week_13,week_14,week_15]

    elif selected_distance == '42' and selected_difficulty == 'Advanced':
        week_1 = [light_run(5),cross_train(45),speed(6),rest(),sprints(6),rest(),tempo(18)]
        week_2 = [rest(),interval(10),speed(7),cross_train(45),sprints(6),rest(),tempo(22)]
        week_3 = [rest(),cross_train(45),tempo(15),hills(4),tempo(5),rest(),tempo(30)]
        week_4 = [rest(),speed(7),light_run(6),progression(12),tempo(5),rest(),tempo(21)]   
        week_5 = [rest(),interval(10),tempo(2),speed(10),progression(11),rest(),tempo(32)]
        week_6 = [rest(),hills(2),progression(18),cross_train(30),interval(10),rest(),run(25)]
        week_7 = [rest(),light_run(18),tempo(7),race(10),progression(11),rest(),tempo(30)] 
        week_8 = [rest(),tempo(10),rest(),speed(10),progression(10),rest(),race(25)]
        week_9 = [rest(),tempo(10),speed(10),tempo(10),race(10),rest(),interval(40)]
        week_10 = [rest(),light_run(8),rest(),hills(1),interval(10),rest(),race(21)]
        week_11 = [rest(),speed(10),cross_train(45),interval(20),light_run(6),rest(),tempo(41)]
        week_12 = [rest(),sprints(5),speed(5),rest(),hills(3),rest(),race(20)]
        week_13 = [rest(),interval(10),light_run(),tempo(3),rest(),rest(),tempo(25)]
        week_14 = [rest(),speed(5),sprints(2),cross_train(30),interval(8),rest(),race(10)]
        week_15 = [tempo(10),cross_train(15),rest(),stretch(30),rest(),light_run(5),race(42.2)]
        plan = [week_1,week_2,week_3,week_4,week_5,week_6,week_7,week_8,week_9,week_10,week_11,week_12,week_13,week_14,week_15] 
    return plan
        
plan = final_plan()

# Make some space
print '\n'
print 'Here\'s the outlined weeks for your selection:\n'
# Use Data pretty printer to nicely print the contents of each week of the plan
for index in range(len(plan)):
    print "Week " + str(index + 1) + ":", plan[index]
    pp = pprint.PrettyPrinter(indent=1, width=80, depth=None)

# Make some space
print "\n"*2

# Options before user goes
def option_menu():
    # Create a list with the available options and print the menu
    options = ['1','2','3','4']
    print 'We are done generating your running plan.'
    print 'Below is guide with details on a specific routine'
    print '1.  Fartlek'
    print '2.  Tempo'
    print '3.  Interval'
    print '4.  Cross Train'
    print '5.  Progression'
    print '6.  Sprints'
    print '7.  Race'
    print '8.  Light Run'
    print '9.  Hill Training'
    print '10. Speed Work'
    print '11. Stretch Session'
    print '12. Steady Run'
    print '0.  Exit'
    

    selection = raw_input('Please select an option: ')
    if selection == '1':
        print '\n'
        print 'You play with speed by running at faster efforts for short periods of time (e.g., to that tree, to the sign) followed by easy-effort running to recover.\n'
    elif selection == '2':
        print '\n'
        print 'This is the effort level just outside your comfort zone, you can hear your breathing, but you\'re not gasping for air.\n'
    elif selection == '3':
        print '\n'
        print 'Are short, intense efforts followed by equal or slightly longer recovery time.\n'
    elif selection == '4':
        print '\n'
        print 'Combination exercises of other disciplines, different than running (e.g., cycling, walking, swimming)\n'
    elif selection == '5':
        print '\n'
        print 'Start at a comfortable speed, gradually accelerate, and end at race pace \n'
    elif selection == '6':
        print '\n'
        print 'Is running a short distance at (or near) top speed for short lengths.\n'          
    elif selection == '7':
        print '\n'
        print 'Run at your set race pace\n'
    elif selection == '8':
        print '\n'
        print 'Run at an easy comfortable pace\n'
    elif selection == '9':
        print '\n'
        print 'Find a hill or bridge where it takes you at least one minute to run.\n'
    elif selection == '10':
        print '\n'
        print 'Is a a fast paced run\n'
    elif selection == '11':
        print '\n'
        print 'Before stretching, always jog at least 10 minutes to warm up the muscles. Never stretch "cold" muscles. Also, you should always take time to stretch after a run.\n'
    elif selection == '12':
        print '\n'
        print 'Run at a fixed and steady pace\n'
    elif selection =='0':
        print'Good Bye!'
    else:
        print 'Invalid option please try again'
        option_menu()

# Call and run option_menu
option_menu()

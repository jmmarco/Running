# import the required modules
import goal
import pprint
from routine import *

#new_goal = goal.Goal()

# Get the distance and difficulty recorded by the user
selected_distance = new_goal.distance
selected_difficulty = new_goal.difficulty


# Based on the selected distance and difficulty choose the right plan
def final_plan():
    # Alternatives for a distance of 10K
    if selected_distance == '10' and selected_difficulty == 'Beginner':
        week_1 = [interval(1), rest(),rest(),resistance(4),rest(),rest(),run(4)]
        week_2 = [rest(),interval(4),rest(),rest(),resistance(45),rest(),run(5)]
        week_3 = [rest(),resistance(30),rest(),rest(),sprints(6),rest(),run(5)]
        week_4 = [rest(),interval(4),rest(),resistance(45),stretch(20),rest(),tempo(10)]   
        week_5 = [rest(),tempo(7),rest(),rest(),cross_train(45),rest(),run(8)]
        week_6 = [rest(),sprints(6),rest(),rest(),stretch(45),light_run(3),race(10)]
        plan = [week_1,week_2,week_3,week_4,week_5,week_6]

    elif selected_distance == '10' and selected_difficulty == 'Intermediate':
        week_1 = [interval(4),rest(),rest(),resistance(30),rest(),rest(),run(4)]
        week_2 = [rest(),interval(4),rest(),rest(),resistance(45),rest(),run(5)]
        week_3 = [rest(),resistance(30),rest(),rest(),sprints(6),rest(),run(5)]
        week_4 = [rest(),interval(4),rest(),resistance(45),stretch(10),rest(),run(10)]   
        week_5 = [rest(),tempo(7),rest(),rest(),cross_train(45),rest(),run(7)]
        week_6 = [rest(),sprints(6),rest(),rest(),resistance(45),light_run(5),race(10)]
        plan = [week_1,week_2,week_3,week_4,week_5,week_6]
        
    elif selected_distance == '10' and selected_difficulty == 'Advanced':
        week_1 = [progression(1),rest(),rest(),run(2),resistance(45),rest(),tempo(6)]
        week_2 = [rest(),progression(2),rest(),resistance(45),sprints(6),rest(),tempo(8)]
        week_3 = [rest(),progression(3),rest(),resistance(45),tempo(6),rest(),progression(10)]
        week_4 = [rest(),tempo(6),rest(),resistance(45),run(6),rest(),tempo(12)]   
        week_5 = [rest(),tempo(5),rest(),cross_train(45),tempo(12),rest(),run(7)]
        week_6 = [rest(), tempo(7),rest(),tempo(4),stretch(10),rest(),tempo(10)]
        plan = [week_1,week_2,week_3,week_4,week_5,week_6]

    # Alternatives for a distance of 21K

    elif selected_distance == '21' and selected_difficulty == 'Beginner':
        week_1 = [rest(), tempo(7),rest(),tempo(4),stretch(10),rest(),tempo(10)]
        week_2 = [rest(), tempo(7),rest(),tempo(4),stretch(10),rest(),tempo(10)]
        week_3 = [rest(), tempo(7),rest(),tempo(4),stretch(10),rest(),tempo(10)]
        week_4 = [rest(), tempo(7),rest(),tempo(4),stretch(10),rest(),tempo(10)]   
        week_5 = [rest(), tempo(7),rest(),tempo(4),stretch(10),rest(),tempo(10)]
        week_6 = [rest(), tempo(7),rest(),tempo(4),stretch(10),rest(),tempo(10)]
        plan = [week_1,week_2,week_3,week_4,week_5,week_6]
        
    elif selected_distance == '21' and selected_difficulty == 'Intermediate':
        week_1 = [rest(), tempo(7),rest(),tempo(4),stretch(10),rest(),tempo(10)]
        week_2 = [rest(), tempo(7),rest(),tempo(4),stretch(10),rest(),tempo(10)]
        week_3 = [rest(), tempo(7),rest(),tempo(4),stretch(10),rest(),tempo(10)]
        week_4 = [rest(), tempo(7),rest(),tempo(4),stretch(10),rest(),tempo(10)]   
        week_5 = [rest(), tempo(7),rest(),tempo(4),stretch(10),rest(),tempo(10)]
        week_6 = [rest(), tempo(7),rest(),tempo(4),stretch(10),rest(),tempo(10)]
        plan = [week_1,week_2,week_3,week_4,week_5,week_6]

    elif selected_distance == '21' and selected_difficulty == 'Advanced':
        week_1 = [rest(), tempo(7),rest(),tempo(4),stretch(10),rest(),tempo(10)]
        week_2 = [rest(), tempo(7),rest(),tempo(4),stretch(10),rest(),tempo(10)]
        week_3 = [rest(), tempo(7),rest(),tempo(4),stretch(10),rest(),tempo(10)]
        week_4 = [rest(), tempo(7),rest(),tempo(4),stretch(10),rest(),tempo(10)]   
        week_5 = [rest(), tempo(7),rest(),tempo(4),stretch(10),rest(),tempo(10)]
        week_6 = [rest(), tempo(7),rest(),tempo(4),stretch(10),rest(),tempo(10)]
        plan = [week_1,week_2,week_3,week_4,week_5,week_6]

    # Alternatives for a distance of 42K

    elif selected_distance == '42' and selected_difficulty == 'Beginner':
        week_1 = [rest(), tempo(7),rest(),tempo(4),stretch(10),rest(),tempo(10)]
        week_2 = [rest(), tempo(7),rest(),tempo(4),stretch(10),rest(),tempo(10)]
        week_3 = [rest(), tempo(7),rest(),tempo(4),stretch(10),rest(),tempo(10)]
        week_4 = [rest(), tempo(7),rest(),tempo(4),stretch(10),rest(),tempo(10)]   
        week_5 = [rest(), tempo(7),rest(),tempo(4),stretch(10),rest(),tempo(10)]
        week_6 = [rest(), tempo(7),rest(),tempo(4),stretch(10),rest(),tempo(10)]
        plan = [week_1,week_2,week_3,week_4,week_5,week_6]
        return plan

    elif selected_distance == '42' and selected_difficulty == 'Intermediate':
        week_1 = [rest(), tempo(7),rest(),tempo(4),stretch(10),rest(),tempo(10)]
        week_2 = [rest(), tempo(7),rest(),tempo(4),stretch(10),rest(),tempo(10)]
        week_3 = [rest(), tempo(7),rest(),tempo(4),stretch(10),rest(),tempo(10)]
        week_4 = [rest(), tempo(7),rest(),tempo(4),stretch(10),rest(),tempo(10)]   
        week_5 = [rest(), tempo(7),rest(),tempo(4),stretch(10),rest(),tempo(10)]
        week_6 = [rest(), tempo(7),rest(),tempo(4),stretch(10),rest(),tempo(10)]
        plan = [week_1,week_2,week_3,week_4,week_5,week_6]

    elif selected_distance == '42' and selected_difficulty == 'Advanced':
        week_1 = [rest(), tempo(7),rest(),tempo(4),stretch(10),rest(),tempo(10)]
        week_2 = [rest(), tempo(7),rest(),tempo(4),stretch(10),rest(),tempo(10)]
        week_3 = [rest(), tempo(7),rest(),tempo(4),stretch(10),rest(),tempo(10)]
        week_4 = [rest(), tempo(7),rest(),tempo(4),stretch(10),rest(),tempo(10)]   
        week_5 = [rest(), tempo(7),rest(),tempo(4),stretch(10),rest(),tempo(10)]
        week_6 = [rest(), tempo(7),rest(),tempo(4),stretch(10),rest(),tempo(10)]
        plan = [week_1,week_2,week_3,week_4,week_5,week_6]

    return plan
        

plan = final_plan()

# Use Data pretty printer to nicely print the contents of each week of the plan
for index in range(len(plan)):
    print "Week " + str(index + 1) + ":", plan[index]
    pp = pprint.PrettyPrinter(indent=1, width=80, depth=None)
    #pp.pprint(['Current week: ', plan[index]])

print "\n"*5
#VALID_SELECTION = ['1. Fartlek Workouts','2. Tempo Workouts','3. Interval Workouts','4. ']
#print VALID_SELECTION
#selection = raw_input('Please select an option')
#if selection == '1':
#    print 'You play with speed by running at faster efforts for short periods of time (to that tree, to the sign) followed by easy-effort running to recover.'

#elif selection == '2':
#    print 'Means to run at an effort at or slightly above your anaerobic threshold and then cooldown.'

#elif selection == '3':
#    print 'Are short, intense efforts followed by equal or slightly longer recovery time.'
#
#
#print 'Remeber, all workouts should include a 15 to 20 minute warmup jog.'
#print 'At the end of each workout do not forget to stretch for at least 10 minutes'
print 'good bye!'




    

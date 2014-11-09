import goal
import pprint
from routine import *

new_goal = goal.Goal()

selected_distance = new_goal.distance
selected_difficulty = new_goal.difficulty


def final_plan():
    # Alternatives for a distance of 10K
    if selected_distance == '10' and selected_difficulty == 'Beginner':
        week_1 = [interval(1), rest(), rest(), resistance(30),rest(),rest(),progression(4)]
        week_2 = [stretch(10), interval(4),rest(),rest(),resistance(45),rest(),progression(5)]
        week_3 = [rest(), resistance(30),rest(),rest(),sprints(0.48),rest(),progression(5)]
        week_4 = [rest(), interval(4),rest(),resistance(45),stretch(10),rest(),tempo(10)]   
        week_5 = [rest(), tempo(7),rest(),rest(),crosstrain(45),rest(),tempo(10)]
        week_6 = [rest(), tempo(7),rest(),resistance(45),stretch(10),rest(),tempo(10)]
        plan = [week_1,week_2,week_3,week_4,week_5,week_6]

    elif selected_distance == '10' and selected_difficulty == 'Intermediate':
        week_1 = [rest(), tempo(7),rest(),resistance(45),stretch(10),rest(),tempo(10)]
        week_2 = [rest(), tempo(7),rest(),resistance(45),stretch(10),rest(),tempo(10)]
        week_3 = [rest(), tempo(7),rest(),resistance(45),stretch(10),rest(),tempo(10)]
        week_4 = [rest(), tempo(7),rest(),resistance(45),stretch(10),rest(),tempo(10)]   
        week_5 = [rest(), tempo(7),rest(),resistance(45),stretch(10),rest(),tempo(10)]
        week_6 = [rest(), tempo(7),rest(),resistance(45),stretch(10),rest(),tempo(10)]
        plan = [[week_1],[week_2],[week_3],[week_4],[week_5],[week_6]]
        
    elif selected_distance == '10' and selected_difficulty == 'Advance':
        week_1 = [rest(), tempo(7),rest(),resistance(45),stretch(10),rest(),tempo(10)]
        week_2 = [rest(), tempo(7),rest(),resistance(45),stretch(10),rest(),tempo(10)]
        week_3 = [rest(), tempo(7),rest(),resistance(45),stretch(10),rest(),tempo(10)]
        week_4 = [rest(), tempo(7),rest(),resistance(45),stretch(10),rest(),tempo(10)]   
        week_5 = [rest(), tempo(7),rest(),resistance(45),stretch(10),rest(),tempo(10)]
        week_6 = [rest(), tempo(7),rest(),resistance(45),stretch(10),rest(),tempo(10)]
        plan = [[week_1],[week_2],[week_3],[week_4],[week_5],[week_6]]

    # Alternatives for a distance of 21K

    elif selected_distance == '21' and selected_difficulty == 'Beginner':
        week_1 = [rest(), tempo(7),rest(),resistance(45),stretch(),rest(),tempo(10)]
        week_2 = [rest(), tempo(7),rest(),resistance(45),stretch(),rest(),tempo(10)]
        week_3 = [rest(), tempo(7),rest(),resistance(45),stretch(),rest(),tempo(10)]
        week_4 = [rest(), tempo(7),rest(),resistance(45),stretch(),rest(),tempo(10)]   
        week_5 = [rest(), tempo(7),rest(),resistance(45),stretch(),rest(),tempo(10)]
        week_6 = [rest(), tempo(7),rest(),resistance(45),stretch(),rest(),tempo(10)]
        plan = [[week_1],[week_2],[week_3],[week_4],[week_5],[week_6]]

    elif selected_distance == '21' and selected_difficulty == 'Intermediate':
        week_1 = [rest(), tempo(7),rest(),resistance(45),stretch(10),rest(),tempo(10)]
        week_2 = [rest(), tempo(7),rest(),resistance(45),stretch(10),rest(),tempo(10)]
        week_3 = [rest(), tempo(7),rest(),resistance(45),stretch(10),rest(),tempo(10)]
        week_4 = [rest(), tempo(7),rest(),resistance(45),stretch(10),rest(),tempo(10)]   
        week_5 = [rest(), tempo(7),rest(),resistance(45),stretch(10),rest(),tempo(10)]
        week_6 = [rest(), tempo(7),rest(),resistance(45),stretch(10),rest(),tempo(10)]
        plan = [[week_1],[week_2],[week_3],[week_4],[week_5],[week_6]]

    elif selected_distance == '21' and selected_difficulty == 'Advance':
        week_1 = [rest(), tempo(7),rest(),resistance(45),stretch(10),rest(),tempo(10)]
        week_2 = [rest(), tempo(7),rest(),resistance(45),stretch(10),rest(),tempo(10)]
        week_3 = [rest(), tempo(7),rest(),resistance(45),stretch(10),rest(),tempo(10)]
        week_4 = [rest(), tempo(7),rest(),resistance(45),stretch(10),rest(),tempo(10)]   
        week_5 = [rest(), tempo(7),rest(),resistance(45),stretch(10),rest(),tempo(10)]
        week_6 = [rest(), tempo(7),rest(),resistance(45),stretch(10),rest(),tempo(10)]
        plan = [[week_1],[week_2],[week_3],[week_4],[week_5],[week_6]]

    # Alternatives for a distance of 42K

    elif selected_distance == '42' and selected_difficulty == 'Beginner':
        week_1 = [rest(), tempo(7),rest(),resistance(45),stretch(),rest(),tempo(10)]
        week_2 = [rest(), tempo(7),rest(),resistance(45),stretch(),rest(),tempo(10)]
        week_3 = [rest(), tempo(7),rest(),resistance(45),stretch(),rest(),tempo(10)]
        week_4 = [rest(), tempo(7),rest(),resistance(45),stretch(),rest(),tempo(10)]   
        week_5 = [rest(), tempo(7),rest(),resistance(45),stretch(),rest(),tempo(10)]
        week_6 = [rest(), tempo(7),rest(),resistance(45),stretch(),rest(),tempo(10)]
        plan = [[week_1],[week_2],[week_3],[week_4],[week_5],[week_6]]
        return plan

    elif selected_distance == '42' and selected_difficulty == 'Intermediate':
        week_1 = [rest(), tempo(7),rest(),resistance(45),stretch(10),rest(),tempo(10)]
        week_2 = [rest(), tempo(7),rest(),resistance(45),stretch(10),rest(),tempo(10)]
        week_3 = [rest(), tempo(7),rest(),resistance(45),stretch(10),rest(),tempo(10)]
        week_4 = [rest(), tempo(7),rest(),resistance(45),stretch(10),rest(),tempo(10)]   
        week_5 = [rest(), tempo(7),rest(),resistance(45),stretch(10),rest(),tempo(10)]
        week_6 = [rest(), tempo(7),rest(),resistance(45),stretch(10),rest(),tempo(10)]
        plan = [[week_1],[week_2],[week_3],[week_4],[week_5],[week_6]]

    elif selected_distance == '42' and selected_difficulty == 'Advance':
        week_1 = [rest(), tempo(7),rest(),resistance(45),stretch(10),rest(),tempo(10)]
        week_2 = [rest(), tempo(7),rest(),resistance(45),stretch(10),rest(),tempo(10)]
        week_3 = [rest(), tempo(7),rest(),resistance(45),stretch(10),rest(),tempo(10)]
        week_4 = [rest(), tempo(7),rest(),resistance(45),stretch(10),rest(),tempo(10)]   
        week_5 = [rest(), tempo(7),rest(),resistance(45),stretch(10),rest(),tempo(10)]
        week_6 = [rest(), tempo(7),rest(),resistance(45),stretch(10),rest(),tempo(10)]
        plan = [[week_1],[week_2],[week_3],[week_4],[week_5],[week_6]]

    return plan
        

plan = final_plan()

#pp = pprint.PrettyPrinter(depth=6)
#pp.pprint('Your first week looks like this'+plan.append([week_1]))
# Try to print nicely

#for plan in plan:
#    print 'This is your plan:', plan

for index in range(len(plan)):
    print "Week " + str(index + 1) + ":", plan[index]
    pp = pprint.PrettyPrinter(depth=6)
    pp.pprint(['Current week: ', plan[index]])

print 'good bye!'




    

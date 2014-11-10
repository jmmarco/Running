class Goal():
    """This class creates and initialize the distance and difficulty variables"""
 

    VALID_DISTANCES = ['10','21','42']
    VALID_DIFFICULTY = ['Beginner','Intermediate','Advanced']
    print 'Welcome to the training plan generator!'
    print 'Valid distances are: ',VALID_DISTANCES[0],',',VALID_DISTANCES[1],',','and',VALID_DISTANCES[2],'K'
    print 'Valid diffculty levels are: ',VALID_DIFFICULTY[0],',',VALID_DIFFICULTY[1],'and',VALID_DIFFICULTY[2]
 
    def __init__(self):
#        self.name = None
#        self.date = None
#        self.reward = None
        self.distance = None
        self.difficulty = None
        self.query_for_parameters();
 
 
 
    def query_for_parameters(self):
#        self.name = raw_input('Goal Name: ')
#        self.date = goal_date = raw_input('Goal date: ')
#        self.reward = raw_input('Reward: ')
        while True:
            distance_input = raw_input('Please enter a Distance: ')
            if distance_input in self.VALID_DISTANCES:
                self.distance = distance_input
                break
            print("Not a valid distance, try again")
        while True:
            difficulty_input = raw_input('Difficulty: ')
            if difficulty_input in self.VALID_DIFFICULTY:
                self.difficulty = difficulty_input
                break
            print("Not a valid difficulty, try again")
            
        
 
 
    def __str__(self):
        return "Distance {0} Difficulty {1}".format(self.distance, self.difficulty)
 
        
        
def main():
    new_goal = Goal()
    print new_goal
 
 
if __name__=='__main__':
    main()

class Goal():
    """This class creates and initialize the distance and difficulty variables"""
 
# Define and create the global variables and welcome the user
    VALID_DISTANCES = ['10','21','42']
    VALID_DIFFICULTY = ['Beginner','Intermediate','Advanced']
    print 'Welcome to the training plan generator!'
    print 'Valid distances are: ',VALID_DISTANCES[0],',',VALID_DISTANCES[1],',','and',VALID_DISTANCES[2],'K'
    print 'Valid diffculty levels are: ',VALID_DIFFICULTY[0],',',VALID_DIFFICULTY[1],'and',VALID_DIFFICULTY[2]

# Create and initialize the class variables  
    def __init__(self):
        self.distance = None
        self.difficulty = None
        self.query_for_parameters();
 
 
# Query user for parameters 
    def query_for_parameters(self):
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
            
        
# Return and display distance and difficulty 
    def __str__(self):
        return "Distance {0} Difficulty {1}".format(self.distance, self.difficulty)
 
        

# Define main function        
def main():
    new_goal = Goal()
    print new_goal
 
# Check to see if this file is executed separately 
if __name__=='__main__':
    main()

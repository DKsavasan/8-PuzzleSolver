# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        start = 0
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[0])):
                self.tiles[row][col] = digitstr[start]
                if self.tiles[row][col] == '0':
                    self.blank_r = row
                    self.blank_c = col
                start += 1


    ### Add your other method definitions below. ###
    def __repr__(self):
        """returns a string representation of a Board object"""
        
        s = ''
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[0])):
                if self.tiles[i][j] == '0': 
                    s+= '_' + ' '
                else:
                    s += str(self.tiles[i][j]) + ' '
            s += '\n'
        
        return s
    
    def move_blank(self, direction):
        """takes as input a string direction that 
        specifies the direction in which the blank should move"""
        
        if direction == 'up':
            if self.blank_r != 0:
                temp = '0'
                self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r - 1][self.blank_c]
                self.tiles[self.blank_r - 1][self.blank_c] = temp
                self.blank_r -= 1
                return True
            else:
                return False
            
        elif direction == 'down':
            if self.blank_r != 2:
                temp = '0'
                self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r + 1][self.blank_c]
                self.tiles[self.blank_r + 1][self.blank_c] = temp
                self.blank_r += 1
                return True
            else:
                return False
            
        elif direction == 'left':
            if self.blank_c != 0:
                temp = '0'
                self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r][self.blank_c - 1]
                self.tiles[self.blank_r][self.blank_c - 1] = temp
                self.blank_c -= 1
                return True
            else:
                return False
        
        elif direction == 'right':
            if self.blank_c != 2:
                temp = '0'
                self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r][self.blank_c + 1]
                self.tiles[self.blank_r][self.blank_c + 1] = temp
                self.blank_c += 1
                return True
            else:
                return False
        else:
            return False
        
        
    def digit_string(self):
        """returns a string of digits that corresponds to 
        the current contents of the called Board object’s tiles attribute"""
        
        current = ''
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[0])):
                current += self.tiles[i][j]    
        return current
    
    
    def copy(self):
        """returns a newly-constructed Board object that 
        is a deep copy of the called object"""
        
        string = self.digit_string()
        return Board(string)
    
    
    def num_misplaced(self):
        """returns the number of tiles in the called Board 
        object that are not where they should be in the goal state"""
        
        count = 0
        for i in range(len(GOAL_TILES)):
            for j in range(len(GOAL_TILES[0])):
                if GOAL_TILES[i][j] != self.tiles[i][j]:
                        count += 1
        return count - 1
    
    def distance_from_goal(self):
        """H2 heuristic function's helper method"""
        GOAL_DICT = {'0': [0,0], '1': [0,1], '2': [0,2], 
                     '3': [1,0], '4': [1,1], '5': [1,2], 
                     '6': [2,0], '7': [2,1], '8': [2,2]}
        total = 0

        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if self.tiles[r][c] == GOAL_TILES[r][c]:
                    total += 0
                else:
                    if self.tiles[r][c] == '0':
                        total += 0
                    else:
                        x,y = GOAL_DICT[self.tiles[r][c]]
                        total += (abs(r - x) + abs(c - y))

        return total
            
    
    def __eq__(self, other):
        """return True if the called object (self) and the argument (other) 
        have the same values for the tiles attribute"""
        
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[0])):
                if self.tiles[i][j] != other.tiles[i][j]:
                    return False
        return True
                
        
        
        

        
        
        
        
        
        
        
        
        
        
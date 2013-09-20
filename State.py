

from helpers import *

class State:
    """
    3 x 3 board representing the state
    """

    goalStateMap = None


    directionRowColDict = {"nw" : (0,0), "n": (0,1), "ne" : (0,2),
                                "w"  : (1,0), "c": (1,1), "e"  : (1,2),
                                "sw" : (2,0), "s": (2,1), "se" : (2,2)}
                                
    indexToDirectionDict = { 0:"nw", 1:"n", 2:"ne",3:"w", 4:"c", 5:"e", 6:"sw", 7:"s", 8: "se"}

    def __init__(self,kList):
        self.board = [ [ " "," ", " "], [" "," "," "], [" "," "," "]]

        if kList != None and len(kList) == 9:
        
            for idx,val in enumerate(kList):

                direction = State.indexToDirectionDict.get(idx,None)

                if direction!=None:
                    self.setValueAtDirection(val,direction)



    

    def setValueAtDirection(self,kValue,kDirection):
        kTuple = State.directionRowColDict.get(kDirection)
        row , col = rolCol(kTuple)
        self.board[row][col] = kValue


    def printBoard(self):
        for i in range(0,3):
            print " "
            for j in range(0,3):
                if self.board[i][j] == 'blank':
                    print " ",
                else:
                    print self.board[i][j],

        print " "


    def sameAsState(self,kState):
        """
        compare the states are same
        """

        for row in range(0,3):
            for col in range(0,3):
                if self.board[row][col] != kState.board[row][col]:
                    return False

        return True

   
    def getCoordinatesForBlank(self):
        """
        return row and col of the blank cell
        """

        for row in range(0,3):
            for col in range(0,3):
                if self.board[row][col] == 'blank':
                    return (row,col)

        return None

    def setState(self,kState):
        """
        copy row col values from arg state to self state
        """
        for row in range(0,3):
            for col in range(0,3):
                self.board[row][col] = kState.board[row][col]



    def moveBlankStateToPosition(self,kBlankCoord,kTargetCoord):
        """
        swap elements 
        """

        targetrow, targetcol = rolCol(kTargetCoord)
        blankrow, blankcol = rolCol(kBlankCoord)
        self.board[blankrow][blankcol] = self.board[targetrow][targetcol];
        self.board[targetrow][targetcol] = 'blank'
        

    @classmethod
    def cloneState(cls,kState):
        """
        -create a new state
        -set the board to the board of kstate
        """
        newState = cls(None)
        newState.setState(kState)
        return newState


    @classmethod
    def getStateFromStateAndMovingBlankToCoordinate(cls,kState,kBlankCell,kTargetPos):
        """
        -create new state by cloning existing state
        -move the blank cell to other position as specified by kTargetPos(tuple(row,col))
        -
        """
        newState = cls.cloneState(kState)
        newState.moveBlankStateToPosition(kBlankCell,kTargetPos)
        return newState
        
        
    def differenceInStates(self,kGoalState):
        """
        heuristic function
        calculate the number of cells are misplaced as compared to the goal state
        """


        diff = 0

        for row in range(0,3):
            for col in range(0,3):
                if self.board[row][col] != kGoalState.board[row][col]:
                    diff = diff+1
                else:
                    pass

        return diff



    def totalStepsToTravelForGoalState(self,kGoalState):
        """
        Total steps for each cell
        step = horizontal distance + vertical distance
        """


        goalStateMap = {1 : (0,0), 2:(0,1), 3:(0,2),
                        4 : (1,0), 5:(1,1), 6:(1,2),
                        7 : (2,0), 8:(2,1), 'blank':(2,2)}
                        

        diff = 0

    
        for row in range(0,3):
            for col in range(0,3):
                # get row col posiiton in target booard
                value = self.board[row][col]
                trow,tcol = rolCol(goalStateMap[value])
                d = abs(trow-row) + abs(tcol-col)
                diff = diff + d
#                print "Diff for val",value,"is :",d," diff : ",diff
            

        
       # raw_input()
        return diff


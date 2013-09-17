
from helpers import *
from Node import *
from State import *
from collections import deque
import csv
import time
        




fringe = []
visitedStates = []
solutions = []

fHeu = True

def stateAlreadyVisited(kState):
    """
    check if state is already visited
    """

    visited = False
    
    for st in visitedStates:
        #check if both states are same
        visited = areStatesSame(st,kState)
        if visited == True:
            return visited

    return visited
            
                    



#get next nodes from given node

def getChildNodes(kNode):
    """
    get child nodes for a parent node
    """
    childNodes = []
    blankCoordinate = kNode.state.getCoordinatesForBlank()
    if blankCoordinate:
        #print blankCoordinate
        for tup in getMovesForPosition(blankCoordinate):
            newState = State.getStateFromStateAndMovingBlankToCoordinate(kNode.state,blankCoordinate,tup)
            #if stateAlreadyVisited(newState) == False:
                #create new node from the state
            newNode = Node.initWithRootNodeAndState(kNode,newState)
            childNodes.append(newNode)

    if len(childNodes)>0:
        print "Parent",
        kNode.printState()
        print "The children are...."
        for c in childNodes:
            c.printState()
   
    return childNodes
    




def printQueue():

    print "----start of queue----"

    for node in fringe:
        node.printState()

    print "---end if queue---"



#function to get the next node for BFS

def getNextNode():
    """
    get next node

    for un-informed search removed first from the list

    """

    global fringe 

    #remove first element from the queue for breadth-first search
    nextnode = fringe.pop(0)

    return nextnode



def getTotalStepsToReachGoalState(kNode,kGoalState):
    """
    get total step each cell has to travel to get to specified position in goal state

    """

    h  = kNode.state.totalStepsToTravelForGoalState(kGoalState)
    g = kNode.level
    f = h + g

    return f


def getNextNodeUsingTotalStepsToTravel(kGoalState):
    """
    select next node depending the heuristic
    heuristic is
    number of cells which are not at the orignal position
    """
   
    global fringe
    global solutions



    minNode = None
    minCost = 99999999999
    minNodeIndex = -1

    
    pnode = None
    pcost = None

    if len(solutions)>0 and solutions[0] != None:
        pnode = solutions[0];
        pcost = getTotalStepsToReachGoalState(pnode,kGoalState)
        print pnode, pcost
       # raw_input()
       



    for idx,node in enumerate(fringe):
       #get the heu. function values
       g_value =getTotalStepsToReachGoalState(node,kGoalState)
           

       if g_value < minCost:
           minNode = node
           minNodeIndex = idx
           minCost = g_value


    fringe.pop(minNodeIndex)
    c = getTotalStepsToReachGoalState(minNode,kGoalState)
    if pnode != None:
        if c > pcost:
            minNode = None
    
    return minNode

#function to h for A* first heuristic
#check number of cells which are out of oreder

def getHValueForNode(kNode,kGoalState):
    h = kNode.state.differenceInStates(kGoalState)
    g = kNode.level
    f = h +g
    return f



def getNextNodeUsingCellDiff(kGoalState):
    """
    select next node depending the heuristic
    heuristic is
    number of cells which are not at the orignal position
    """
   
    global fringe
    global solutions

   



    minNode = None
    minCost = 99999999999
    minNodeIndex = -1

    
    pnode = None
    pcost = None

    if len(solutions)>0 and solutions[0] != None:
        pnode = solutions[0];
        pcost = getHValueForNode(pnode,kGoalState)
        print pnode, pcost
        raw_input()
       



    for idx,node in enumerate(fringe):
       #get the heu. function values
       g_value = getHValueForNode(node,kGoalState)
           

       if g_value < minCost:
           minNode = node
           minNodeIndex = idx
           minCost = g_value


    fringe.pop(minNodeIndex)
    c = getHValueForNode(minNode,kGoalState)
    if pnode != None:
        if c > pcost:
            minNode = None
    
    return minNode
    
    

def informed(kParentNode,kGoalState,kLimit):
    """
    get goal state
    """
    global fringe
    global visitedStates
    global solutions

    
    totalNodeVisited = 0

    #clear the visited nodes list
    visitedStates = []

    #clear solutions accumulated in previous passes
    solutions = []

    depth = 0
    
    while len(fringe) > 0 and kLimit > 0:
        # get next node fromt the fringe
        print "getting next from queue..."
        printQueue()

        #remove this condition and make seperate functions for different heuristic
        nextNode = None
        if fHeu:
            nextNode = getNextNodeUsingCellDiff(kGoalState) 
        else:
            nextNode = getNextNodeUsingTotalStepsToTravel(kGoalState) 


        #fringe exhausted
        if nextNode == None:
            raw_input("Find")
            return solutions,totalNodeVisited


        nextNode.visited = True
        visitedStates.append(nextNode.state)
        
        totalNodeVisited = totalNodeVisited +1
        kLimit = kLimit - 1
        
        print "Extracted Node...."
        nextNode.printState()
        
        #check if this node state is same as goal state
        if nextNode.isSameStateAs(kGoalState):
            print " goal state found"
            solutions.append(nextNode)
            raw_input()
        else:
            pass


        #get successors from current state         
        childNodes = getChildNodes(nextNode)
        if childNodes and len(childNodes) > 0 :
            #print childNodes,len(childNodes)
            for node in childNodes:
                #print node
                #check if the node is already visited
                if stateAlreadyVisited(node.state) == False:
                     fringe.append(node)



    return solutions,totalNodeVisited





def bfs(kParentNode,kGoalState,kLimit):
    """
    get goal state
    """
    global fringe
    global visitedStates
    
    #clear the visited nodes list
    visitedStates = []




    
    depth = 0
    idx = 0
    nodesvisited = 0

    while len(fringe) > 0 and kLimit > 0:
       
        # get next node fromt the fringe
        print "getting next from queue..."
        printQueue()
       
        nextNode =  getNextNode()
        nextNode.visited = True
        visitedStates.append(nextNode.state)
        
        nodesvisited = nodesvisited + 1
        kLimit = kLimit - 1
        
        print "Extracted Node...."
        nextNode.printState()
        
        #check if this node state is same as goal state
        if nextNode.isSameStateAs(kGoalState):
            print " goal state found"
            return nextNode, nodesvisited
        else:
            print " not goal state"



        #get successors from current state         
        childNodes = getChildNodes(nextNode)
        if childNodes and len(childNodes) > 0 :
            #print childNodes,len(childNodes)
            for node in childNodes:
                #print node
                #check if the node is already visited
                if stateAlreadyVisited(node.state) == False:
                     fringe.append(node)



    return None,nodesvisited







def makeState(*args,**kwargs):
    """
    make a new state from the elements from the list
    """
    
    cells = []

    for item in args:
        #print item
        cells.append(item)
    
    newState = State(cells)
    #newState.printBoard()
    return newState





def testiUninformedSearch(kInitialState,kgoalState,kLimit):
    """
    perform blind search
    BFS

    """

    
    global fringe

    #empty the fringe

    fringe = []


    
    #goalState.printBoard()
    root = Node.initRootNodeWithState(kInitialState)
    #root.printState();
    fringe.append(root)
    
    
    goalnNode,nodesChecked = bfs(root,kgoalState,kLimit);
    if goalnNode != None:
        print "------Uninformed Search (BFS) ---------: ",goalnNode.level,nodesChecked
        goalnNode.printPath()
        return goalnNode,nodesChecked

   
    return None,nodesChecked

    




def testInformedSearch(kInitialState,kgoalState,kLimit):

    """
    perform A* search 
    """


    global fringe

    #empty fringe

    fringe = []

    root = Node.initRootNodeWithState(kInitialState)
    fringe.append(root)
    sol,nodesVisited = informed(root,kgoalState,kLimit)


       

    if sol and sol[0] != None:
        print "------Informed search : ---------: ",sol[0].level,nodesVisited
        sol[0].printPath()
        return sol[0],nodesVisited

    raw_input()

    return None,nodesVisited



def main():
    goalState  = makeState(1,2,3,4,5,6,7,8,'blank') 

    # First group of test cases - should have solutions with depth <= 5
    initialState1 = makeState(2, "blank", 3, 1, 5, 6, 4, 7, 8)
    initialState2 = makeState(1, 2, 3, "blank", 4, 6, 7, 5, 8)
    initialState3 = makeState(1, 2, 3, 4, 5, 6, 7, "blank", 8)
    initialState4 = makeState(1, "blank", 3, 5, 2, 6, 4, 7, 8)
    initialState5 = makeState(1, 2, 3, 4, 8, 5, 7, "blank", 6)


    # Second group of test cases - should have solutions with depth <= 10
    initialState6 = makeState(2, 8, 3, 1, "blank", 5, 4, 7, 6)
    initialState7 = makeState(1, 2, 3, 4, 5, 6, "blank", 7, 8)
    initialState8 = makeState("blank", 2, 3, 1, 5, 6, 4, 7, 8)
    initialState9 = makeState(1, 3, "blank", 4, 2, 6, 7, 5, 8)
    initialState10 = makeState(1, 3, "blank", 4, 2, 5, 7, 8, 6)


    # Third group of test cases - should have solutions with depth <= 20
    initialState11 = makeState("blank", 5, 3, 2, 1, 6, 4, 7, 8)
    initialState12 = makeState(5, 1, 3, 2, "blank", 6, 4, 7, 8)
    initialState13 = makeState(2, 3, 8, 1, 6, 5, 4, 7, "blank")
    initialState14 = makeState(1, 2, 3, 5, "blank", 6, 4, 7, 8)
    initialState15 = makeState("blank", 3, 6, 2, 1, 5, 4, 7, 8)


    # Fourth group of test cases - should have solutions with depth <= 50
    initialState16 = makeState(2, 6, 5, 4, "blank", 3, 7, 1, 8)
    initialState17 = makeState(3, 6, "blank", 5, 7, 8, 2, 1, 4)
    initialState18 = makeState(1, 5, "blank", 2, 3, 8, 4, 6, 7)
    initialState19 = makeState(2, 5, 3, 4, "blank", 8, 6, 1, 7)
    initialState20 = makeState(3, 8, 5, 1, 6, 7, 4, 2, "blank")




    testcases = [initialState1,initialState2,initialState3,initialState4,initialState5,initialState6,initialState7,initialState8]

    initialState = initialState20
    test_no = 19

    global fHeu

    fHeu = False


    


    #bfsGoalNode,bfsCost = testiUninformedSearch(initialState,goalState,2000)
    startTime  = time.time()
    iGoalNode,iCost = testInformedSearch(initialState,goalState,2000)
    endTime = time.time()
    timeDiff = endTime-startTime




    print "\n"*100
    #print "BFS RESULT"
    #if bfsGoalNode != None:
    #    bfsGoalNode.printPath()
    #    print "BFS COST:",bfsCost,"BFS DEPTH:",bfsGoalNode.level
    #else: 
    #    print "BFS COST:",bfsCost

    print ""
    print "INFORMED SEARCH  RESULT"



    searchCost = iCost
    level = -1
    if iGoalNode !=  None:
        iGoalNode.printPath()
        level = iGoalNode.level
        print "INF COST:",searchCost,"INFORMED DEPTH:",iGoalNode.level,timeDiff," secs"
    else:
        print "Cannot find solution Cost:",searchCost,timeDiff," secs"


"""
    if fHeu == True:
        r = csv.writer(open('firstHeu.csv','ab+'))
        r.writerow([test_no,searchCost,level,endTime-startTime])
    else:
        r = csv.writer(open('secondHeu.csv','ab+'))
        r.writerow([test_no,searchCost,level,endTime-startTime])
"""



    #goalState.printBoard()
    #root = Node.initRootNodeWithState(initialState)
    #root.printState();
    #global fringe
    #fringe.append(root)
    
    
    #goalnNode,depth = bfs(root,goalState,10);
    #print "------depth---------: ",goalnNode.level,depth
    #goalnNode.printPath()

    #return
    #sol,nodesVisited = informed(root,goalState,10)
    #print "------depth---------: ",sol[0].level,nodesVisited
    #sol[0].printPath()




if __name__ == '__main__':
    main()

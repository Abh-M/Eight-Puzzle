
from helpers import *
from Node import *
from State import *
from collections import deque
import csv
import time
        




fringe = []
visitedStates = []
solutions = []

fHeu = None

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

    
    #uncomment following block to print children of particular node

    """
    if len(childNodes)>0:
        print "Parent",
        kNode.printState()
        print "The children are...."
        for c in childNodes:
            c.printState()
    """


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





def bfs(kParentNode,kGoalState,kLimit):
    """
    get goal state
    """
    global fringe
    global visitedStates
    
    #clear the visited nodes list
    visitedStates = []

    nodesvisited = 0

    while len(fringe) > 0 and kLimit > 0:
       
        # get next node fromt the fringe
        print "getting next from queue..."
        #printQueue()
       
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
            pass
            #print " not goal state"



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





def testUninformedSearch(kInitialState,kgoalState,kLimit):
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
    
   
    startTime = time.time()
    goalnNode,nodesChecked = bfs(root,kgoalState,kLimit);
    endTime = time.time()

    timeDiff = endTime - startTime

    if goalnNode != None:
        print "------Uninformed Search (BFS) ---------: ",
        goalnNode.printPath()
        print "Depth :",goalnNode.level,"| Nodes Visisted :",nodesChecked,"| Duration :",timeDiff,"seconds"
        return goalnNode,nodesChecked,timeDiff
    else:
        nodesChecked = 0
        print "-------Could not find result------"


   
    return None,nodesChecked,timeDiff

    



def main():
    pass


if __name__ == '__main__':
    main()


        

from State import *
from helpers import *

class Node:
    """
    Tree Node
    """
    state_key = 'state'
    parent_key = 'parent'
    cost_key = 'cost'
    visited_key = 'visited'

    def __init__(self, *args,**kwargs):

        self.state = kwargs.get(Node.state_key,None)
        self.parent = kwargs.get(Node.parent_key,None)
        self.visited = False
        self.level = 0 if self.parent == None else self.parent.level+1


    #different constructors with different arguments

    @classmethod
    def initRootNodeWithState(cls,kState):
        return  Node(state=kState)

    @classmethod
    def initWithRootNodeAndState(cls,kRoot,kState):
        newNode = Node(state=kState,parent=kRoot)
        #print "--------------------",newNode.parent
        return newNode
    

    def printState(self):
        self.state.printBoard()

    
    def isSameStateAs(self,kState):
        return self.state.sameAsState(kState)


    def getBlankCellCoordinate(self):
        return self.state.getCoordinatesForBlank()

    def printPath(self):

        path = []
        nxt = self
        while nxt is not  None:
            path.insert(0,nxt)
            nxt = nxt.parent
        
        for node in path:
            node.printState()



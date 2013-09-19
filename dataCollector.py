


from EightPuzzle import testUninformedSearch, testInformedSearchOne, testInformedSearchTwo, testUninformedSearch, makeState
import csv


class SearchMethod:
    BFS, CELL_DIFF, MANHATTAN = range(0,3)




def getFileHandle(kSearchType, purge = True):
    
    """
    create csv writer for appropriate file and return it
    searchmethod 0  -> BFS
                 1  -> Cell difference heuristic
                 2  -> mahnattan distance heuristic
    """

    fileName =  "BFS.CSV" if kSearchType == SearchMethod.BFS else "CellDiff.csv" if kSearchType == SearchMethod.CELL_DIFF else "Manhattan.csv"
    
    openMode  = "wb+" if purge == True else "ab+"

    csvWriter = csv.writer(open(fileName,openMode))

    if openMode == "wb+":
        csvWriter.writerow(["#","Nodes Visisted","Path Length","Duration","Limit"])


    

    return csvWriter


def executeTestCases(testcaseList,goalState,searchType):
    """

    perform test based on the search Type

    """


    if searchType == SearchMethod.CELL_DIFF or searchType == SearchMethod.MANHATTAN:
        
        #set the flag for first heuristic

        logFile  = getFileHandle(searchType,True)

        limit = 5000

        for index,initialState in enumerate(testcaseList):

            #perform initial test and write result to the file
            
            finalNode = None
            searchCost = 0
            timeDiff = 0
            level = 0

            if SearchMethod.CELL_DIFF == searchType:
                finalNode,searchCost,timeDiff = testInformedSearchOne(initialState,goalState,limit)
            elif SearchMethod.MANHATTAN == searchType:
                finalNode,searchType,timeDiff = testInformedSearchTwo(initialState,goalState,limit)

            
            
            if finalNode !=  None:
                finalNode.printPath()
                level = finalNode.level
                print "INF COST:",searchCost," | INFORMED DEPTH:",level,"| DURAIION :",timeDiff," secs"
            else:
                print "Cannot find solution Cost:",searchCost," | DURATION ",timeDiff," secs"


            #write result to file
            logFile.writerow([index+1,searchCost,level,timeDiff,limit])

    elif searchType == SearchMethod.BFS:

        limit = 50000

        logFile = getFileHandle(searchType,True)

        for index,initialState in enumerate(testcaseList):

            finalNode,searchCost,timeDiff  = testUninformedSearch(initialState,goalState,limit)

            level = 0
            
            if finalNode !=  None:
                finalNode.printPath()
                level = finalNode.level
                
                print "BFS COST:",searchCost," | BFS  DEPTH:",level,"| DURAIION :",timeDiff," secs"
            else:
                print "Cannot find solution Cost:",searchCost," | DURATION ",timeDiff," secs"

            #write result to file
            logFile.writerow([index+1,searchCost,level,timeDiff,limit])






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




    testcases = [initialState1,initialState2,initialState3,initialState4,initialState5,initialState6,initialState7,initialState8,initialState9,initialState10,initialState11,initialState12,initialState13,initialState14,initialState15,initialState16,initialState17,initialState18,initialState19,initialState20]


    executeTestCases(testcases[0:20],goalState,SearchMethod.CELL_DIFF)
    #executeTestCases(testcases[0:6],goalState,SearchMethod.MANHATTAN)
    #executeTestCases(testcases[0:12],goalState,SearchMethod.BFS)



if __name__ == "__main__":
    main()

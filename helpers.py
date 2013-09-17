




class SearchMethod:
    BFS, CELL_DIFF, MANHATTAN = range(0,3)




def row(kTuple):
    return kTuple[0]

def col(kTuple):
    return kTuple[1]


def rolCol(kTuple):
    return kTuple[0], kTuple[1]



def getMovesForPosition(kTuple):
    row,col = rolCol(kTuple)
    #check if can be moved up
    if row>0:
        yield (row-1,col)

    # check if can be moved down
    if row<2:
        yield (row+1,col)

    #check if can be moved left
    if col>0:
        yield (row,col-1)

    #check if can be moved right
    if col<2:
        yield (row,col+1)


def areStatesSame(s1,s2):
    """
    compare two states
    """
    for row in range(0,3):
        for col in range(0,3):
            if s1.board[row][col] != s2.board[row][col]:
                return False


    return True




def AgetFileHandle(searchMethod, purge = True):
    
    """
    create csv writer for appropriate file and return it
    searchmethod 0  -> BFS
                 1  -> Cell difference heuristic
                 2  -> mahnattan distance heuristic
    """

    fileName =  "BFS.CSV" if searchmethod == 1 else "CellDiff.csv" if searchmethod == 1 else "Manhattan.csv"
    
    openMode  = "wb+" if purge == True else "ab+"

    csvWriter = csv.writer(open(fileName,openMode))


    return csvwrite




    











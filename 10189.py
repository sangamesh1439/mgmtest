import sys

def printInSameLine(arg):
    print(arg,end="")

def calculateAdjucentMines(n,m,i, j, field):
    adjucentMines=0
    for ii in range (i-1, min(i+2, n)):
        for jj in range (j-1, min(j+2, m)):
            if ii >= 0 and jj >= 0:
                if(field[ii][jj] == '*'):
                    adjucentMines = adjucentMines+1
    return adjucentMines

def minesweeper(n, m, field):
    for i in range(0, n):
        for j in range(0, m):
            if field[i][j] == '*':
                printInSameLine('*')
            else:
                adjucentMines = calculateAdjucentMines(n, m, i,j,field)
                printInSameLine(adjucentMines)
        print("")
        

fieldCount = 1
for nm in sys.stdin:
    [n, m] = map(int, nm.split(" "))
    
    field = []
    for i in range (0, n):
        row = list(sys.stdin.readline().strip())
        field.append(row)

    print("Field #%d:"%fieldCount)
    minesweeper(n,m,field)
    fieldCount = fieldCount+1
    print("")
exit(0)

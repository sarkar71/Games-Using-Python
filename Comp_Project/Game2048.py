import random
from GameBasics import moveRightAction1D, moveLeftAction1D, \
 transMatrix, createZeroMatrix
from PrintGame import print2DMatrix 
from StoringDataInCsv import StoreScoreToCsv, CalculateHighestScore
from msvcrt import getch
Mat2D = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# Initialize
# Input: Matxix , number of elements to initialize
# Output: Changed Matrix according to Action taken

def InitializeValues2D(Mat2D, n):

    # Initializing 2D Matrix
    Status = True
    EmptyIndexList = []
    for i in range(len(Mat2D)):
        for j in range(len(Mat2D)):
            if (Mat2D[i][j] == 0):
                EmptyIndexList.append((i, j))

    # Checking if EmptyIndexList has any element in it
    if len(EmptyIndexList) == 0:
        Status = False
        return [["G", "A", "M", "E"], [0, 0, 0, 0], \
        ["O", "V", "E", "R"]], Status

    # Entering New Random Element in the matrix
    for i in range(n):
        (EmpRandRowIdx, EmpRandColIdx) = random.choice(EmptyIndexList)
        RandElementChoice = random.choice([2, 4])
        Mat2D[EmpRandRowIdx][EmpRandColIdx] = RandElementChoice
    return Mat2D, Status

# Actions
# Move Left 2D
def moveLeftAction2D(Mat2D):
    Status = True
    for i in range(len(Mat2D)):
        Mat1D = Mat2D[i]
        Mat2D[i] = moveLeftAction1D(Mat1D)
    return Mat2D, Status

# Move Right 2D
def moveRightAction2D(Mat2D):
    Status = True
    for i in range(len(Mat2D)):
        Mat1D = Mat2D[i]
        Mat2D[i] = moveRightAction1D(Mat1D)
    return Mat2D , Status

# Move Up 2D
def moveUpAction2D(Mat2D):
    Status = True
    Mat2D, Status = moveLeftAction2D(transMatrix(Mat2D))
    return transMatrix(Mat2D), Status

# Move Down 2D
def moveDownAction2D(Mat2D):
    Status = True
    Mat2D, Status = moveRightAction2D(transMatrix(Mat2D))
    return transMatrix(Mat2D), Status



# TEST

if __name__=="__main__":
    try:
        name = input("Enter your full name?")
        n = int(input("Enter the size of board - 4/8: "))
        Mat2D = createZeroMatrix(n)
        print("Starting the game")
        Mat2D, Status = InitializeValues2D(Mat2D, 2)
        print2DMatrix(Mat2D)
        print("###########################################")
        # IF Status = True --> O/P = Changed 2D Matrix
        score = 0
        while Status:
            score += 5
            a = ord(getch())

            # Mapping with Arrow key Press
            if a ==75:
                Mat2D, Status = moveLeftAction2D(Mat2D)
            elif a==77:
                Mat2D, Status = moveRightAction2D(Mat2D)
            elif a == 72:
                Mat2D, Status = moveUpAction2D(Mat2D)
            elif a == 80:
                Mat2D, Status = moveDownAction2D(Mat2D)
            elif a == 27:  # ESC
                score -= 5
                break
            else:
                score -= 5
                continue
            Mat2D, Status = InitializeValues2D(Mat2D, 1)

            print2DMatrix(Mat2D)

            print("################ SCORE = "+str(score)+" ################")

        # Printing Score after each move
        print("Your total score is "+str(score))
        # Storing Name , Board Size, Score in File
        StoreScoreToCsv(name,n,score)
        # Storing Name of Highest Scorer and Hisghest Scorer Name According to Board Size
        ScorerName, HighestScore = CalculateHighestScore(n)
        print("############# HIGHEST SCORE ################")
        print("In "+str(n)+" X "+str(n)+" board :")
        print("Highest Scorer: "+str(ScorerName))
        print("Highest Score: "+str(HighestScore))
        print("############################################")

    except Exception:
        print("error in values entered... Please exit and try again")
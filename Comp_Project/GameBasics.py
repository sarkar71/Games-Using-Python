import random
# Step 1
# initialize 2 elements in the array (only 2)

def initializeGame1D(Mat1D,n):
    i = 0
    while(i<n):
        x = random.randint(0, len(Mat1D)-1)
        Mat1D[x] = 2
        i += 1
    return Mat1D

# Step 2
# Right or Left Addition operations
# Only addition of same numbers

def moveToRight1D(Mat1D):
    # When Action = Swipe Right
    for i in range(len(Mat1D)-2, -1, -1):
        for j in range(i, len(Mat1D)-1):
            if Mat1D[j+1] == 0:
                (Mat1D[j], Mat1D[j+1]) = \
                (Mat1D[j+1], Mat1D[j])
    return Mat1D

def moveToLeft1D(Mat1D):
    # When Action = Swipe Left
    for i in range(len(Mat1D)-1):
        for j in range(i, -1,-1):
            if Mat1D[j] == 0:
                Mat1D[j], Mat1D[j+1] = \
                Mat1D[j+1], Mat1D[j]
    return Mat1D

def addMoveLeft1D(Mat1D):
    # Adding same numbers to Left
    i = 0
    while (i < len(Mat1D)-1):
        if Mat1D[i] == Mat1D[i + 1]:
            (Mat1D[i], Mat1D[i + 1]) = (Mat1D[i + 1] + Mat1D[i], 0)
            i += 2
        else:
            i += 1
    return moveToLeft1D(Mat1D)

def addMoveRight1D(Mat1D):
    # Adding same numbers to Right
    i = len(Mat1D)-1
    while(i > 0):
        if Mat1D[i] == Mat1D[i-1]:
            (Mat1D[i], Mat1D[i-1]) = (0, Mat1D[i-1]+Mat1D[i])
            i -= 2
        else:
            i -= 1

    return moveToRight1D(Mat1D)

def moveRightAction1D(Mat1D):
    # Shifting Mat1D To Right
    Mat1D = moveToRight1D(Mat1D)
    Mat1D = addMoveRight1D(Mat1D)
    return Mat1D

def moveLeftAction1D(Mat1D):
    # Shifting Mat1D to Left
    Mat1D = moveToLeft1D(Mat1D)
    Mat1D = addMoveLeft1D(Mat1D)
    return Mat1D

# Enter one new element after every Action

def newElementEnter1D(Mat1D):
    emp =[]
    for i in range(len(Mat1D)):
        if Mat1D[i]==0:
            emp.append(i)

    if len(emp) == 0:
        return "Game Over"

    Mat1D[random.choice(emp)] = 2

    return Mat1D

def transMatrix(Mat2D):
    M = []
    for i in range(len(Mat2D)):
        R = []
        for j in range(len(Mat2D)):
            R.append(Mat2D[j][i])
        M.append(R)
    return M

# For positioning 0 in the Matrix
def createZeroMatrix(n):
    Mat2D = []
    for i in range(n):
        a = []
        for j in range(n):
            a.append(0)
        Mat2D.append(a)
    return Mat2D
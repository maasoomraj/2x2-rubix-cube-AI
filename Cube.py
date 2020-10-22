class Cube:
    def __init__(self, state):
        self.IdealState = [["G", "G", "G", "G"],
                           ["Y", "Y", "Y", "Y"],
                           ["O", "O", "O", "O"],
                           ["W", "W", "W", "W"],
                           ["B", "B", "B", "B"],
                           ["R", "R", "R", "R"]]
        self.state = state
        self.visited = [state]
        self.rotation = []
        
    def rotateFront(self, actual, times):
        state = []
        if(actual):
            state = self.state
        else:
            for i in range(len(self.state)):
                s = []
                for j in range(len(self.state[0])):
                    s.append(self.state[i][j])
                state.append(s)

        for i in range(times):      
            edge1 = state[1][0], state[1][2]
            edge2 = state[2][0], state[2][2]
            edge3 = state[3][0], state[3][2]
            edge4 = state[5][3], state[5][1]

            state[5][3], state[5][1] = edge3
            state[3][0], state[3][2] = edge2
            state[2][0], state[2][2] = edge1
            state[1][0], state[1][2] = edge4

            square1 = state[0][2]
            state[0][2] = state[0][3]
            state[0][3] = state[0][1]
            state[0][1] = state[0][0]
            state[0][0] = square1
        return self.misplacedCorners(state), state

    def rotateBack(self, actual, times):
        state = []
        if(actual):
            state = self.state
        else:
            for i in range(len(self.state)):
                s = []
                for j in range(len(self.state[0])):
                    s.append(self.state[i][j])
                state.append(s)
        
        edge1 = state[2][3], state[2][1]
        edge2 = state[1][3], state[1][1]
        edge3 = state[5][0], state[5][2]
        edge4 = state[3][3], state[3][1]

        state[3][3], state[3][1] = edge3
        state[5][0], state[5][2] = edge2
        state[1][3], state[1][1] = edge1
        state[2][3], state[2][1] = edge4
        
        square1 = state[4][2]
        state[4][2] = state[4][3]
        state[4][3] = state[4][1]
        state[4][1] = state[4][0]
        state[4][0] = square1
        return self.misplacedCorners(state), state

    def rotateLeft(self, actual, times):
        state = []
        if(actual):
            state = self.state
        else:
            for i in range(len(self.state)):
                s = []
                for j in range(len(self.state[0])):
                    s.append(self.state[i][j])
                state.append(s)
        
        edge1 = state[5][1], state[5][0]
        edge2 = state[4][1], state[4][0]
        edge3 = state[2][1], state[2][0]
        edge4 = state[0][1], state[0][0]

        state[0][1], state[0][0] = edge3
        state[2][1], state[2][0] = edge2
        state[4][1], state[4][0] = edge1
        state[5][1], state[5][0] = edge4

        square1 = state[1][2]
        state[1][2] = state[1][3]
        state[1][3] = state[1][1]
        state[1][1] = state[1][0]
        state[1][0] = square1
        return self.misplacedCorners(state), state
        
    def rotateRight(self, actual, times):
        state = []
        if(actual):
            state = self.state
        else:
            for i in range(len(self.state)):
                s = []
                for j in range(len(self.state[0])):
                    s.append(self.state[i][j])
                state.append(s)
        
        edge1 = state[0][2], state[0][3]
        edge2 = state[2][2], state[2][3]
        edge3 = state[4][2], state[4][3]
        edge4 = state[5][2], state[5][3]

        state[5][2], state[5][3] = edge3
        state[4][2], state[4][3] = edge2
        state[2][2], state[2][3] = edge1
        state[0][2], state[0][3] = edge4
        
        square1 = state[3][2]
        state[3][2] = state[3][3]
        state[3][3] = state[3][1]
        state[3][1] = state[3][0]
        state[3][0] = square1
        return self.misplacedCorners(state), state

    def rotateTop(self, actual, times):
        state = []
        if(actual):
            state = self.state
        else:
            for i in range(len(self.state)):
                s = []
                for j in range(len(self.state[0])):
                    s.append(self.state[i][j])
                state.append(s)
        
        edge1 = state[0][3], state[0][1]
        edge2 = state[1][2], state[1][3]
        edge3 = state[4][0], state[4][2]
        edge4 = state[3][1], state[3][0]

        state[3][1], state[3][0] = edge3
        state[4][0], state[4][2] = edge2
        state[1][2], state[1][3] = edge1
        state[0][3], state[0][1] = edge4
        
        square1 = state[2][2]
        state[2][2] = state[2][3]
        state[2][3] = state[2][1]
        state[2][1] = state[2][0]
        state[2][0] = square1
        return self.misplacedCorners(state), state
        
    def rotateBottom(self, actual, times):
        state = []
        if(actual):
            state = self.state
        else:
            for i in range(len(self.state)):
                s = []
                for j in range(len(self.state[0])):
                    s.append(self.state[i][j])
                state.append(s)
        
        edge1 = state[0][0], state[0][2]
        edge2 = state[1][1], state[1][0]
        edge3 = state[4][3], state[4][1]
        edge4 = state[3][2], state[3][3]

        state[3][2], state[3][3] = edge3
        state[4][3], state[4][1] = edge2
        state[1][1], state[1][0] = edge1
        state[0][0], state[0][2] = edge4
        
        square1 = state[5][2]
        state[5][2] = state[5][3]
        state[5][3] = state[5][1]
        state[5][1] = state[5][0]
        state[5][0] = square1
        return self.misplacedCorners(state), state

    # def rotateCube(self, move):
    #     if(move == "Front 90"):
    #         self.rotateFront(True, 1)
    #     elif(move == "Front 180"):
    #         self.rotateFront(True, 2)
    #     elif(move == "Front 270"):
    #         self.rotateFront(True, 3)
    #     elif(move == "Back 90"):
    #         self.rotateBack(True, 1)
    #     elif(move == "Back 180"):
    #         self.rotateBack(True, 2)
    #     elif(move == "Back 270"):
    #         self.rotateBack(True, 3)
    #     elif(move == "Top 90"):
    #         self.rotateTop(True, 1)
    #     elif(move == "Top 180"):
    #         self.rotateTop(True, 2)
    #     elif(move == "Top 270"):
    #         self.rotateTop(True, 3)
    #     elif(move == "Bottom 90"):
    #         self.rotateBottom(True, 1)
    #     elif(move == "Bottom 180"):
    #         self.rotateBottom(True, 2)
    #     elif(move == "Bottom 270"):
    #         self.rotateBottom(True, 3)
    #     elif(move == "Left 90"):
    #         self.rotateLeft(True, 1)
    #     elif(move == "Left 180"):
    #         self.rotateLeft(True, 2)
    #     elif(move == "Left 270"):
    #         self.rotateLeft(True, 3)
    #     elif(move == "Right 90"):
    #         self.rotateRight(True, 1)
    #     elif(move == "Right 180"):
    #         self.rotateRight(True, 2)
    #     elif(move == "Right 270"):
    #         self.rotateRight(True, 3)

    def printCube(self):
        print ("")
        print (" "),(" "),(" "),(" "),self.state[1][0],self.state[1][1]
        print (" "),(" "),(" "),(" "),self.state[1][2],self.state[1][3]
        print (" "),self.state[0][0],self.state[0][1],(" "),self.state[2][0],self.state[2][1],(" "),\
                self.state[4][0],self.state[4][1],(" "),self.state[5][0],self.state[5][1]
        print (" "),self.state[0][2],self.state[0][3],(" "),self.state[2][2],self.state[2][3],(" "),\
                self.state[4][2],self.state[4][3],(" "),self.state[5][2],self.state[5][3]
        print (" "),(" "),(" "),(" "),self.state[3][0],self.state[3][1]
        print (" "),(" "),(" "),(" "),self.state[3][2],self.state[3][3]
        print ("")

    def misplacedCorners(self, state):
        misplaced = 0
        for i in range(len(state)):
            for j in range(len(state[0])):
                if(self.IdealState[i][j] != state[i][j]):
                    misplaced += 1
        return misplaced

    def moves(self):
        arr = []
        arr.append(("Front 90",self.rotateFront(False, 1)))
        arr.append(("Front 180",self.rotateFront(False, 2)))
        arr.append(("Front 270",self.rotateFront(False, 3)))

        arr.append(("Back 90",self.rotateBack(False, 1)))
        arr.append(("Back 180",self.rotateBack(False, 2)))
        arr.append(("Back 270",self.rotateBack(False, 3)))

        arr.append(("Top 90",self.rotateTop(False, 1)))
        arr.append(("Top 180",self.rotateTop(False, 2)))
        arr.append(("Top 270",self.rotateTop(False, 3)))

        arr.append(("Bottom 90",self.rotateBottom(False, 1)))
        arr.append(("Bottom 180",self.rotateBottom(False, 2)))
        arr.append(("Bottom 270",self.rotateBottom(False, 3)))

        arr.append(("Left 90",self.rotateLeft(False, 1)))
        arr.append(("Left 180",self.rotateLeft(False, 2)))
        arr.append(("Left 270",self.rotateLeft(False, 3)))

        arr.append(("Right 90",self.rotateRight(False, 1)))
        arr.append(("Right 180",self.rotateRight(False, 2)))
        arr.append(("Right 270",self.rotateRight(False, 3)))
        arr.sort(key = lambda x: x[1][0])

        # print(arr)
        currentMisplaced = self.misplacedCorners(self.state)
        for i in range(len(arr)):
            if(arr[i][1][1] not in self.visited and arr[i][1][0] <= currentMisplaced+1):
                self.visited += [arr[i][1][1]]
                self.rotation += [arr[i][0]]
                self.state = arr[i][1][1]
                # self.rotateCube(arr[i][0])
                break
        self.printCube()

    def isGoalState(self):
        for i in range(len(self.state)):
            for j in range(len(self.state[0])):
                if(self.state[i][j] != self.IdealState[i][j]):
                    return False
        return True

    def solve(self):
        for i in range(1000):
            if not self.isGoalState():
                self.moves()
            else:
                print(self.rotation)
                break
        print(self.rotation)

problem = [["R", "Y", "G", "B"],
           ["G", "O", "B", "G"],
           ["O", "R", "Y", "W"],
           ["R", "R", "Y", "G"],
           ["W", "W", "B", "O"],
           ["B", "Y", "W", "O"]]

mas = Cube(problem)
# mas.rotateBottom(False)
mas.solve()
# print(mas.rotateFront(True, 2))
# mas.printCube()
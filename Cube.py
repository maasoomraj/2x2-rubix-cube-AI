import util

class Cube:
    def __init__(self):
        self.IdealState = [["G", "G", "G", "G"],
                           ["Y", "Y", "Y", "Y"],
                           ["O", "O", "O", "O"],
                           ["W", "W", "W", "W"],
                           ["B", "B", "B", "B"],
                           ["R", "R", "R", "R"]]
        self.visited = []
        self.corners = [dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict()]
        self.visitedCorners = [[],[],[],[],[],[],[],[]]
        
    # Function for clockwise rotation of Front Face
    def rotateFront(self, currState, times):
        state = []
        for i in range(len(currState)):
            s = []
            for j in range(len(currState[0])):
                s.append(currState[i][j])
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
        return state

    # Function for clockwise rotation of Back Face
    def rotateBack(self, currState, times):
        state = []
        for i in range(len(currState)):
            s = []
            for j in range(len(currState[0])):
                s.append(currState[i][j])
            state.append(s)
        
        for i in range(times):   
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
        return state

    # Function for clockwise rotation of Left Face
    def rotateLeft(self, currState, times):
        state = []
        for i in range(len(currState)):
            s = []
            for j in range(len(currState[0])):
                s.append(currState[i][j])
            state.append(s)
        
        for i in range(times):   
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
        return state
        
    # Function for clockwise rotation of Right Face
    def rotateRight(self, currState, times):
        state = []
        for i in range(len(currState)):
            s = []
            for j in range(len(currState[0])):
                s.append(currState[i][j])
            state.append(s)
        
        for i in range(times):   
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
        return state

    # Function for clockwise rotation of Top Face
    def rotateTop(self, currState, times):
        state = []
        for i in range(len(currState)):
            s = []
            for j in range(len(currState[0])):
                s.append(currState[i][j])
            state.append(s)
        
        for i in range(times):   
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
        return state
    
    # Function for clockwise rotation of Bottom Face
    def rotateBottom(self, currState, times):
        state = []
        for i in range(len(currState)):
            s = []
            for j in range(len(currState[0])):
                s.append(currState[i][j])
            state.append(s)
        
        for i in range(times):   
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
        return state

    # Function to print cube in a well manner
    def printCube(self, state):
        print ("")
        print (" "),(" "),(" "),(" "),state[1][0],state[1][1]
        print (" "),(" "),(" "),(" "),state[1][2],state[1][3]
        print (" "),state[0][0],state[0][1],(" "),state[2][0],state[2][1],(" "),\
                state[4][0],state[4][1],(" "),state[5][0],state[5][1]
        print (" "),state[0][2],state[0][3],(" "),state[2][2],state[2][3],(" "),\
                state[4][2],state[4][3],(" "),state[5][2],state[5][3]
        print (" "),(" "),(" "),(" "),state[3][0],state[3][1]
        print (" "),(" "),(" "),(" "),state[3][2],state[3][3]
        print ("")

    # Anti-Clockwise rotation is 3 times clockwise rotation of face
    # Half Rotation is 2 times clockwise rotation of face

    # Function to rotate top face in all 3 ways
    def topRotation(self, state):
        arr = []
        arr.append(("Top 90",self.rotateTop(state, 1)))
        arr.append(("Top 180",self.rotateTop(state, 2)))
        arr.append(("Top 270",self.rotateTop(state, 3)))
        return arr

    # Function to rotate bottom face in all 3 ways
    def bottomRotation(self, state):
        arr = []
        arr.append(("Bottom 90",self.rotateBottom(state, 1)))
        arr.append(("Bottom 180",self.rotateBottom(state, 2)))
        arr.append(("Bottom 270",self.rotateBottom(state, 3)))
        return arr

    # Function to rotate front face in all 3 ways
    def frontRotation(self, state):
        arr = []
        arr.append(("Front 90",self.rotateFront(state, 1)))
        arr.append(("Front 180",self.rotateFront(state, 2)))
        arr.append(("Front 270",self.rotateFront(state, 3)))
        return arr

    # Function to rotate back face in all 3 ways
    def backRotation(self, state):
        arr = []
        arr.append(("Back 90",self.rotateBack(state, 1)))
        arr.append(("Back 180",self.rotateBack(state, 2)))
        arr.append(("Back 270",self.rotateBack(state, 3)))
        return arr

    # Function to rotate left face in all 3 ways
    def leftRotation(self, state):
        arr = []
        arr.append(("Left 90",self.rotateLeft(state, 1)))
        arr.append(("Left 180",self.rotateLeft(state, 2)))
        arr.append(("Left 270",self.rotateLeft(state, 3)))
        return arr

    # Function to rotate right face in all 3 ways
    def rightRotation(self, state):
        arr = []
        arr.append(("Right 90",self.rotateRight(state, 1)))
        arr.append(("Right 180",self.rotateRight(state, 2)))
        arr.append(("Right 270",self.rotateRight(state, 3)))
        return arr

    # Function to rotate a given state, in all 18 possible ways
    # Returns a 3d array, where each item is a 2d array after rotation
    def moves(self, state):
        arr = []
        arr += self.topRotation(state)
        arr += self.bottomRotation(state)
        arr += self.frontRotation(state)
        arr += self.backRotation(state)
        arr += self.leftRotation(state)
        arr += self.rightRotation(state)
        return arr

    # Function to check if given state is a goal state or not
    # return True if goal state, else return False
    def isGoalState(self, state):
        for i in range(len(state)):
            for j in range(len(state[0])):
                if(state[i][j] != self.IdealState[i][j]):
                    return False
        return True

    ############################################################################################################################
    ############################################################################################################################


    # Given below is Code for not pre-computing, and finding number of moves to bring cube to ideal position
    # during time of finding heuristic value
    # This method is not implemented as it takes a lot of time, for testing purpose
    
    # Function to make moves in 9 possible ways depending on cubes position
    # def heuristicMove(self, state, cube):
    #     arr = []
    #     # Find cubes position
    #     cubesPosition = self.positionOfCube(state)[cube]
    #     if(cubesPosition == 0 or cubesPosition == 1 or cubesPosition == 2 or cubesPosition == 3):
    #         arr += self.frontRotation(state)
    #     if(cubesPosition == 4 or cubesPosition == 5 or cubesPosition == 6 or cubesPosition == 7):
    #         arr += self.backRotation(state)
    #     if(cubesPosition == 0 or cubesPosition == 1 or cubesPosition == 4 or cubesPosition == 5):
    #         arr += self.topRotation(state)
    #     if(cubesPosition == 2 or cubesPosition == 3 or cubesPosition == 6 or cubesPosition == 7):
    #         arr += self.bottomRotation(state)
    #     if(cubesPosition == 0 or cubesPosition == 2 or cubesPosition == 4 or cubesPosition == 6):
    #         arr += self.leftRotation(state)
    #     if(cubesPosition == 1 or cubesPosition == 3 or cubesPosition == 5 or cubesPosition == 7):
    #         arr += self.rightRotation(state)
    #     # print(len(arr))
    #     return arr

    # Function to find position of all 8 Cubes in given state
    # def positionOfCube(self, state):
    #     cubes = [["G", "Y", "O"], ["G", "O", "W"], ["G", "Y", "R"], ["G", "W", "R"],
    #              ["B", "O", "Y"], ["B", "O", "W"], ["B", "Y", "R"], ["B", "W", "R"]]
        
    #     orientation = [[0,1,2], [0,2,1], [1,0,2], [1,2,0], [2,0,1], [2,1,0]]
    #     cubesPosition = [0,0,0,0,0,0,0,0]
    #     for i in range(len(cubes)):
    #         for j in range(len(orientation)):
    #             if(state[0][1] == cubes[i][orientation[j][0]] and state[1][2] == cubes[i][orientation[j][1]] and state[2][0] == cubes[i][orientation[j][2]]):
    #                 cubesPosition[0] = i
    #             if(state[0][3] == cubes[i][orientation[j][0]] and state[2][2] == cubes[i][orientation[j][1]] and state[3][0] == cubes[i][orientation[j][2]]):
    #                 cubesPosition[1] = i
    #             if(state[0][0] == cubes[i][orientation[j][0]] and state[1][0] == cubes[i][orientation[j][1]] and state[5][1] == cubes[i][orientation[j][2]]):
    #                 cubesPosition[2] = i
    #             if(state[0][2] == cubes[i][orientation[j][0]] and state[3][2] == cubes[i][orientation[j][1]] and state[5][3] == cubes[i][orientation[j][2]]):
    #                 cubesPosition[3] = i
                
    #             if(state[4][0] == cubes[i][orientation[j][0]] and state[2][1] == cubes[i][orientation[j][1]] and state[1][3] == cubes[i][orientation[j][2]]):
    #                 cubesPosition[4] = i
    #             if(state[4][1] == cubes[i][orientation[j][0]] and state[5][0] == cubes[i][orientation[j][1]] and state[1][1] == cubes[i][orientation[j][2]]):
    #                 cubesPosition[6] = i
    #             if(state[4][2] == cubes[i][orientation[j][0]] and state[2][3] == cubes[i][orientation[j][1]] and state[3][1] == cubes[i][orientation[j][2]]):
    #                 cubesPosition[5] = i
    #             if(state[4][3] == cubes[i][orientation[j][0]] and state[5][2] == cubes[i][orientation[j][1]] and state[3][3] == cubes[i][orientation[j][2]]):
    #                 cubesPosition[7] = i
    #     # print(cubesPosition)
    #     # cubesMap = [[0,0,1],[0,1,1],[0,0,0],[0,1,0],[0,1,1],[1,1,1],[0,1,0],[1,1,0]]
    #     # manhattan = 0
    #     # for i in range(7):
    #     #     a1 = cubesMap[idealCubesPosition[i]]
    #     #     a2 = cubesMap[cubesPosition[i]]
    #     #     manhattan += abs(a1[0]-a2[0]) + abs(a1[1]-a2[1]) + abs(a1[2]-a2[2])
    #     # print((manhattan+0.0)/(4.0))
    #     # return (manhattan+0.0)/(4.0)
    #     return cubesPosition  
    
    # Heuristic function when we are not pre computing number of moves
    # def heuristic(self, currState):
    #     cubesNumber = [[[0,1],[1,2],[2,0]],[[0,3],[2,2],[3,0]],[[0,0],[1,0],[5,1]],[[0,2],[3,2],[5,3]],
    #                    [[4,0],[2,1],[1,3]],[[4,1],[5,0],[1,1]],[[4,2],[2,3],[3,1]],[[4,3],[5,2],[3,3]]]
    #     cubesColor = [["G", "Y", "O"], ["G", "O", "W"], ["G", "Y", "R"], ["G", "W", "R"],
    #                   ["B", "O", "Y"], ["B", "R", "Y"], ["B", "O", "W"], ["B", "R", "W"]]
    #     answer = 0
    #     for i in range(8):
    #         visited = []
    #         que = util.Queue()
    #         que.push((currState, 0))
    #         while(not que.isEmpty()):
    #             state, steps = que.pop()
    #             visited += [state]

    #             if(steps == 4):
    #                 answer += steps
    #                 break

    #             if(state[cubesNumber[i][0][0]][cubesNumber[i][0][1]] == cubesColor[i][0] and
    #                state[cubesNumber[i][1][0]][cubesNumber[i][1][1]] == cubesColor[i][1] and 
    #                state[cubesNumber[i][2][0]][cubesNumber[i][2][1]] == cubesColor[i][2]):
    #                 answer += steps
    #                 break

    #             arr = self.heuristicMove(state, i)
    #             for j in range(len(arr)):
    #                 if(arr[j][1] not in visited):
    #                     que.push((arr[j][1], steps+1))

    #     # print("Heuristic", answer)
    #     return (answer+0.0)/(4.0)


    ############################################################################################################################
    ############################################################################################################################

    # Since, we want less computation for this project, we have made an assumption that
    # If number of moves to bring a cube to particular position is more than 4, we will consider it any high number say 11
    def heuristicFunction(self, state):
        value = 0
        # Stores cubes
        cube0 = [state[0][1], state[1][2], state[2][0]]
        cube1 = [state[0][3], state[2][2], state[3][0]]
        cube2 = [state[0][0], state[1][0], state[5][1]]
        cube3 = [state[0][2], state[3][2], state[5][3]]
        cube4 = [state[4][0], state[2][1], state[1][3]]
        cube5 = [state[4][2], state[2][3], state[3][1]]
        cube6 = [state[4][1], state[5][0], state[1][1]]
        cube7 = [state[4][3], state[5][3], state[3][3]]
        arr = []
        arr1 = []
        # Convert list to str, to search in dictionary
        arr.append(' '.join(map(str, cube0)))
        arr.append(' '.join(map(str, cube1)))
        arr.append(' '.join(map(str, cube2)))
        arr.append(' '.join(map(str, cube3)))
        arr.append(' '.join(map(str, cube4)))
        arr.append(' '.join(map(str, cube5)))
        arr.append(' '.join(map(str, cube6)))
        arr.append(' '.join(map(str, cube7)))
        arr1.append(cube0)
        arr1.append(cube1)
        arr1.append(cube2)
        arr1.append(cube3)
        arr1.append(cube4)
        arr1.append(cube5)
        arr1.append(cube6)
        arr1.append(cube7)

        for i in range(len(arr)):
            if(arr1[i] in self.visitedCorners[i]):
                # print(self.corners[i][arr[i]])
                value += self.corners[i][arr[i]]
            else:
                # print(11)
                value += 11

        # returns heuristic value / 4
        return (value+0.0)/4.0

    # Function to fill visited corners and orientation of corner
    # Function which create dictionary for number of moves to reach ideal position for a cube
    def mapCorner(self, state, directions):
        l = len(directions)

        cube0 = [state[0][1], state[1][2], state[2][0]]
        if(cube0 not in self.visitedCorners[0]):
            self.visitedCorners[0] += [cube0]
            self.corners[0][' '.join(map(str, cube0))] = l
        cube1 = [state[0][3], state[2][2], state[3][0]]
        if(cube1 not in self.visitedCorners[1]):
            self.visitedCorners[1] += [cube1]
            self.corners[1][' '.join(map(str, cube1))] = l
        cube2 = [state[0][0], state[1][0], state[5][1]]
        if(cube2 not in self.visitedCorners[2]):
            self.visitedCorners[2] += [cube2]
            self.corners[2][' '.join(map(str, cube2))] = l
        cube3 = [state[0][2], state[3][2], state[5][3]]
        if(cube3 not in self.visitedCorners[3]):
            self.visitedCorners[3] += [cube3]
            self.corners[3][' '.join(map(str, cube3))] = l
        cube4 = [state[4][0], state[2][1], state[1][3]]
        if(cube4 not in self.visitedCorners[4]):
            self.visitedCorners[4] += [cube4]
            self.corners[4][' '.join(map(str, cube4))] = l
        cube5 = [state[4][2], state[2][3], state[3][1]]
        if(cube5 not in self.visitedCorners[5]):
            self.visitedCorners[5] += [cube5]
            self.corners[5][' '.join(map(str, cube5))] = l
        cube6 = [state[4][1], state[5][0], state[1][1]]
        if(cube6 not in self.visitedCorners[6]):
            self.visitedCorners[6] += [cube6]
            self.corners[6][' '.join(map(str, cube6))] = l
        cube7 = [state[4][3], state[5][3], state[3][3]]
        if(cube7 not in self.visitedCorners[7]):
            self.visitedCorners[7] += [cube7]
            self.corners[7][' '.join(map(str, cube7))] = l

    # A simple DFS run , to pre compute values for heuristic function
    def preSolve(self):
        print("Pre computation before solving Rubix Cube ...")
        que = util.Stack()
        que.push((self.IdealState, 0, []))
        visited = []
        while(not que.isEmpty()):
            state, depth, directions = que.pop()
            visited += [state]

            self.mapCorner(state, directions)

            # Since, the computation will be very high, but this will be one time computation only
            # I have run BFS till depth 4
            if(depth == 3):
                break

            arr = self.moves(state)
            for i in range(len(arr)):
                if(arr[i][1] not in visited):
                    que.push((arr[i][1], depth+1,  directions + [arr[i][0]]))
        print("Pre computation done, to faster solving rubix cube ... !")

    def dfs(self, d, state):
        # DFS till depth d, as DFS requires less space
        # BFS promises optimal solution
        # Iterative Deepening DFS requires less space and promises optimal solution

        # answer array initialised to []
        answer = []
        
        # Stack for implementing DFS
        que = util.Stack()
        # Calculating fOfN for starting state
        fOfN = self.heuristicFunction(state),
        que.push((state, 0, fOfN, []))
        # Visited array initialised to []
        visited = []
        while(not que.isEmpty()):
            state, depth, fn, directions = que.pop()
            # Push node in visited array
            visited += [state]

            # check for goal state
            if(self.isGoalState(state)):
                answer = directions
                break

            # obtain list of 2d array, where each 2d array is state after rotation
            arr = self.moves(state)
            for i in range(len(arr)):
                # If depth is less than equal to desired DFS depth
                # If this state is not previously visited
                if(depth + 1 <= d and arr[i][1] not in visited):
                    # find heuristic value
                    hn = self.heuristicFunction(arr[i][1])
                    # f(n) = g(n) + h(n)
                    fn1 = (depth + 1) + hn
                    if(fn1 < fn):
                        que.push((arr[i][1], depth+1, fn1, directions + [arr[i][0]]))
                        # que.push((arr[i][1], depth+1, fn1, directions + [arr[i][0]]), fn1)
        return answer

    # Main function which solves the rubix cube
    def solve(self, state):
        print("Started Solving Rubix Cube ...")
        # Pre-Computation
        self.preSolve()
        answer = []
        for d in range(10):
            answer = self.dfs(d, state)
            if(len(answer) > 0):
                break
        print("Successfully Solved")
        print(answer)

problem = []
with open('input.txt') as f:
    for line in f:
        inner_list = [elt.strip() for elt in line.split(',')]
        problem.append(inner_list)

rubix = Cube()
rubix.solve(problem)

# G,G,G,G
# R,O,R,O
# Y,W,Y,W
# O,R,O,R
# B,B,B,B
# Y,W,Y,W

# G,O,G,W
# R,Y,G,O
# Y,B,O,W
# B,R,O,R
# Y,R,B,B
# G,W,Y,W
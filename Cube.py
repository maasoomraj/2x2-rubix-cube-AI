import util

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
        return state

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
        return state

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
        return state
        
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
        return state

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
        return state
        
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
        return state

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

    def moves(self, state):
        self.state = state
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
        return arr
    
    def heuristicMove(self, currState, cube):
        self.state = currState
        arr = []
        cubesPosition = self.positionOfCube(currState)[cube]
        if(cubesPosition == 0 or cubesPosition == 1 or cubesPosition == 2 or cubesPosition == 3):
            arr.append(("Front 90",self.rotateFront(False, 1)))
            arr.append(("Front 180",self.rotateFront(False, 2)))
            arr.append(("Front 270",self.rotateFront(False, 3)))
        if(cubesPosition == 4 or cubesPosition == 5 or cubesPosition == 6 or cubesPosition == 7):
            arr.append(("Back 90",self.rotateBack(False, 1)))
            arr.append(("Back 180",self.rotateBack(False, 2)))
            arr.append(("Back 270",self.rotateBack(False, 3)))
        if(cubesPosition == 0 or cubesPosition == 1 or cubesPosition == 4 or cubesPosition == 5):
            arr.append(("Top 90",self.rotateTop(False, 1)))
            arr.append(("Top 180",self.rotateTop(False, 2)))
            arr.append(("Top 270",self.rotateTop(False, 3)))
        if(cubesPosition == 2 or cubesPosition == 3 or cubesPosition == 6 or cubesPosition == 7):
            arr.append(("Bottom 90",self.rotateBottom(False, 1)))
            arr.append(("Bottom 180",self.rotateBottom(False, 2)))
            arr.append(("Bottom 270",self.rotateBottom(False, 3)))
        if(cubesPosition == 0 or cubesPosition == 2 or cubesPosition == 4 or cubesPosition == 6):
            arr.append(("Left 90",self.rotateLeft(False, 1)))
            arr.append(("Left 180",self.rotateLeft(False, 2)))
            arr.append(("Left 270",self.rotateLeft(False, 3)))
        if(cubesPosition == 1 or cubesPosition == 3 or cubesPosition == 5 or cubesPosition == 7):
            arr.append(("Right 90",self.rotateRight(False, 1)))
            arr.append(("Right 180",self.rotateRight(False, 2)))
            arr.append(("Right 270",self.rotateRight(False, 3)))
        # print(len(arr))
        return arr
        

    def isGoalState(self, state):
        for i in range(len(state)):
            for j in range(len(state[0])):
                if(state[i][j] != self.IdealState[i][j]):
                    return False
        return True

    def positionOfCube(self, state):
        cubes = [["G", "Y", "O"], ["G", "O", "W"], ["G", "Y", "R"], ["G", "W", "R"],
                 ["B", "O", "Y"], ["B", "O", "W"], ["B", "Y", "R"], ["B", "W", "R"]]
        
        orientation = [[0,1,2], [0,2,1], [1,0,2], [1,2,0], [2,0,1], [2,1,0]]
        cubesPosition = [0,0,0,0,0,0,0,0]
        for i in range(len(cubes)):
            for j in range(len(orientation)):
                if(state[0][1] == cubes[i][orientation[j][0]] and state[1][2] == cubes[i][orientation[j][1]] and state[2][0] == cubes[i][orientation[j][2]]):
                    cubesPosition[0] = i
                if(state[0][3] == cubes[i][orientation[j][0]] and state[2][2] == cubes[i][orientation[j][1]] and state[3][0] == cubes[i][orientation[j][2]]):
                    cubesPosition[1] = i
                if(state[0][0] == cubes[i][orientation[j][0]] and state[1][0] == cubes[i][orientation[j][1]] and state[5][1] == cubes[i][orientation[j][2]]):
                    cubesPosition[2] = i
                if(state[0][2] == cubes[i][orientation[j][0]] and state[3][2] == cubes[i][orientation[j][1]] and state[5][3] == cubes[i][orientation[j][2]]):
                    cubesPosition[3] = i
                
                if(state[4][0] == cubes[i][orientation[j][0]] and state[2][1] == cubes[i][orientation[j][1]] and state[1][3] == cubes[i][orientation[j][2]]):
                    cubesPosition[4] = i
                if(state[4][1] == cubes[i][orientation[j][0]] and state[5][0] == cubes[i][orientation[j][1]] and state[1][1] == cubes[i][orientation[j][2]]):
                    cubesPosition[6] = i
                if(state[4][2] == cubes[i][orientation[j][0]] and state[2][3] == cubes[i][orientation[j][1]] and state[3][1] == cubes[i][orientation[j][2]]):
                    cubesPosition[5] = i
                if(state[4][3] == cubes[i][orientation[j][0]] and state[5][2] == cubes[i][orientation[j][1]] and state[3][3] == cubes[i][orientation[j][2]]):
                    cubesPosition[7] = i
        # print(cubesPosition)
        # cubesMap = [[0,0,1],[0,1,1],[0,0,0],[0,1,0],[0,1,1],[1,1,1],[0,1,0],[1,1,0]]
        # manhattan = 0
        # for i in range(7):
        #     a1 = cubesMap[idealCubesPosition[i]]
        #     a2 = cubesMap[cubesPosition[i]]
        #     manhattan += abs(a1[0]-a2[0]) + abs(a1[1]-a2[1]) + abs(a1[2]-a2[2])
        # print((manhattan+0.0)/(4.0))
        # return (manhattan+0.0)/(4.0)
        return cubesPosition  
    
    def heuristic(self, currState):
        cubesNumber = [[[0,1],[1,2],[2,0]],[[0,3],[2,2],[3,0]],[[0,0],[1,0],[5,1]],[[0,2],[3,2],[5,3]],
                       [[4,0],[2,1],[1,3]],[[4,1],[5,0],[1,1]],[[4,2],[2,3],[3,1]],[[4,3],[5,2],[3,3]]]
        cubesColor = [["G", "Y", "O"], ["G", "O", "W"], ["G", "Y", "R"], ["G", "W", "R"],
                      ["B", "O", "Y"], ["B", "R", "Y"], ["B", "O", "W"], ["B", "R", "W"]]
        answer = 0
        for i in range(8):
            visited = []
            que = util.Queue()
            que.push((currState, 0))
            while(not que.isEmpty()):
                state, steps = que.pop()
                visited += [state]

                if(steps == 4):
                    answer += steps
                    break

                if(state[cubesNumber[i][0][0]][cubesNumber[i][0][1]] == cubesColor[i][0] and
                   state[cubesNumber[i][1][0]][cubesNumber[i][1][1]] == cubesColor[i][1] and 
                   state[cubesNumber[i][2][0]][cubesNumber[i][2][1]] == cubesColor[i][2]):
                    answer += steps
                    break

                arr = self.heuristicMove(state, i)
                for j in range(len(arr)):
                    if(arr[j][1] not in visited):
                        que.push((arr[j][1], steps+1))

        print("Heuristic", answer)
        return (answer+0.0)/(4.0)


    def solve(self):
        print("Hello")
        # que = util.PriorityQueue()
        que = util.Queue()
        fOfN = self.heuristic(self.state),
        # que.push((self.state, 0, fOfN, []), fOfN)
        que.push((self.state, 0, fOfN, []))
        answer = []
        while(not que.isEmpty()):
            state, depth, fn, directions = que.pop()
            print(len(self.visited))
            self.visited += [state]

            if(self.isGoalState(state)):
                answer = directions
                print("Found")
                break

            arr = self.moves(state)
            for i in range(len(arr)):
                hn = self.heuristic(arr[i][1])
                fn1 = depth + 1 + hn
                print(fn1)
                if(fn1 <= fn and arr[i][1] not in self.visited):
                    que.push((arr[i][1], depth+1, fn1, directions + [arr[i][0]]))
                    # que.push((arr[i][1], depth+1, fn1, directions + [arr[i][0]]), fn1)

        print(answer)

problem = [["G", "O", "G", "W"],
           ["R", "Y", "G", "G"],
           ["Y", "Y", "O", "O"],
           ["B", "B", "O", "W"],
           ["R", "B", "Y", "B"],
           ["R", "W", "R", "W"]]

mas = Cube(problem)
# mas.rotateBottom(False)
mas.solve()
# print(mas.rotateFront(True, 2))
# mas.printCube()
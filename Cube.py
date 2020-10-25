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
        # return self.misplacedCorners(state), state
        return self.manhattanDistance(state), state

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
        return self.manhattanDistance(state), state

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
        return self.manhattanDistance(state), state
        
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
        return self.manhattanDistance(state), state

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
        return self.manhattanDistance(state), state
        
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
        return self.manhattanDistance(state), state

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
        arr.sort(key = lambda x: x[1][0])

        return arr

        # currentMisplaced = self.misplacedCorners(self.state)
        # broke = False
        # for i in range(len(arr)):
        #     if(arr[i][1][1] not in self.visited):
        #         self.visited += [arr[i][1][1]]
        #         self.rotation += [arr[i][0]]
        #         self.state = arr[i][1][1]
        #         broke = True
        #         break
        # if broke:
        #     self.printCube()

    def isGoalState(self, state):
        
        for i in range(len(state)):
            for j in range(len(state[0])):
                if(state[i][j] != self.IdealState[i][j]):
                    return False
        return True

    def manhattanDistance(self, state):
        # opposite = []
        # same = []
        # oppositeColors = ["B", "W", "R", "Y", "G", "O"]
        # sameColors = ["G", "Y", "O", "W", "B", "R"]
        # for i in range(6):
        #     color1 = 0
        #     color2 = 0
        #     for j in range(4):
        #         if(state[i][j] == oppositeColors[i]):
        #             color1 += 1
        #         if(state[i][j] == sameColors[i]):
        #             color2 += 1
        #     opposite.append(color1)
        #     same.append(color2)
        # manhattan = 0
        # for i in range(6):
        #     manhattan += 2*opposite[i]
        #     manhattan += 4 - same[i] - opposite[i]
        # return manhattan/4
        # state = self.IdealState
        cubes = [["G", "Y", "O"], ["G", "O", "W"], ["G", "Y", "R"], ["G", "W", "R"],
                 ["B", "O", "Y"], ["B", "O", "W"], ["B", "Y", "R"], ["B", "W", "R"]]
        
        orientation = [[0,1,2], [0,2,1], [1,0,2], [1,2,0], [2,0,1], [2,1,0]]
        idealCubesPosition = [0,1,2,3,4,5,6,7]
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
        print(cubesPosition)
        cubesMap = [[0,0,1],[0,1,1],[0,0,0],[0,1,0],[0,1,1],[1,1,1],[0,1,0],[1,1,0]]
        manhattan = 0
        for i in range(7):
            a1 = cubesMap[idealCubesPosition[i]]
            a2 = cubesMap[cubesPosition[i]]
            manhattan += abs(a1[0]-a2[0]) + abs(a1[1]-a2[1]) + abs(a1[2]-a2[2])
        # print((manhattan+0.0)/(4.0))
        return (manhattan+0.0)/(4.0)
                

    def solve(self):
        que = util.Queue()
        print(self.manhattanDistance(self.state))
        que.push((self.state, 0, 0 + self.manhattanDistance(self.state), []))

        answer = []
        while(not que.isEmpty()):
            state, depth, fn, directions = que.pop()
            print(depth)
            self.visited += [state]

            if(self.isGoalState(state)):
                answer = directions
                print("Found")
                break

            arr = self.moves(state)
            for i in range(len(arr)):
                fn1 = depth + 1 + arr[i][1][0]
                if(fn1 <= fn and arr[i][1][1] not in self.visited):
                    que.push((arr[i][1][1], depth+1, fn1, directions + [arr[i][0]]))

        print(answer)
        self.printCube()
        # print(self.rotation)

problem = [["B", "O", "R", "W"],
           ["Y", "W", "G", "W"],
           ["Y", "B", "G", "R"],
           ["O", "Y", "Y", "R"],
           ["O", "G", "B", "W"],
           ["R", "O", "B", "G"]]

mas = Cube(problem)
# mas.rotateBottom(False)
mas.solve()
# print(mas.rotateFront(True, 2))
# mas.printCube()
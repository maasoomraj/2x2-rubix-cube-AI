class Cube:
    def __init__(self, state):
        self.IdealState = [["G", "G", "G", "G"],
                     ["Y", "Y", "Y", "Y"],
                     ["O", "O", "O", "O"],
                     ["W", "W", "W", "W"],
                     ["B", "B", "B", "B"],
                     ["R", "R", "R", "R"]]
        self.state = state
        
    def rotateFront(self, actual):
        state = []
        if(actual):
            state = self.state
        else:
            for i in range(len(self.state)):
                s = []
                for j in range(len(self.state[0])):
                    s.append(self.state[i][j])
                state.append(s)
                    
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
        print(state)
        print(self.state)

    def rotateBack(self, actual):
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
        print(state)

    def rotateLeft(self, actual):
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
        print(state)
        
    def rotateRight(self, actual):
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
        print(state)

    def rotateTop(self, actual):
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
        print(state)
        
    def rotateBottom(self, actual):
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
        print(state)

problem = [["R", "Y", "G", "B"],
           ["G", "O", "B", "G"],
           ["O", "R", "Y", "W"],
           ["R", "R", "Y", "G"],
           ["W", "W", "B", "O"],
           ["B", "Y", "W", "O"]]

mas = Cube(problem)
mas.rotateBottom(False)
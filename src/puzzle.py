import copy
class puzzle:

    def __init__(self,type,iter):
        self.grid = []
        self.x0=0
        self.y0=0
        self.gsize=0

        if(type==1):
            file_read = open("../data/input", "r")
            lines = file_read.readlines()
            file_read.close()
            i = -1
            for string in lines:
                if not (i == -1):
                    self.grid.append([])
                line = string.split()
                j = 0
                for val in line:
                    if (i == -1):
                        self.gsize = int(val)
                        break
                    self.grid[i].append(int(val))
                    if self.grid[i][j] == 0:
                        self.x0 = i
                        self.y0 = j
                    j = j + 1
                i = i + 1

        elif type==2:
            file_read = open("../data/"+ str(iter) + ".txt", "r")
            lines = file_read.readlines()
            file_read.close()
            i = -1
            for string in lines:
                if not (i == -1):
                    self.grid.append([])
                line = string.split()
                j = 0
                for val in line:
                    if (i == -1):
                        self.gsize = int(val)
                        break
                    self.grid[i].append(int(val))
                    if self.grid[i][j] == 0:
                        self.x0 = i
                        self.y0 = j
                    j = j + 1
                i = i + 1


    def __cmp__(self, other):
            return True
            # kaaj ache

    def __gt__(self, other):
            # return self.displacementDistance() < other.displacementDistance()
            return True
            # kaaj ache

    def goalState(self):
        ans=""
        for j in range(0, self.gsize * self.gsize):
            ans += str(j) + " "
        return ans
    def valid(self,x,y):
            if x>=0 and x<self.gsize and y>=0 and y<self.gsize :
                return True
            else:
                return False
    def swap(self,x0,y0,x1,y1):
        self.grid[x0][y0] = self.grid[x1][y1]
        self.grid[x1][y1] = 0
    def right(self):
        if not(self.valid(self.x0,self.y0+1)):
            return False
        temp = puzzle(0,0)
        temp.x0 = self.x0
        temp.y0 = self.y0
        temp.grid = copy.deepcopy(self.grid)
        temp.gsize = self.gsize
        temp.swap(temp.x0,temp.y0,temp.x0,temp.y0+1)
        temp.y0 = temp.y0 + 1
        return temp

    def left(self):
        if not(self.valid(self.x0,self.y0-1)):
            return False
        temp = puzzle(0,0)
        temp.x0 = self.x0
        temp.y0 = self.y0
        temp.grid = copy.deepcopy(self.grid)
        temp.gsize = self.gsize
        temp.swap(temp.x0,temp.y0,temp.x0,temp.y0-1)
        temp.y0 = temp.y0-1
        return temp

    def up(self):
        if not(self.valid(self.x0-1,self.y0)):
            return False
        temp = puzzle(0,0)
        temp.x0 = self.x0
        temp.y0 = self.y0
        temp.grid = copy.deepcopy(self.grid)
        temp.gsize = self.gsize
        temp.swap(temp.x0,temp.y0,temp.x0-1,temp.y0)
        temp.x0 = temp.x0-1
        return temp

    def down(self):
        if not(self.valid(self.x0+1,self.y0)):
            return False
        temp = puzzle(0,0)
        temp.x0 = self.x0
        temp.y0 = self.y0
        temp.grid = copy.deepcopy(self.grid)
        temp.gsize = self.gsize
        temp.swap(temp.x0,temp.y0,temp.x0+1,temp.y0)
        temp.x0 = temp.x0 + 1
        return temp
    def toString(self):
        st = ""
        for i in range(self.gsize):
            for j in range(self.gsize):
                st += str(self.grid[i][j])+" "
        return  st

    def displacementDistance(self):
        distance = 0
        for i in range(self.gsize):
            for j in range(self.gsize):
                current = self.grid[i][j]
                truex = current//self.gsize
                truey = current%self.gsize

                if not (i == truex and j == truey):
                    distance = distance + 1
        return distance


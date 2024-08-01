import puzzle
from queue import PriorityQueue
class BFS:

    def start(self,puzzle):

        queue = list()
        visited = {}
        map = {}
        parent = {}
        ind = 0
        pq = PriorityQueue()

        steps = 0
        queue.append(puzzle)
        parent[ind] = -1
        map[ind] = puzzle
        visited[puzzle.toString()] = 0

        ans = puzzle.goalState()
        sol = []
        if(puzzle.toString()==ans):
            sol.insert(0, puzzle.grid)
            return sol


        while (len(queue)>0):
            temp = queue.pop(0)
            curPuzzle = temp
            pid = visited[curPuzzle.toString()]
            for i in range(4):
                if (i == 0):
                    nextPuzzle = curPuzzle.left()
                elif (i == 1):
                    nextPuzzle = curPuzzle.up()
                elif (i == 2):
                    nextPuzzle = curPuzzle.right()
                elif (i == 3):
                    nextPuzzle = curPuzzle.down()
                if (nextPuzzle != False and nextPuzzle != None):
                    if not nextPuzzle.toString() in visited:
                        ind += 1
                        queue.append(nextPuzzle)
                        visited[nextPuzzle.toString()] = ind
                        parent[ind] = pid
                        map[ind] = nextPuzzle

                        if (nextPuzzle.toString() == ans):

                            path = ind
                            while (path != -1):
                                sol.insert(0, nextPuzzle.grid)
                                path = parent[path]
                                if (path == -1):
                                    break
                                nextPuzzle = map[path]
                            return sol,visited
        return False



class UCS:

    def start(self,puzzle):

        queue = []
        visited = {}
        map = {}
        parent = {}
        ind =0
        pq = PriorityQueue()

        steps =0
        pq.put((steps,puzzle))
        parent[ind] = -1
        map[ind] = puzzle
        visited[puzzle.toString()] = 0


        ans = puzzle.goalState()

        sol = []
        if (puzzle.toString() == ans):
            sol.insert(0, puzzle.grid)
            return sol

        while(pq.not_empty):
            temp = pq.get()
            curPuzzle =  temp[1]
            parentCost = temp[0]
            pid = visited[curPuzzle.toString()]
            for i in range(4):
                if (i == 0):
                    nextPuzzle = curPuzzle.left()
                elif (i == 1):
                    nextPuzzle = curPuzzle.up()
                elif (i == 2):
                    nextPuzzle = curPuzzle.right()
                elif (i == 3):
                    nextPuzzle = curPuzzle.down()
                if(nextPuzzle!=False and nextPuzzle!=None):
                    if not nextPuzzle.toString() in visited:
                        ind += 1
                        pq.put((parentCost+1,nextPuzzle))
                        visited[nextPuzzle.toString()] = ind
                        parent[ind] = pid
                        map[ind]=nextPuzzle


                        if(nextPuzzle.toString()==ans):
                            path = ind
                            while(path!=-1):
                                sol.insert(0,nextPuzzle.grid)
                                path = parent[path]
                                if(path==-1):
                                    break
                                nextPuzzle = map[path]
                            return sol,visited
        return False


class GBFS:

    def start(self,puzzle):

        queue = []
        visited = {}
        map = {}
        parent = {}
        ind =0
        pq = PriorityQueue()

        pq.put((puzzle.displacementDistance(),puzzle))
        parent[ind] = -1
        map[ind] = puzzle
        visited[puzzle.toString()] = 0

        ans = puzzle.goalState()

        sol = []
        if (puzzle.toString() == ans):
            sol.insert(0, puzzle.grid)
            return sol

        while(pq.not_empty):
            temp = pq.get()
            curPuzzle =  temp[1]
            parentCost = temp[0]
            pid = visited[curPuzzle.toString()]
            for i in range(4):
                if (i == 0):
                    nextPuzzle = curPuzzle.left()
                elif (i == 1):
                    nextPuzzle = curPuzzle.up()
                elif (i == 2):
                    nextPuzzle = curPuzzle.right()
                elif (i == 3):
                    nextPuzzle = curPuzzle.down()
                if(nextPuzzle!=False and nextPuzzle!=None):
                    if not nextPuzzle.toString() in visited:
                        ind += 1
                        pq.put((nextPuzzle.displacementDistance(),nextPuzzle))
                        visited[nextPuzzle.toString()] = ind
                        parent[ind] = pid
                        map[ind]=nextPuzzle


                        if(nextPuzzle.toString()==ans):
                            path = ind
                            while(path!=-1):
                                sol.insert(0,nextPuzzle.grid)
                                path = parent[path]
                                if(path==-1):
                                    break
                                nextPuzzle = map[path]
                            return sol,visited
        return False


class ASTAR:

    def start(self,puzzle):
        queue = []
        visited = {}
        map = {}
        parent = {}
        ind =0
        pq = PriorityQueue()

        pq.put((puzzle.displacementDistance(),puzzle))
        parent[ind] = -1
        map[ind] = puzzle
        visited[puzzle.toString()] = 0


        ans = puzzle.goalState()

        sol = []
        if (puzzle.toString() == ans):
            sol.insert(0, puzzle.grid)
            return sol


        while pq:
            temp = pq.get()
            curPuzzle =  temp[1]
            parentCost = temp[0]
            pid = visited[curPuzzle.toString()]
            for i in range(4):
                if (i == 0):
                    nextPuzzle = curPuzzle.left()
                elif (i == 1):
                    nextPuzzle = curPuzzle.up()
                elif (i == 2):
                    nextPuzzle = curPuzzle.right()
                elif (i == 3):
                    nextPuzzle = curPuzzle.down()
                if(nextPuzzle!=False and nextPuzzle!=None):
                    if not nextPuzzle.toString() in visited:
                        ind += 1
                        pq.put((nextPuzzle.displacementDistance()+parentCost,nextPuzzle))
                        visited[nextPuzzle.toString()] = ind
                        parent[ind] = pid
                        map[ind]=nextPuzzle


                        if(nextPuzzle.toString()==ans):
                            path = ind
                            while(path!=-1):
                                sol.insert(0,nextPuzzle.grid)
                                path = parent[path]
                                if(path==-1):
                                    break
                                nextPuzzle = map[path]
                            return sol,visited
        return False



class DLS:
    ind=0
    visited = {}
    map = {}
    goal = ""
    parent = {}
    def recursion(self,curPuzzle,limit):

        if(curPuzzle.toString()==self.goal):
            answer = []
            path = self.visited[(curPuzzle.toString(),limit)]
            while path != -1 :
                answer.insert(0,curPuzzle.grid)
                path = self.parent[path]
                if path != -1:
                    curPuzzle = self.map[path]
            return answer

        elif limit==-1:
            return False
        else:
            limitCrossed = False
            for i in range(4):
                if (i == 0):
                    nextPuzzle = curPuzzle.left()
                elif (i == 1):
                    nextPuzzle = curPuzzle.up()
                elif (i == 2):
                    nextPuzzle = curPuzzle.right()
                elif (i == 3):
                    nextPuzzle = curPuzzle.down()
                if(nextPuzzle!=False and (nextPuzzle.toString(),limit-1) not in self.visited):
                    self.visited[(nextPuzzle.toString(),limit-1)] = self.ind
                    self.map[self.ind] = nextPuzzle
                    self.parent[self.ind] = self.visited[(curPuzzle.toString(),limit)]
                    self.ind += 1
                    ret = self.recursion(nextPuzzle,limit-1)
                    if(ret!=False):
                        return ret

            return False



    def start(self,puzzle,limit):
        self.ind = 0
        self.parent.clear()
        self.visited.clear()
        self.map.clear()
        self.goal = puzzle.goalState()
        limit-=1
        self.visited[(puzzle.toString(),limit)] = self.ind
        self.map[self.ind] = puzzle
        self.parent[self.ind] = -1
        self.ind+=1
        anst = self.recursion(puzzle,limit)
        return anst




class IDS:
    ind=0
    visited = {}
    map = {}
    goal = ""
    cutoff=0
    parent = {}

    def recursion(self, curPuzzle, limit):

        if (curPuzzle.toString() == self.goal):
            answer = []
            path = self.visited[(curPuzzle.toString(), limit)]
            while path != -1:
                answer.insert(0, curPuzzle.grid)
                path = self.parent[path]
                if path != -1:
                    curPuzzle = self.map[path]
            return answer

        elif limit == -1:
            self.cutoff=1
            return False
        else:
            limitCrossed = False
            for i in range(4):
                if (i == 0):
                    nextPuzzle = curPuzzle.left()
                elif (i == 1):
                    nextPuzzle = curPuzzle.up()
                elif (i == 2):
                    nextPuzzle = curPuzzle.right()
                elif (i == 3):
                    nextPuzzle = curPuzzle.down()
                if (nextPuzzle != False and (nextPuzzle.toString(), limit - 1) not in self.visited):
                    self.visited[(nextPuzzle.toString(), limit - 1)] = self.ind
                    self.map[self.ind] = nextPuzzle
                    self.parent[self.ind] = self.visited[(curPuzzle.toString(), limit)]
                    self.ind += 1
                    ret = self.recursion(nextPuzzle, limit - 1)
                    if (ret != False):
                        return ret

            return False



    def start(self,puzzle):

        self.goal =""
        self.goal = puzzle.goalState()
        limit=0
        while(True):
            self.ind=0
            self.parent.clear()
            self.visited.clear()
            self.map.clear()

            self.cutoff=0
            self.visited[(puzzle.toString(),limit)] = self.ind
            self.map[self.ind] = puzzle
            self.parent[self.ind] = -1
            self.ind+=1
            ans =  self.recursion(puzzle,limit)
            if(ans!=False):
                return ans
            else:
                if(self.cutoff==1):
                    limit+=1
                else:
                    return False
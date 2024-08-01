import puzzle as pz
import algo
import time
import numpy as np
import matplotlib.pyplot as plt

while(True):
    print("Select from the options below:\n1.Online mode\n2.Offline mode\n3.Exit\n")
    option = input()
    if(option=="1"):
        newPuzzle = pz.puzzle(1,0)
        print("Select which algorithm to run:\n1.BFS\n2.UCS\n3.GBFS\n4.A*\n5.DLS\n6.IDS\nChoice:\n")
        algoChoice = input()

        if(algoChoice=="1"):
            print("Running BFS......")
            start = time.time()
            running = algo.BFS()
            answer,visited = running.start(newPuzzle)
            end = time.time()
            total = end-start
            print("Running time: ",total)
            if(answer==False):
                print("No solution found\n")
            else:
                print("Steps taken ",len(answer)-1)
                st=0
                for abox in answer:
                    print("----------------------")
                    print("Step ",st)
                    st+=1
                    for bbox in abox:
                        print(bbox, "\n")

        elif (algoChoice == "2"):
            print("Running UCS......")
            start = time.time()
            running = algo.UCS()
            answer,visited = running.start(newPuzzle)
            end = time.time()
            total = end - start
            print("Running time: ", total)
            if (answer == False):
                print("No solution found\n")
            else:
                print("Steps taken ", len(answer) - 1)
                st = 0
                for abox in answer:
                    print("----------------------")
                    print("Step ", st)
                    st += 1
                    for bbox in abox:
                        print(bbox, "\n")

        elif (algoChoice == "3"):
            print("Running GBFS......")
            start = time.time()
            running = algo.GBFS()
            answer,visited = running.start(newPuzzle)
            end = time.time()
            total = end - start
            print("Running time: ", total)
            if (answer == False):
                print("No solution found\n")
            else:
                print("Steps taken ", len(answer) - 1)
                st = 0
                for abox in answer:
                    print("----------------------")
                    print("Step ", st)
                    st += 1
                    for bbox in abox:
                        print(bbox, "\n")

        elif (algoChoice == "4"):
            print("Running A*......")
            start = time.time()
            running = algo.ASTAR()
            answer,visited = running.start(newPuzzle)
            end = time.time()
            total = end - start
            print("Running time: ", total)
            if (answer == False):
                print("No solution found\n")
            else:
                print("Steps taken ", len(answer) - 1)
                st = 0
                for abox in answer:
                    print("----------------------")
                    print("Step ", st)
                    st += 1
                    for bbox in abox:
                        print(bbox, "\n")

        elif (algoChoice == "5"):
            print("Running DLS......")
            start = time.time()
            running = algo.DLS()
            answer = running.start(newPuzzle,20)
            end = time.time()
            total = end - start
            print("Running time: ", total)
            if (answer == False):
                print("No solution found\n")
            else:
                print("Steps taken ", len(answer) - 1)
                st = 0
                for abox in answer:
                    print("----------------------")
                    print("Step ", st)
                    st += 1
                    for bbox in abox:
                        print(bbox, "\n")

        elif (algoChoice == "6"):
            print("Running IDS......")
            start = time.time()
            running = algo.IDS()
            answer = running.start(newPuzzle)
            end = time.time()
            total = end - start
            print("Running time: ", total)
            if (answer == False):
                print("No solution found\n")
            else:
                print("Steps taken ", len(answer) - 1)
                st = 0
                for abox in answer:
                    print("----------------------")
                    print("Step ", st)
                    st += 1
                    for bbox in abox:
                        print(bbox, "\n")
        else:
            print("Wrong option selected.Try again\n\n")

    elif option=="2":
        timeData = []
        nodeData = []
        stepData = []
        for i in range(6):
            timeData.append([0.0] * 20)
            nodeData.append([0.0] * 20)
            stepData.append([0.0] * 20)

        for i in range(1,21):
            newPuzzle = pz.puzzle(2,i)
            #print(boxy.box)

            print("BFS_",i)
            start = time.time()
            answer = algo.BFS()
            ans,visited = answer.start(newPuzzle)
            finish = time.time() - start
            timeData[0][i-1] = finish
            nodeData[0][i-1] = len(visited)
            stepData[0][i-1] = len(ans) - 1

            print("UCS_",i)
            start = time.time()
            answer = algo.UCS()
            ans,visited = answer.start(newPuzzle)
            finish = time.time() - start
            timeData[1][i-1] = finish
            nodeData[1][i-1] = len(visited)
            stepData[1][i-1] = len(ans) - 1

            print("GBFS_",i)
            start = time.time()
            answer = algo.GBFS()
            ans,visited = answer.start(newPuzzle)
            finish = time.time() - start
            timeData[2][i-1] = finish
            nodeData[2][i-1] = len(visited)
            stepData[2][i-1] = len(ans) - 1

            print("A*_",i)
            start = time.time()
            answer = algo.ASTAR()
            ans,visited = answer.start(newPuzzle)
            finish = time.time() - start
            timeData[3][i-1] = finish
            nodeData[3][i-1] = len(visited)
            stepData[3][i-1] = len(ans) - 1

            print("DLS_", i)
            start = time.time()
            answer = algo.DLS()
            ans = answer.start(newPuzzle, 20)
            finish = time.time() - start
            timeData[4][i - 1] = finish
            nodeData[4][i - 1] = len(answer.visited)
            stepData[4][i - 1] = len(ans) - 1

            print("IDS_", i)
            start = time.time()
            answer = algo.IDS()
            ans = answer.start(newPuzzle)
            finish = time.time() - start
            timeData[5][i - 1] = finish
            nodeData[5][i - 1] = len(answer.visited)
            stepData[5][i - 1] = len(ans) - 1

        print(timeData)
        print(nodeData)
        print(stepData)
        xaxis = np.arange(1,21)
        plt.plot(xaxis,timeData[0], linestyle = '-', label = "BFS")
        plt.plot(xaxis,timeData[1], linestyle = '-', label = "UCS")
        plt.plot(xaxis,timeData[2], linestyle = '-', label = "GBFS")
        plt.plot(xaxis,timeData[3], linestyle = '-', label = "A*")
        plt.plot(xaxis,timeData[4], linestyle = '-', label = "DLS")
        plt.plot(xaxis,timeData[5], linestyle = '-', label = "IDS")
        plt.grid()
        plt.legend()
        plt.title("Time Data")
        plt.show()

        xaxis = np.arange(1,21)
        plt.plot(xaxis,nodeData[0], linestyle = '-', label = "BFS")
        plt.plot(xaxis,nodeData[1], linestyle = '-', label = "UCS")
        plt.plot(xaxis,nodeData[2], linestyle = '-', label = "GBFS")
        plt.plot(xaxis,nodeData[3], linestyle = '-', label = "A*")
        plt.plot(xaxis,nodeData[4], linestyle = '-', label = "DLS")
        plt.plot(xaxis,nodeData[5], linestyle = '-', label = "IDS")
        plt.grid()
        plt.legend()
        plt.title("Node Data")
        plt.show()

        xaxis = np.arange(1,21)
        plt.plot(xaxis,stepData[0], linestyle = '-', label = "BFS")
        plt.plot(xaxis,stepData[1], linestyle = '-', label = "UCS")
        plt.plot(xaxis,stepData[2], linestyle = '-', label = "GBFS")
        plt.plot(xaxis,stepData[3], linestyle = '-', label = "A*")
        plt.plot(xaxis,stepData[4], linestyle = '-', label = "DLS")
        plt.plot(xaxis,stepData[5], linestyle = '-', label = "IDS")
        plt.grid()
        plt.legend()
        plt.title("Step Data")
        plt.show()
        

    elif option=="3":
        break

    else:
        print("Wrong option selected.Try again\n\n")

import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import os.path
import operator

def getNum(text):
    return int(''.join(ele for ele in text if ele.isdigit() or ele == '.'))

def findLargestNumber(text):
    ls = list()
    for w in text.split():
        try:
            ls.append(int(w))
        except:
            pass
    try:
        return max(ls)
    except:
        return None

def openFile():

    filename = askopenfilename(parent=root)
    extension = os.path.splitext(filename)[1][1:]

    if extension == '':
        messagebox.showinfo("Error", "No file chosen, please click on a valid test file")

    else:
        with open(filename) as f:
            content = f.readlines()

        content = [x.strip() for x in content]
        totalnodes = getNum(content[3])
        system = buildCoords(content,totalnodes)
        heuritic(system)


def getGridSize(content):

    #print('Raj')
    flag = False
    i = 0
    k = len(content)
    largestnumberArray = []

    while not flag:
        while i < k:

            if content[i] == 'EOF':
                flag = True

            if content[i][0].isdigit():
                largestnumber = findLargestNumber(content[i])
                largestnumberArray.append(largestnumber)
                i += 1

            else:
                i += 1

        largestCoordinate = max(largestnumberArray)

    x = 0

    if largestCoordinate < 10000:
        x = 10000

    if largestCoordinate < 1000:
        x = 1000

    if largestCoordinate > 100:
        x = 100

    return x

def createGrid():

    x = [['.' for i in range(getGridSize())] for j in range(getGridSize())]
    return x

def buildCoords(content,totalnodes):
    system = []
    #print(content[6])
    #print(totalnodes)
    #x=content[7].split()
    #system.append(x)
    #print(system)

    i = 0
    while i < totalnodes:
        x=content[7+i].split()
        #print(x)
        system.append(x)
        i += 1

    k = getDemand(content)

    #print(k)
    #print(content[k])

    k += 1

    i = 0
    while i < totalnodes:
        x=content[k+i].split()
        #print(x[1])
        system[i].append(x[1])
        i += 1

    #print(system)

    return system

    #print(x)
    #print(x[0])
    #print(x[1])


def getDemand(content):
    i = 0
    k = len(content)
    while i < k:
        if content[i] == "DEMAND_SECTION":
            return  i
        i += 1

def heuritic(system):
    depotX = system[0][1]
    depotY = system[0][2]
    #print(depotX)
    #print(depotY)

    k = len(system)
    #print(k)

    i = 1

    routes = []
    #x = [0,1,0]
    #routes.append(x)


    while i <= k:

        x = [0,i,0]
        routes.append(x)

        i += 1

    print(routes)

    savings = []

    i = 1
    while i <= k:

        j = i+1

        while j < k:
            #print('i: ' + str(i) + ' j: ' + str(j))
            nodeix = system[i][1]
            nodeiy = system[i][2]
            nodejx = system[j][1]
            nodejy = system[j][2]

            d1 = calcDist(depotX,depotY,nodeix,nodeiy)
            d2 = calcDist(depotX,depotY,nodejx,nodejy)
            d3 = calcDist(nodeix,nodeiy,nodejx,nodejy)

            #print(d1)
            #print(d2)
            #print(d3)

            savingscalc = int(d1) + int(d2) - int(d3)
            x = [i,j,savingscalc]
            savings.append(x)
            j += 1
        i += 1

    #print(savings)
    #sorted(savings, key=operator.itemgetter(2), reverse=True)
    savings.sort(key=operator.itemgetter(2),reverse=True)
    print(savings)
    #calcDist(depotX,depotY,system[1][1],system[1][2])

    capacity = 15

    i = 0
    #while i <= k:








def calcDist(x1,y1,x2,y2):
    calc1 = int(x1) - int(x2)
    calc2 = int(y1) - int(y2)
    calc = calc1**2 + calc2**2
    calc = calc**0.5
    #print(calc)
    return calc





root = Tk()
b = Button(root, text="Open VRP File", command=openFile)
b.pack()
root.mainloop()
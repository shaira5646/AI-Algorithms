# -*- coding: utf-8 -*-
"""8_20101261_ShairaChowdhury.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_mqqrZbU7e0GdByyG2EiSanUJb1x2fZS
"""

#### A* SEARCH ####

from google.colab import drive 
from queue import PriorityQueue

### PRIORITY QUEUE ###

fringe = PriorityQueue()


def a_star_search(start,dest,hVal,treeMap):
  fnVal = 0
  gnVal = 0
  distance = 0
  path = []
  flag = True
  visited = []
  fringe.put((hVal[start],start,[start]))     ### Put A in priorityQ
  while flag:
    pop = fringe.get()
    path = pop[2]              #### PATH A->
    distance = pop[0]- hVal[pop[1]]
    if pop[1] == dest:
      flag = False
    else:
      visited.append(pop[1])           ## A ->
      for i in treeMap[pop[1]]:        ### Putting children in priorityQ         
        if start == pop[1]:
          gnVal += i[1]
          fnVal = hVal[i[0]] + gnVal   ## Calculating F(n) = h(n)+g(n)
          path = path + [i[0]]
          fringe.put((fnVal,i[0],path))    #### putting node  in priority Q with f(n) value
          gnVal = 0
          path = pop[2]
        else:
          if i[1] in visited:
            continue
          else:
            gnVal=distance+i[1]
            fnVal = hVal[i[0]] + gnVal   ## Calculating F(n) = h(n)+g(n)
            path = path+[i[0]]
            fringe.put((fnVal,i[0],path))    #### putting visited path list in priority Q with f(n) value
            gnVal = 0
            path = pop[2]
    if fringe.empty():
      return "No PATH FOUND", False

  return path, distance


### INPUT FILE READING ####

def hashmap(fileVal):
  hVal = {}
  treeMap = {}
  for i in range(len(fileVal)):
    x = fileVal[i].split()
    hVal.update({x[0]:int(x[1])})
    treeMap.update({x[0]:[]})
    for j in range(3,len(x),2):
      treeMap[x[0]].append((x[j-1],int(x[j])))
  return hVal, treeMap


inputFile=open("/content/Input file.txt","r")

fileVal=inputFile.readlines()

hVal, treeMap = hashmap(fileVal)

inputFile.close()


start = input("Start Node: ")
dest = input("Destination: ")

#### check priority queue empty or not 

if start == dest:
  print("Path: ", start)
  print("Total distance:",0,"km")

else:
  path, trueCost = a_star_search(start,dest,hVal,treeMap)

  if trueCost == False:
    print("Path: ",path)
  
  else:
    print("Path: ", end = "")

    for i in range(len(path)):
      if path[i] == dest:
        print(path[i])
      else:
        print(path[i],end = " -> ")

    print("Total distance:",trueCost,"km")
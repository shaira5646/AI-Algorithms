# -*- coding: utf-8 -*-
"""8_20101261_ShairaChowdhury.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sBmDT8gRgPBckE4Rz6fOU7n53toTbBmL
"""

### SECOND ATTEMPT ###

import numpy
from numpy import random


## TAKING INPUT ##

inputFile=open("/content/Input.txt","r")

n = int(inputFile.readline())

register = {}

for i in range(n):
  x = inputFile.readline().split()
  register.update({i:x})

#print("register:", register)

inputFile.close()

### CREATING POPULATION of n randomly generated chromosomes #####
control = numpy.array([0]*n)
def populate(n,control):
  population = random.randint(2, size=(10,n))
  if control in population:
    population = population[~numpy.all(population == 0, axis=1)]

  #print("population:", population)
  return population

## FITNESS FUCTION ##

def fitness(dep,lend):
  return abs(dep - lend) 

## USING ONE POINT CROSSOVER FROM THE RANDOM INDEX ###

one_point = random.randint(1,n)

#print("Crossover from:",one_point)

def crossover(chromeA,chromeB,one_point):
  offA = numpy.concatenate((chromeA[0:one_point], chromeB[one_point:]))
  offB = numpy.concatenate((chromeB[0:one_point], chromeA[one_point:]))
  return [offA,offB]

## MUTATION ON RANDOM INDEX ##

def mutation(chrome):
  idx = random.randint(n)
  if chrome[idx] == 0:
    chrome[idx] = 1
  else:
    chrome[idx] = 0

  return chrome

result = 0 
flag = False

population = populate(n,control)

##### GENETIC ALGORITM #######
for run in range (0,5001,1):
  fitVal = []
  newOFF = numpy.array([0]*n)
  ## CALCULATING FITNESS OF EACH CHROMOSOME ##
  for i in population:
    lend = 0
    dep = 0
    for j in range(n):
      if i[j] == 1:
        x = int(register[j][1])
        if register[j][0] == "l":
          lend += x
        else:
          dep += x
    fitVal.append(fitness(dep,lend)) 
  
  ### checking for output ###
  if 0 in fitVal:
    for i in range(len(fitVal)):
      if fitVal[i] == 0:
        result = population[i]
        flag = True 
    break

  ### ELIMINATING THE WORST FITNESS ###
  #print(fitVal)
  parent1 = 0
  eli = min(fitVal)
  for i in range(0,len(fitVal),1):
    if fitVal[i] == eli:
      parent1 = population[i]
      fitVal.pop(i)
      break

  parent2 = 0
  eli = min(fitVal)
  for i in range(len(fitVal)):
    if fitVal[i] == eli:
      parent2 = population[i]
      fitVal.pop(i)
      break
  
  ### crossover ###
  off = crossover(parent1,parent2,one_point)
  newOFF = numpy.vstack((newOFF, off[0]))
  newOFF = numpy.vstack((newOFF, off[1]))
  newOFF = numpy.delete(newOFF, 0, axis = 0)

  #print("offspring:",newOFF)

  ### MUTATION ###
  
  for i in range(len(newOFF)):
    newOFF[i] = mutation(newOFF[i])


  ## GOAL TEST ##
  fitVal = []
  for i in newOFF:
    lend = 0
    dep = 0
    for j in range(n):
      if i[j] == 1:
        x = int(register[j][1])
        if register[j][0] == "l":
          lend += x
        else:
          dep += x
    fitVal.append(fitness(dep,lend)) 

  ### checking for output ###
  if 0 in fitVal and control not in newOFF:
    for i in range(len(fitVal)):
      if fitVal[i] == 0:
        result = newOFF[i]
        flag = True
    break
  
  population = populate(n,control)

if flag == False:
  print(-1)
else:
  for i in result:
    print(i,end = "")
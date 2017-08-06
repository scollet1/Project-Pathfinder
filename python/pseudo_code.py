# The only thing this code and I have in common is that neither of us run

import dependencies such as numpy, math, $LIBRAIRIES
import keras
import numpy as numpy
import math
import random

# ~GLOBALS~ #

EXPLORATION = "e-greedy"
EPISODES = 5000 # large enough to converge, small enough that it doesn't take years
LEARNING_RATE = some num between [0.0000, 0.0004] # we can play around with this though
MEMORY = large value # where we're going to store our long-short-term memory 
BATCH_SIZE = 64 # how many nodes do we have??? [64 ~ 128]
GAMMA = 0.95 # this discounts the reward by diminishing returns over time [0, 1]
LAMBDA = 0.99
EPSILON_MAX = 0.99 #this is for a greedy epsilon problem to determine what actions we search for [0, 1]
EPSILON_MIN = 0.01

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

class Brain:
  def __init__(some params)
    initialize
   
  def train(some params)
    stuff
   
  def predict()
    if goal:
      do something
    else:
      do the otherthing
  
  def update()????????????
  
  def memory()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
  
class Robot:
  steps = 0
  epsilon = EPSILON_MAX
  
  def __init__(params)
    initialize
  
  def act() #roll the dice for a move
    if random.random() < epsilon
      return random action
    else
      return optimal action # action = argmax Q(s, a')
  
  def observe()
    observe that reward
    
  def learn() #learning fun

  def loss(target, prediction)
    err = prediction - target
    loss =  keras.mean(keras.sqrt(1 + keras.square(error)) - 1)
    return (loss)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
  
class Domain: #our simulated world
  
  def __init__(params)
    init map
    
  def run(robot, agents)
    while True:
      action = robot.act
      reward(action)
      robot.observe(reward)
      robot.learn

  def reward(action)
    scan map

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    
class Agents:
  
  def __init__(params)
   
  def pathfinding(params)
  
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
 
agents = agents
robot = robot
domain = Domain

for e in range(EPISODES):
  domain.run(robot, agents)
  

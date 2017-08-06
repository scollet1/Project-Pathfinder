# The only thing this code and I have in common is that neither of us run

# import dependencies such as numpy, math, $LIBRAIRIES
import keras
import numpy as numpy
import math
import random
from collections import deque

# ~GLOBALS~ #

EXPLORATION = "e-greedy"
ACTIONS = 5
EPISODES = 5000 # large enough to converge, small enough that it doesn't take years
LEARNING_RATE = 0.0002 # some num between [0.0001, 0.0004] we can play around with this though
MEMORY = large value # where we're going to store our long-short-term memory 
BATCH_SIZE = 64 # how many nodes do we have??? [64 ~ 128]
GAMMA = 0.95 # this discounts the reward by diminishing returns over time [0, 1]
LAMBDA = 0.99 # a rate of change in epsilon
EPSILON_MAX = 0.99 # this is for a greedy epsilon problem to determine what actions we search for [0, 1]
EPSILON_MIN = 0.01 # this is the target epsilon value as be begin to narrow down our policy

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
  
  def __init__(self, action_size)
    initialize
  
  def act(state) #roll the dice for a move
    if random.random() < epsilon
      return random action
    else
      return optimal action # action = argmax Q(s, a')
  
  def observe()
    observe that reward
  
  def remember()
  
  def learn() #learning fun

  	def loss(target, prediction)
    		err = prediction - target
    		loss =  keras.mean(keras.sqrt(1 + keras.square(error)) - 1)
    		return (loss)

  	def _build_model(self):
     		model = Sequential()
     		model.add(Dense(24, input_dim=self.state_size, activation='relu'))
    	 	model.add(Dense(24, activation='relu'))
     		model.add(Dense(self.action_size, activation='linear'))
     		model.compile(loss=self._huber_loss, optimizer=Adam(lr=self.learning_rate))
     		return model

	def load(self, name):
		self.model.load_weights(name)

	def save(self, name):
		self.model.save_weights(name)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
  
class Domain: #our simulated world
  
  def __init__(params):
    
    init map

  def state: # this method returns all information about our current state
    state = [17][17] # some 17 * 17 array of values from [0, 1]
    return state
    
  def reward(action):
    scan map
    
  def reset():
    return (self.state())

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    
class Agents:
  
  def __init__(params)
   
  def pathfinding(params)
  
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

if __name__ == "__main__":
  agents = agents
  robot = robot
  domain = gym.make('Custom-Domain')
  state_size = domain.state_size

  for e in range(EPISODES):
    state = domain.reset()
    state = numpy.reshape(state, [1, state_size])
    for time in range(500)
      action = robot.act(state)
      reward = reward if not done else -10
      robot.remember(state action, reward, next_state, done)
      state = next_state
      if done:
        robot.update_target_model()
        print("episode: {}/{}, score: {}, e: {:2}".format(e, EPISODES, time, agent.epsilon))
				break
    if len(robot.memory) > batch_size
      robot.replay(batch_size)

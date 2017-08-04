# The only thing this code and I have in common is that neither of us runs

import dependencies such as numpy, math, $LIBRAIRIES

define loss value = some num
learning rate = some num between [0.0000, 0.0004] #we can play around with this though
memory = large value
batch size = how many nodes do we have??? [64, ~ 100] is a good range
gamma = this modifies the reward by diminishing returns over time [0, 1]
lambda = rate of decay
epsilon = this is for a greedy epsilon problem to determine what actions we search for [0, 1]

def loss function()
  err = 
  ~ magic ~
  return (loss)
  
class Brain:
  def init(some params)
    initialize
   
  def train(some params)
    stuff
   
  def predict()
    if goal:
      do something
    else:
      do the otherthing
  
  def update()????????????
  
class Robot
  steps = 
  epsilon = 
  
  def init(params)
    initialize
  
  def action() #roll the dice for a move
    if random.random() < epsilon
      return thing
    else
      return other thing
  
  def observe()

  def learn() #learning fun

class Domain #our simulated world
  
  def init(params)
   
  def run
    while True:
      act
      observe
      learn
      
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
 
agents = agents
robot = robot
domain = domain

while True:
  domain.run(robot, agents)
  

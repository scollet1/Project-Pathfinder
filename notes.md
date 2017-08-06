# Steps
-------

1. initialize memory
2. initialize action_value function Q with random weights
3. observe initial state s

4. while(True)
   1. select action a
      1. with probability epsilon select random action
      2. otherwise elect a = argmax Q(s, a')
   2. carry out action a
   3. observe reward r and new state s'
   4. store experience <s, a, r, s'> in memory
  
   5. sample random transitions <ss, aa, rr, ss'> from memory
   6. calculate target for each minibatch transition
      1. if ss' is terminal state then tt = rr
      2. otherwise tt = rr + gmax Q(ss', aa')
   7. if robot has not updated location after 10 turns
      1. then restart the simulation

# Defining the MDP
------------------

  S is an infinite set of states

  A is a finite set of actions
    - A 2d list of possible movement actions. A vector to navigate

  P_a(s, s') is the probability that action a in state s at time t will lead to s' at t + 1
    - traversing the list of possible S and possible A
    
  R_a(s, s') is the immediate reward received after transitioning from state s to state s' due to action a

  g is an element of [0, 1] otherwise known as the discount factor
    - for each step in time, rewards farthest from the agent are diminished

  π(s) := ∑ P_π(s) • (s, s')(R_π(s) • (s, s') + gV(s'))
          s'
          
# Constructing a Custom Environment
-----------------------------------

https://github.com/openai/gym/tree/master/gym/envs

Basically, we can define an environment package to feed into the OpenAI gym dependency

# Algorithms
------------

## below is an algorithm for constructing a custom neural network
  
```python
  def createNetwork():
    # network weights
    W_conv1 = weight_variable([8, 8, 4, 32])
    b_conv1 = bias_variable([32])

    W_conv2 = weight_variable([4, 4, 32, 64])
    b_conv2 = bias_variable([64])

    W_conv3 = weight_variable([3, 3, 64, 64])
    b_conv3 = bias_variable([64])

    W_fc1 = weight_variable([1600, 512])
    b_fc1 = bias_variable([512])

    W_fc2 = weight_variable([512, ACTIONS])
    b_fc2 = bias_variable([ACTIONS])

    # input layer
    s = tf.placeholder("float", [None, 80, 80, 4])

    # hidden layers
    h_conv1 = tf.nn.relu(conv2d(s, W_conv1, 4) + b_conv1)
    h_pool1 = max_pool_2x2(h_conv1)

    h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2, 2) + b_conv2)
    # h_pool2 = max_pool_2x2(h_conv2)

    h_conv3 = tf.nn.relu(conv2d(h_conv2, W_conv3, 1) + b_conv3)
    # h_pool3 = max_pool_2x2(h_conv3)

    # h_pool3_flat = tf.reshape(h_pool3, [-1, 256])
    h_conv3_flat = tf.reshape(h_conv3, [-1, 1600])

    h_fc1 = tf.nn.relu(tf.matmul(h_conv3_flat, W_fc1) + b_fc1)

    # readout layer
    readout = tf.matmul(h_fc1, W_fc2) + b_fc2

    return s, readout, h_fc1
```




## below is an aglorithm for action selection

  ```python
  if random.random() <= epsilon:
    print("----------Random Action----------")
    action_index = random.randrange(ACTIONS)
    a_t[random.randrange(ACTIONS)] = 1
  else:
    action_index = np.argmax(readout_t)
    a_t[action_index] = 1
  ```

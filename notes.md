# Steps

- initialize memory
- initialize action_value function Q with random weights
- observe initial state s

- while(True)
  - select action a 
    - with probability epsilon select random action
    - otherwise elect a = argmax Q(s, a')
  - carry out action a
  - observe reward r and new state s'
  - store experience <s, a, r, s'> in memory
  
  - sample random transitions <ss, aa, rr, ss'> from memory
  - calculate target for each minibatch transition
    - if ss' is terminal state then tt = rr
    - otherwise tt = rr + gmax Q(ss', aa')
  - if robot has not updated location after 10 turns
    - then restart the simulation
  
# Defining the MDP

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

# algorithms

## below is an algorithm for constructing a custom neural network

  def createNetwork():
  //network weights
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

    //input layer
    s = tf.placeholder("float", [None, 80, 80, 4])

    // hidden layers
    h_conv1 = tf.nn.relu(conv2d(s, W_conv1, 4) + b_conv1)
    h_pool1 = max_pool_2x2(h_conv1)

    h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2, 2) + b_conv2)
    // h_pool2 = max_pool_2x2(h_conv2)

    h_conv3 = tf.nn.relu(conv2d(h_conv2, W_conv3, 1) + b_conv3)
    // h_pool3 = max_pool_2x2(h_conv3)

    // h_pool3_flat = tf.reshape(h_pool3, [-1, 256])
    h_conv3_flat = tf.reshape(h_conv3, [-1, 1600])

    h_fc1 = tf.nn.relu(tf.matmul(h_conv3_flat, W_fc1) + b_fc1)

    // readout layer
    readout = tf.matmul(h_fc1, W_fc2) + b_fc2

    return s, readout, h_fc1

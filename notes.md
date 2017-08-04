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
  
# Defining the MDP

  S is a finite set of states
    A 2d list of possible spaces to move into. This is defined by local (x, y) coordinates, relative to the agent

  A is a finite set of actions
    A 2d list of possible movement actions. A vector to navigate and a negative or positive 1

  P_a(s, s') is the probability that action a in state s at time t will lead to s' at t + 1
    traversing the list of possible S and possible A
      if (x, y) are not occupied at s'
        then the probability of moving to, and existing in, that state is high
      else if (x, y) are occupied at s'
        then the probability of moving to, and existing in, that state is low

  R_a(s, s') is the immediate reward received after transitioning from state s to state s' due to action a
    for each step closer to s_END, a reward is given
    for each step farther from s_END, a reward is taken away

  g is an element of [0, 1] otherwise known as the discount factor
    for each step in time, rewards farthest from the agent are diminished

  π(s) := ∑ P_π(s) • (s, s')(R_π(s) • (s, s') + gV(s'))
          s'

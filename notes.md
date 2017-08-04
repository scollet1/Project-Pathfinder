# Steps

initialize memory
initialize action_value function Q with random weights
observe initial state s

while(True)
  select action a
    with probability epsilon select random action
    otherwise elect a = argmax Q(s, a')
  carry out action a
  observe reward r and new state s'
  store experience <s, a, r, s'> in memory
  
  sample random transitions <ss, aa, rr, ss'> from memory
  calculate target for each minibatch transition
    if ss' is terminal state then tt = rr
    otherwise tt = rr + gmax Q(ss', aa')
  

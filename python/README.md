# TODO 
  - [ ] MVP <--- 
  - [ ] project <--- 
    - [ ] Algorithm Converges
  - [ ] bonsuses! <--- 
    - [ ] A3C Network distributed across the NFS
  
### functions
  - [ ] Reward
  - [ ] Loss
  - [ ] Update
  - [ ] Learn

### object classes - referring to all objects in the simulation
  - [ ] construct robot
    - [ ] robot AI
  - [ ] construct agents
    - [ ] agents' AI - The AI is rudimentary; each agent has a starting location and a goal; they will navigate the domain until they reach their goal or until a number of time steps have passed without them moving (i.e they can never reach their goal); if they have stopped moving for long enough time, they will stop moving for the rest of the simulation (i.e sitting down)
  - [ ] construct domain
    - [ ] map domain to a data structure - This is a data-agnostic structure starting at [100][100] and scaling by [HEIGHT][WIDTH]; each space should be initilized by calculating density and supplying a value [0, 1] where 0 is empty and 1 is an agent; the robot should be denoted by a 2 and should be spawned first. 

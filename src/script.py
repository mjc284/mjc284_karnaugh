import numpy as np
import states_parser as sp

states = np.array([[0, 1], [1, 2], [2, 0]])
parsed = sp.parse(states)

for line in parsed:
    print(line)
    

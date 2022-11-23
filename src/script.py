import numpy as np
import states_parser as sp
import karnaugh as kn

states = np.array([[0, 1], [1, 2], [2, 0]])
parsed = sp.parse(states)

processed = kn.map(parsed)
print(processed)

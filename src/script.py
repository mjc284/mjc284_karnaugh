import numpy as np
import states_parser as sp
import karnaugh as kn

states = np.array([[0, 1], [1, 2], [2, 0]])
states = np.array([[1, 1, 1, 3], [2, 2, 2, 2], [4, 4, 4, 4], [4, 4, 4, 4], [0, 0, 0, 0]])

parsed = [[['A', 'B', 'C', 'D'], ['O']],
[[0, 0, 0, 0], [0]],
[[0, 0, 0, 1], [0]],
[[0, 0, 1, 0], [1]],
[[0, 0, 1, 1], [1]],
[[0, 1, 0, 0], [0]],
[[0, 1, 0, 1], [1]],
[[0, 1, 1, 0], [0]],
[[0, 1, 1, 1], [1]],
[[1, 0, 0, 0], [1]],
[[1, 0, 0, 1], [0]],
[[1, 0, 1, 0], [0]],
[[1, 0, 1, 1], [0]],
[[1, 1, 0, 0], [0]],
[[1, 1, 0, 1], [1]],
[[1, 1, 1, 0], [0]],
[[1, 1, 1, 1], [1]]]

parsed = sp.parse(states)
sp.present(parsed)

print("")

processed = kn.map(parsed)
kn.present(processed)

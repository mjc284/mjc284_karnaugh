# mjc284_karnaugh
Python scripts to help construct karnaugh maps, boolean expressions, and finite state machines.
Refer to script.py for examples of each functions.

## states_parser.py
Module for interpreting state diagram and generating truth tables for processing. 

### parse(states)
Function to parse states into table format for Karnaugh mapper to process. The "states" must be an array in the form of [[state 0], [state 1], ...] where each [state n] = [(next state when I0 = 0, I1 = 0, ... In = 0), (next state when I0 = 0, I1 = 0, ..., In = 1), ...].
Return: parsed table array.

### flipflop(table, flipflop_type)
Function to modify a parsed truth table to fit a given flip-flop type. The flipflop_type can take values of "SR", "JK", "D", or "T".
Return: modified table array.

### show(table)
Print the parsed truth table into a human-readable table in the console.

### Example

<details>
  <summary>Expand</summary>
  
Sample state diagram:
![State_Diagram](/photos/state_diagram.png "State_Diagram")

Input:
```
# Declare states:
states = [[1, 1, 1, 3], [2, 2, 2, 2], [4, 4, 4, 4], [4, 4, 4, 4], [0, 0, 0, 0]]

# Parse states into table format:
parsed = sp.parse(states)

# Print parsed states into human-readable table format:
print("Parsed states:\n")
sp.show(parsed)
print("\n")

# Parse states into flip-flop table format:
# sp.flipflop(parsed_table, flipflop_type) where flipflop_type = "JK"/"SR"/"D"/"T"
parsed = sp.flipflop(parsed, "JK")

# Print parsed flip-flop states into human-readable table format:
print("Parsed JK flip-flop states:\n")
sp.show(parsed)
print("\n")
```

Console Output:
```
Parsed states:

| A | B | C | I1| I2|| O1| O2| O3|
----------------------------------
| 0 | 0 | 0 | 0 | 0 || 0 | 0 | 1 |
| 0 | 0 | 0 | 0 | 1 || 0 | 0 | 1 |
| 0 | 0 | 0 | 1 | 0 || 0 | 0 | 1 |
| 0 | 0 | 0 | 1 | 1 || 0 | 1 | 1 |
| 0 | 0 | 1 | 0 | 0 || 0 | 1 | 0 |
| 0 | 0 | 1 | 0 | 1 || 0 | 1 | 0 |
| 0 | 0 | 1 | 1 | 0 || 0 | 1 | 0 |
| 0 | 0 | 1 | 1 | 1 || 0 | 1 | 0 |
| 0 | 1 | 0 | 0 | 0 || 1 | 0 | 0 |
| 0 | 1 | 0 | 0 | 1 || 1 | 0 | 0 |
| 0 | 1 | 0 | 1 | 0 || 1 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 || 1 | 0 | 0 |
| 0 | 1 | 1 | 0 | 0 || 1 | 0 | 0 |
| 0 | 1 | 1 | 0 | 1 || 1 | 0 | 0 |
| 0 | 1 | 1 | 1 | 0 || 1 | 0 | 0 |
| 0 | 1 | 1 | 1 | 1 || 1 | 0 | 0 |
| 1 | 0 | 0 | 0 | 0 || 0 | 0 | 0 |
| 1 | 0 | 0 | 0 | 1 || 0 | 0 | 0 |
| 1 | 0 | 0 | 1 | 0 || 0 | 0 | 0 |
| 1 | 0 | 0 | 1 | 1 || 0 | 0 | 0 |
| 1 | 0 | 1 | 0 | 0 || X | X | X |
| 1 | 0 | 1 | 0 | 1 || X | X | X |
| 1 | 0 | 1 | 1 | 0 || X | X | X |
| 1 | 0 | 1 | 1 | 1 || X | X | X |
| 1 | 1 | 0 | 0 | 0 || X | X | X |
| 1 | 1 | 0 | 0 | 1 || X | X | X |
| 1 | 1 | 0 | 1 | 0 || X | X | X |
| 1 | 1 | 0 | 1 | 1 || X | X | X |
| 1 | 1 | 1 | 0 | 0 || X | X | X |
| 1 | 1 | 1 | 0 | 1 || X | X | X |
| 1 | 1 | 1 | 1 | 0 || X | X | X |
| 1 | 1 | 1 | 1 | 1 || X | X | X |


Parsed JK flip-flop states:

| A | B | C | I1| I2|| Ja| Ka| Jb| Kb| Jc| Kc|
-----------------------------------------------
| 0 | 0 | 0 | 0 | 0 || 0 | X | 0 | X | 1 | X |
| 0 | 0 | 0 | 0 | 1 || 0 | X | 0 | X | 1 | X |
| 0 | 0 | 0 | 1 | 0 || 0 | X | 0 | X | 1 | X |
| 0 | 0 | 0 | 1 | 1 || 0 | X | 1 | X | 1 | X |
| 0 | 0 | 1 | 0 | 0 || 0 | X | 1 | X | X | 1 |
| 0 | 0 | 1 | 0 | 1 || 0 | X | 1 | X | X | 1 |
| 0 | 0 | 1 | 1 | 0 || 0 | X | 1 | X | X | 1 |
| 0 | 0 | 1 | 1 | 1 || 0 | X | 1 | X | X | 1 |
| 0 | 1 | 0 | 0 | 0 || 1 | X | X | 1 | 0 | X |
| 0 | 1 | 0 | 0 | 1 || 1 | X | X | 1 | 0 | X |
| 0 | 1 | 0 | 1 | 0 || 1 | X | X | 1 | 0 | X |
| 0 | 1 | 0 | 1 | 1 || 1 | X | X | 1 | 0 | X |
| 0 | 1 | 1 | 0 | 0 || 1 | X | X | 1 | X | 1 |
| 0 | 1 | 1 | 0 | 1 || 1 | X | X | 1 | X | 1 |
| 0 | 1 | 1 | 1 | 0 || 1 | X | X | 1 | X | 1 |
| 0 | 1 | 1 | 1 | 1 || 1 | X | X | 1 | X | 1 |
| 1 | 0 | 0 | 0 | 0 || X | 1 | 0 | X | 0 | X |
| 1 | 0 | 0 | 0 | 1 || X | 1 | 0 | X | 0 | X |
| 1 | 0 | 0 | 1 | 0 || X | 1 | 0 | X | 0 | X |
| 1 | 0 | 0 | 1 | 1 || X | 1 | 0 | X | 0 | X |
| 1 | 0 | 1 | 0 | 0 || X | X | X | X | X | X |
| 1 | 0 | 1 | 0 | 1 || X | X | X | X | X | X |
| 1 | 0 | 1 | 1 | 0 || X | X | X | X | X | X |
| 1 | 0 | 1 | 1 | 1 || X | X | X | X | X | X |
| 1 | 1 | 0 | 0 | 0 || X | X | X | X | X | X |
| 1 | 1 | 0 | 0 | 1 || X | X | X | X | X | X |
| 1 | 1 | 0 | 1 | 0 || X | X | X | X | X | X |
| 1 | 1 | 0 | 1 | 1 || X | X | X | X | X | X |
| 1 | 1 | 1 | 0 | 0 || X | X | X | X | X | X |
| 1 | 1 | 1 | 0 | 1 || X | X | X | X | X | X |
| 1 | 1 | 1 | 1 | 0 || X | X | X | X | X | X |
| 1 | 1 | 1 | 1 | 1 || X | X | X | X | X | X |



Output Equations:

Ja = B
Ka = 1
Jb = !A&I1&I2 | C
Kb = 1
Jc = !A&!B
Kc = 1
```
</details>

## karnaugh.py
Module for karnaugh mapping and outputting boolean equations for a given truth table.

### map(table)
Function to solve the karnaugh map of a given truth table. The truth table has to be a filled table (See fill(table)).
Return: mapped solution array.

#### Mapping algorithm:
The function solves the karnaugh map with the following recursion: identifying neighbors and merging, removing duplicates. For example, for the given truth table:

```
| A | B | C | D || O |
----------------------
| 0 | 0 | 0 | 0 || 0 |
| 0 | 0 | 0 | 1 || 0 |
| 0 | 0 | 1 | 0 || 0 |
| 0 | 0 | 1 | 1 || 0 |
| 0 | 1 | 0 | 0 || 0 |
| 0 | 1 | 0 | 1 || 1 |
| 0 | 1 | 1 | 0 || 0 |
| 0 | 1 | 1 | 1 || 1 |
| 1 | 0 | 0 | 0 || 0 |
| 1 | 0 | 0 | 1 || 0 |
| 1 | 0 | 1 | 0 || 0 |
| 1 | 0 | 1 | 1 || 0 |
| 1 | 1 | 0 | 0 || 0 |
| 1 | 1 | 0 | 1 || 1 |
| 1 | 1 | 1 | 0 || 0 |
| 1 | 1 | 1 | 1 || 1 |

```

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
```
</details>

## karnaugh.py
Module for karnaugh mapping and print boolean equations for a given truth table in a console.

### map(table)
Function to solve the karnaugh map of a given truth table. The truth table has to be a filled table (See fill(table)).
Return: mapped solution array.

#### Mapping algorithm:
<details>
  <summary>Expand</summary>
  
  The function solves the karnaugh map with the following recursion: identifying neighbors and merging, removing duplicates. 
  For example, for the given truth table:

```
| A | B | C | D || O |
----------------------
| 0 | 0 | 0 | 0 ||'X'|
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
1. Extract 1s or Xs:
  
  ```
  [[[0, 0, 0, 0], ['X']], [[0, 1, 0, 1], [1]], [[0, 1, 1, 1], [1]], [[1, 1, 0, 1], [1]], [[1, 1, 1, 1], [1]]]
  ```

2. Identify and merge neighbors:
  
  ```
  [[[0, 0, 0, 0], ['X']], [[0, 1, 'X', 1], [1]], [['X', 1, 0, 1], [1]], [['X', 1, 1, 1], [1]], [[1, 1, 'X', 1], [1]]]
  ```
  
3. Remove duplicates: (none)
  
4. Identify and merge neighbors:
  
  ```
  [[[0, 0, 0, 0], ['X']], [['X, 1, 'X', 1], [1]], [['X', 1, 'X', 1], [1]]]
  ```
5. Remove duplicates:
  
  ```
  [[[0, 0, 0, 0], ['X']], [['X, 1, 'X', 1], [1]]
  ```
  
6. Final solution (eliminate terms that output 'X'):
  
  ```
  [['X, 1, 'X', 1], [1]]
	
  O = B & D
  ```
  
</details>

### fill(table, default_value)
Function to fill a truth table with a default value for all other possible values of the inputs.
Return: filled truth table.

#### Example:

<details>
  <summary>Expand</summary>
  
  Input:
  ```
  # Manually declare truth table:
  truth_table = [[['A', 'B', 'C', 'I1', 'I2'], ['O1', 'O2', 'O3']], 
                 [[  1,   0,   0,    0,    0], [   0,    0,    1]], 
                 [[  0,   0,   0,    0,    0], [   0,    0,    1]]]
  
  # Print truth table in human-readable table format:
  print("Arbitrary Truth Table:\n")
  sp.show(truth_table)
  print("\n")

  # Populate truth table with default 0, 1, or 'X' for Karnaugh mapper.
  # kn.fill(input_truth_table, default_value)
  truth_table = kn.fill(truth_table, 0)

  # Print populated truth table in human-readable table format:
  print("Filled states:\n")
  sp.show(truth_table)
  print("\n")
  ```
  
  Console output:
  
  ```
  Arbitrary Truth Table:

| A | B | C | I1| I2|| O1| O2| O3|
----------------------------------
| 1 | 0 | 0 | 0 | 0 || 0 | 0 | 1 |
| 0 | 0 | 0 | 0 | 0 || 0 | 0 | 1 |


Filled states:

| A | B | C | I1| I2|| O1| O2| O3|
----------------------------------
| 0 | 0 | 0 | 0 | 0 || 0 | 0 | 1 |
| 0 | 0 | 0 | 0 | 1 || 0 | 0 | 0 |
| 0 | 0 | 0 | 1 | 0 || 0 | 0 | 0 |
| 0 | 0 | 0 | 1 | 1 || 0 | 0 | 0 |
| 0 | 0 | 1 | 0 | 0 || 0 | 0 | 0 |
| 0 | 0 | 1 | 0 | 1 || 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 || 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 1 || 0 | 0 | 0 |
| 0 | 1 | 0 | 0 | 0 || 0 | 0 | 0 |
| 0 | 1 | 0 | 0 | 1 || 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 0 || 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 || 0 | 0 | 0 |
| 0 | 1 | 1 | 0 | 0 || 0 | 0 | 0 |
| 0 | 1 | 1 | 0 | 1 || 0 | 0 | 0 |
| 0 | 1 | 1 | 1 | 0 || 0 | 0 | 0 |
| 0 | 1 | 1 | 1 | 1 || 0 | 0 | 0 |
| 1 | 0 | 0 | 0 | 0 || 0 | 0 | 1 |
| 1 | 0 | 0 | 0 | 1 || 0 | 0 | 0 |
| 1 | 0 | 0 | 1 | 0 || 0 | 0 | 0 |
| 1 | 0 | 0 | 1 | 1 || 0 | 0 | 0 |
| 1 | 0 | 1 | 0 | 0 || 0 | 0 | 0 |
| 1 | 0 | 1 | 0 | 1 || 0 | 0 | 0 |
| 1 | 0 | 1 | 1 | 0 || 0 | 0 | 0 |
| 1 | 0 | 1 | 1 | 1 || 0 | 0 | 0 |
| 1 | 1 | 0 | 0 | 0 || 0 | 0 | 0 |
| 1 | 1 | 0 | 0 | 1 || 0 | 0 | 0 |
| 1 | 1 | 0 | 1 | 0 || 0 | 0 | 0 |
| 1 | 1 | 0 | 1 | 1 || 0 | 0 | 0 |
| 1 | 1 | 1 | 0 | 0 || 0 | 0 | 0 |
| 1 | 1 | 1 | 0 | 1 || 0 | 0 | 0 |
| 1 | 1 | 1 | 1 | 0 || 0 | 0 | 0 |
| 1 | 1 | 1 | 1 | 1 || 0 | 0 | 0 |
  ```
</details>

### show(solution_array)
Function to print the solution array into HDL-compatible boolean equations.
Return: boolean expression.

### output(solution_array, output_file_path, verilog_module_name)
Function to generate a verilog module with the given finite state machine solution array. 

## Example Dataflow

Sample state diagram:
![State_Diagram](/photos/state_diagram.png "State_Diagram")

Input:

```
# Declare states with the format: [[state 0], [state 1], ...]
# Each [state n] = [(next state when I0 = 0, I1 = 0, ... In = 0), (next state when I0 = 0, I1 = 0, ..., In = 1), ...]
states = [[1, 1, 1, 3], [2, 2, 2, 2], [4, 4, 4, 4], [4, 4, 4, 4], [0, 0, 0, 0]]

# Function to parse states into table format for Karnaugh mapper to process:
parsed = sp.parse(states)

# Print parsed states into human-readable table format:
print("Parsed states:\n")
sp.show(parsed)
print("\n")

# Function to map the Karnaugh:
processed = kn.map(parsed)

# Print mapped Karnaugh into HDL-compatible boolean equations:
print("Output Equations:\n")
kn.show(processed)
print("\n")

# Output a verilog file with the implemented finite state machine:
# kn.output(mapped_array, output_file_path, verilog_module_name)
kn.output(processed, "FSM.v", "FSM")
print("Verilog output generated. Check: FSM.v")
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


Output Equations:

O1 = B
O2 = !A&!B&I1&I2 | !B&C
O3 = !A&!B&!C


Verilog output generated. Check: FSM.v
```

FSM.v:

```
module FSM(
	 input clk,
	 input [1:0] in,
	 output [2:0] state
	);

	reg [2:0] reg_state = 3'b0;
	always @(posedge clk) begin
		reg_state[0] <= reg_state[1];
		reg_state[1] <= !reg_state[0]&!reg_state[1]&reg_state[3]&reg_state[4] | !reg_state[1]&reg_state[2];
		reg_state[2] <= !reg_state[0]&!reg_state[1]&!reg_state[2];
	end
endmodule
```

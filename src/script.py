import states_parser as sp
import karnaugh as kn


print("Method 1: Solve Karnaugh equations based on finite state machine.\n")

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

# Output a verilog file with the implemented finite state machine:
# kn.output(mapped_array, output_file_path, verilog_module_name)
kn.output(processed, "FSM.v", "FSM")


print("\n\n\n\n")


print("Method 2: Solve Karnaugh equations based on arbitrary truth table.")

# Manually declare truth table:
truth_table = [[['A', 'B', 'C', 'I1', 'I2'], ['O1', 'O2', 'O3']], 
          [[1, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0]], 
          [[0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0]]]

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

# Function to map the Karnaugh:
processed = kn.map(truth_table)
print ("")

# Print mapped Karnaugh into HDL-compatible boolean equations:
print("Output Equations:\n")
kn.show(processed)


print("\n\n\n\n")


print("Method 3: Solve Karnaugh equations based on finite state machine and choice of flip flop.")

states = [[1, 1, 1, 3], [2, 2, 2, 2], [4, 4, 4, 4], [4, 4, 4, 4], [0, 0, 0, 0]]
parsed = sp.parse(states)

print("Parsed states:\n")
sp.show(parsed)
print("\n")

# Parse states into flip-flop table format:
# sp.flipflop(parsed_table, flipflop_type) where flipflop_type = "JK"/"SR"/"D"/"T"
parsed = sp.flipflop(parsed, "JK")

print("Parsed JK flip-flop states:\n")
sp.show(parsed)
print("\n")

processed = kn.map(parsed)
kn.show(processed)
# Parse states into table format for Karnaugh mapper
def parse(states):
    num_states = len(states)
    num_inputs = len(states[0])
    num_states_label = 1
    num_inputs_label = 1
    output = []

    # Determine number of input bits required
    while(2**(num_states_label) < num_states):
        num_states_label += 1

    while(2**(num_inputs_label) < num_inputs):
        num_inputs_label += 1

    # Label input bits
    inputs_label = []
    for i in range(0, num_states_label):
        inputs_label += [chr(65 + i)]

    for i in range(0, num_inputs_label):
        s = chr(73) + chr(49+i)
        inputs_label += [s]

    # Label output bits
    outputs_label = []
    for i in range(0, num_states_label):
        s = chr(79) + chr(49+i)
        outputs_label += [s]

    output += [[inputs_label, outputs_label]]

    # Parse states into binary table
    for i in range(0, 2**(num_states_label)):
        input_bin1 = []
        old_value = 0

        for x in range(0, num_states_label):
            value = int((i-old_value)/(2**(num_states_label-x-1)))
            input_bin1 += [value]
            old_value += value*(2**(num_states_label-x-1))

        for j in range(0, 2**(num_inputs_label)):
            old_value = 0
            input_bin2 = []
            for x in range(0, num_inputs_label):
                value = int((j-old_value)/(2**(num_inputs_label-x-1)))
                input_bin2 += [value]
                old_value += value*(2**(num_inputs_label-x-1))

            old_value = 0
            output_bin = []
            for x in range(0, num_states_label):
                if(i < num_states):
                    value = int((states[i][j]-old_value)/(2**(num_states_label-x-1)))
                    output_bin += [value]
                    old_value += value*(2**(num_states_label-x-1))
                else:
                    output_bin += 'X'
            
            input_bin = input_bin1 + input_bin2
            output += [[input_bin, output_bin]]

    return output

# Print parsed states into human-readable table
def show(parsed):
    cnt1 = 0
    for line in parsed:
        cnt2 = 0
        print("|", end = '')
        for item in line:
            for element in item:
                if(isinstance(element, str)):
                    if(len(element) > 1):
                        print(" %s|" %element, end = '')
                    else:
                        print(" %s |" %element, end = '')
                else:
                    print(" %1d |" %element, end = '')

            if(cnt2 == 0):
                print("|", end = '')
            cnt2 = 1

        if(cnt1 == 0):
            print("")
            for i in range(0, 7*len(parsed[0][0])):
                print("-", end = '')
        cnt1 = 1

        print("")




                


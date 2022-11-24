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

# Modify parsed states to fit flip flops
# type = "SR"/"JK"/"D"/"T"
def flipflop(parsed, type):
    num_inputs = len(parsed[0][0])
    num_outputs = len(parsed[0][1])
    output = []

    tmp = []
    if(type == "JK"):
        tmp += parsed[0][0]
        tmp2 = []
        for i in range(0, num_outputs):
            s1 = "J" + chr(97+i)
            s2 = "K" + chr(97+i)
            tmp2 += [s1, s2]
    elif(type == "SR"):
        tmp += parsed[0][0]
        tmp2 = []
        for i in range(0, num_outputs):
            s1 = "S" + chr(97+i)
            s2 = "R" + chr(97+i)
            tmp2 += [s1, s2]
    elif(type == "D"):
        tmp += parsed[0][0]
        tmp2 = []
        for i in range(0, num_outputs):
            s = "D" + chr(97+i)
            tmp2 += [s]
    elif(type == "T"):
        tmp += parsed[0][0]
        tmp2 = []
        for i in range(0, num_outputs):
            s = "T" + chr(97+i)
            tmp2 += [s]
    else:
        print("??")
        # Throw error
    
    output += [[tmp, tmp2]]

    tmp = []
    cnt = 1
    for line in parsed:
        if(cnt == 0):
            tmp = line[0]
            tmp2 = []
            for i in range(0, num_outputs):
                if((line[0][i] == 0) and (line[1][i] == 0)):
                    if(type == "JK"):
                        tmp2 += [0, 'X']
                    elif(type == "SR"):
                        tmp2 += ['X', 1]
                    elif(type == "D"):
                        tmp2 += [0]
                    elif(type == "T"):
                        tmp2 += [0]
                elif((line[0][i] == 0) and (line[1][i] == 1)):
                    if(type == "JK"):
                        tmp2 += [1, 'X']
                    elif(type == "SR"):
                        tmp2 += [1, 0]
                    elif(type == "D"):
                        tmp2 += [1]
                    elif(type == "T"):
                        tmp2 += [1]
                elif((line[0][i] == 1) and (line[1][i] == 0)):
                    if(type == "JK"):
                        tmp2 += ['X', 1]
                    elif(type == "SR"):
                        tmp2 += [0, 1]
                    elif(type == "D"):
                        tmp2 += [0]
                    elif(type == "T"):
                        tmp2 += [1]
                elif((line[0][i] == 1) and (line[1][i] == 1)):
                    if(type == "JK"):
                        tmp2 += [1, 'X']
                    elif(type == "SR"):
                        tmp2 += [1, 'X']
                    elif(type == "D"):
                        tmp2 += [1]
                    elif(type == "T"):
                        tmp2 += [0]
                elif((((line[0][i] == 0) or (line[0][i] == 1)) or (line[0][i] == 'X')) and (line[1][i] == 'X')):
                    if(type == "JK"):
                        tmp2 += ['X', 'X']
                    elif(type == "SR"):
                        tmp2 += ['X', 1]
                    elif(type == "D"):
                        tmp2 += ['X']
                    elif(type == "T"):
                        tmp2 += ['X']
                elif((line[0][i] == 'X') and (line[1][i] == 0)):
                    if(type == "JK"):
                        tmp2 += ['X', 'X']
                        # Throw warning
                    elif(type == "SR"):
                        tmp2 += [0, 1]
                    elif(type == "D"):
                        tmp2 += [0]
                    elif(type == "T"):
                        tmp2 += ['X']
                        # Throw warning
            output += [[tmp, tmp2]]
        cnt = 0
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
            for i in range(0, int(4.3*len(parsed[0][0] + parsed[0][1]))):
                print("-", end = '')
        cnt1 = 1

        print("")




                


import numpy as np

def parse(states):
    num_states = np.shape(states)[0]
    num_inputs = np.shape(states)[1]
    num_states_label = 1
    num_inputs_label = 1
    output = []

    while(2**(num_states_label) < num_states):
        num_states_label += 1

    while(2**(num_inputs_label) < num_inputs):
        num_inputs_label += 1

    inputs_label = []
    for i in range(0, num_states_label):
        inputs_label += [chr(65 + i)]

    for i in range(0, num_inputs_label):
        s = chr(73) + chr(49+i)
        inputs_label += [s]

    outputs_label = []
    for i in range(0, num_states_label):
        s = chr(79) + chr(49+i)
        outputs_label += [s]

    output += [[inputs_label, outputs_label]]

    for i in range(0, 2**(num_states_label)):
        input_bin1 = []
        old_value = 0

        for x in range(0, num_states_label):
            value = np.floor((i-old_value)/(2**(num_states_label-x-1)))
            input_bin1 += [value]
            old_value += value*(2**(num_states_label-x-1))


        for j in range(0, 2**(num_inputs_label)):
            old_value = 0
            input_bin2 = []
            for x in range(0, num_inputs_label):
                value = np.floor((j-old_value)/(2**(num_inputs_label-x-1)))
                input_bin2 += [value]
                old_value += value*(2**(num_inputs_label-x-1))

            old_value = 0
            output_bin = []
            for x in range(0, num_states_label):
                if(i < num_states):
                    value = np.floor((states[i][j]-old_value)/(2**(num_states_label-x-1)))
                    output_bin += [value]
                    old_value += value*(2**(num_states_label-x-1))
                else:
                    output_bin += 'X'
            
            input_bin = input_bin1 + input_bin2
            output += [[input_bin, output_bin]]

    return output

def present(parsed):
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
            for i in range(0, 22):
                print("-", end = '')
        cnt1 = 1

        print("")




                


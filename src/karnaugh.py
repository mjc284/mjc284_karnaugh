import numpy as np

# Check if two binary arrays differ by 1 bit
def check_neighbor(cmp1, cmp2):
    num_inputs = len(cmp1)
    output = []
    cnt = 0

    for inputs in range(0, num_inputs):
        if(cmp1[inputs] != cmp2[inputs]):
            output += ['X']
            cnt += 1
        else:
            output += [cmp1[inputs]]
    return [[cnt], output]

# Populate truth table with default values
def fill(table, default):
    num_inputs = len(table[0][0])
    num_outputs = len(table[0][1])

    output = []
    output += [table[0]]

    tmp1 = []
    tmp2 = []

    # Populate first address of empty row with 'default'
    for i in range(0, num_inputs):
        tmp1 += [0]
    for j in range(0, num_outputs):
        tmp2 += [default]
    output += [[tmp1, tmp2]]

    # Populate rest of the addresses with 'default'
    for i in range(1, 2**num_inputs):
        tmp1 = []
        for j in range(0, num_inputs):
            tmp1.insert(0, int(((i & 2**j)) != 0))
        tmp2 = []
        for j in range(0, num_outputs):
            tmp2 += [default]
        output += [[tmp1, tmp2]]

    # Find and replace existing table values
    swc = 0
    for line in table:
        if(swc == 1):
            index = 0
            for i in range(0, num_inputs):
                index += line[0][i]*(2**(num_inputs - i - 1))
            output[int(index)+1] = line
        swc = 1

    return output

# Map the Karnaugh
def map(table):
    inputs_label = table[0][0]
    outputs_label = table[0][1]
    num_inputs = len(inputs_label)
    num_outputs = len(outputs_label)

    # Reformat table into individual maps for each outputs
    maps = []
    for outputs in range(0, num_outputs):
        tmp = []
        label = 1
        for line in table:
            if(label == 0):
                tmp += [[line[0], line[1][outputs]]]
            label = 0
        maps += [tmp]

    # Extract elemets with output = 1 or X
    selected_maps = []
    for map in maps:
        tmp = []
        for line in map:
            if((line[1] == 1) or (line[1] == 'X')):
                tmp += [line]
        selected_maps += [tmp]

    # Remove trivial outputs
    old_selected_maps = []
    old_outputs_label = []
    cnt = 0
    for map in selected_maps:
        if(map != []):
            old_selected_maps += [map]
            old_outputs_label += [outputs_label[cnt]]
        else:
            num_outputs -= 1
        cnt += 1
    selected_maps = old_selected_maps
    outputs_label = old_outputs_label

    # Start of Karnaugh recursion
    old_selected_maps= []
    while(old_selected_maps != selected_maps):

        # Identify and merge adjacent cells using check_neighbor()
        old_selected_maps = selected_maps
        processed = []
        for map in selected_maps:
            num_entries = len(map)
            tmp = []

            if(num_entries >= 2):
                markoff = []
                for j in range(0, num_entries):
                    markoff += [0]
                for index1 in range(0, num_entries):
                    for index2 in range(index1 + 1, num_entries):
                        neighbor = check_neighbor(map[index1][0], map[index2][0])
                        if(neighbor[0][0] < 2):
                            if((map[index1][1] == 'X') and (map[index2][1] == 'X')):
                                tmp += [[neighbor[1], 'X']]
                            else:
                                tmp += [[neighbor[1], '1']]
                            markoff[index1] += 1
                            markoff[index2] += 1
                    if(markoff[index1] == 0):
                        tmp += [map[index1]]
            if(tmp != []):
                processed += [tmp]
            else:
                processed = selected_maps
        selected_maps = processed  

        # Remove duplicates
        post_selected_maps = []
        for map in selected_maps:
            post_map = []
            num_entries = len(map)
            for index1 in range(0, num_entries):
                same = 0
                for index2 in range(index1 + 1, num_entries):
                    if(map[index1] == map[index2]):
                        same = 1
                if(same != 1):
                    post_map += [map[index1]]
            post_selected_maps += [post_map]

        selected_maps = post_selected_maps 
    
    # Add labels
    mapped = []
    cnt = 0
    for map in selected_maps:
        tmp = []
        tmp += [[inputs_label, outputs_label[cnt]]]
        for line in map:
            if(line[1] != 'X'):
                tmp += [line]
        cnt += 1
        mapped += [tmp]

    return mapped

# Show boolean equations of mapped outputs
def show(mapped):
    for map in mapped:
        label = 1
        swc2 = 0
        print(map[0][1], end = '')
        print(" = ", end = '')
        for line in map:
            if(swc2 == 1):
                    print(" | ", end = '')
            if(label == 0):
                swc1 = 0
                num_item = len(line[0])
                for index in range(0, num_item):
                    if(line[0][index] == 1):
                        if(swc1 == 1):
                            print("&", end = '')
                        print(map[0][0][index], end = '')
                        swc1 = 1
                    elif(line[0][index] == 0):
                        if(swc1 == 1):
                            print("&", end = '')
                        print("!", end = '')
                        print(map[0][0][index], end = '')
                        swc1 = 1
                swc2 = 1
            label = 0
        print("")
        




   



            




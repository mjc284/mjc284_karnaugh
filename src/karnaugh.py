import numpy as np

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

def map(table):
    inputs_label = table[0][0]
    outputs_label = table[0][1]
    num_inputs = len(inputs_label)
    num_outputs = len(outputs_label)

    maps = []
    for outputs in range(0, num_outputs):
        tmp = []
        label = 1
        for line in table:
            if(label == 0):
                tmp += [[line[0], line[1][outputs]]]

            label = 0
        maps += [tmp]

    selected_maps = []

    for map in maps:
        tmp = []
        for line in map:
            if((line[1] == 1) or (line[1] == 'X')):
                tmp += [line]
        selected_maps += [tmp]
    
    processed = []
    for i in range(0, num_inputs):
        pre_selected_maps = []
        for map in selected_maps:
            num_entries = len(map)
            tmp = []
            if(num_entries > 2):
                for index1 in range(1, num_entries - 1):
                    cnt = 0
                    for index2 in range(index1 + 1, num_entries):
                        neighbor = check_neighbor(map[index1][0], map[index2][0])
                        if(neighbor[0][0] < 2):
                            if((map[index1][1] == 'X') and (map[index2][1] == 'X')):
                                tmp += [[neighbor[1], 'X']]
                            else:
                                tmp += [[neighbor[1], '1']]
                            cnt += 1
                    if(cnt == 0):
                        tmp += [map[index1]]
            if(tmp != []):
                processed += [tmp]

        selected_maps = []
        selected_maps += processed

    mapped = []
    for map in selected_maps:
        tmp = []
        for line in map:
            if(line[1] != 'X'):
                tmp += [line]
        mapped += [tmp]

    return mapped


   



            




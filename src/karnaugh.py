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

    old_processed = [1]
    processed = []
    while(old_processed != processed):
        pre_selected_maps = []
        old_processed = processed
        processed = []
        for map in selected_maps:
            num_entries = len(map)
            tmp = []

            if(num_entries > 2):
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

        selected_maps = []
        selected_maps += processed        

    print(selected_maps)
    print("")
    mapped = []
    cnt = 0
    for map in selected_maps:
        tmp = []
        tmp += [[table[0][0], table[0][1][cnt]]]
        for line in map:
            if(line[1] != 'X'):
                tmp += [line]
        cnt += 1
        mapped += [tmp]

    print(mapped)

    return mapped

def present(mapped):
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
        




   



            




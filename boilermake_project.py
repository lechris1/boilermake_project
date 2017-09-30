fp = open("cad-events-boilermake-partial.csv")

badge_dict = {}
line_num = 0
acceptable = ["SCHED","ARREST","DSP","STKDSP","OUTSER","TSTOP"]
for line in fp:
    line_list = line.split(",")
    CadUnit = line_list[1]
    DispType = line_list[6]
    time1 = line_list[3]
    time2 = line_list[4]
    if DispType not in acceptable:
        DispType = "Other"
        if CadUnit not in badge_dict: #checks if the Cad is in the dict
            badge_dict[CadUnit] = {DispType:[(time1,time2)]}
        else:
            if DispType not in badge_dict[CadUnit]:
                badge_dict[CadUnit][DispType] = [(time1,time2)]
            else:
                badge_dict[CadUnit][DispType].append((time1,time2))
    else:
        if CadUnit not in badge_dict: #checks if the Cad is in the dict
            badge_dict[CadUnit] = {DispType:[(time1,time2)]}
        else:
            if DispType not in badge_dict[CadUnit]:
                badge_dict[CadUnit][DispType] = [(time1,time2)]
            else:
                badge_dict[CadUnit][DispType].append((time1,time2))
    line_num += 1

search = input("Search two CadUnits to compare (CadUnit1 space CadUnit2: ")
search = search.split()
Cad_info = []
Cad2_info = []
if search[0] in badge_dict:
    total_time = 0
    for disp in badge_dict[search[0]]:
        total_time += len(badge_dict[search[0]][disp])
    for i in badge_dict[search[0]]:
        percent = len(badge_dict[search[0]][i])/total_time
        disp_type_tup = ((i),percent,badge_dict[search[0]][i])
        Cad_info.append(disp_type_tup)
if search[1] in badge_dict:
    total_time = 0
    for disp in badge_dict[search[1]]:
        total_time += len(badge_dict[search[1]][disp])
    for i in badge_dict[search[1]]:
        percent = len(badge_dict[search[1]][i])/total_time
        disp_type_tup = ((i),percent,badge_dict[search[1]][i])
        Cad2_info.append(disp_type_tup)
else:
    print("ERROR: CadUnit not found")
    
print(Cad_info)
print(Cad2_info)
fp.close()
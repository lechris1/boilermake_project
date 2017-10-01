import plotly
import plotly.plotly as py
import plotly.figure_factory as ff
import plotly.graph_objs as go
plotly.tools.set_credentials_file(username='lechris1', api_key='pUnU4LIH9XjDK1rf91dH')

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


# Set table

first = []
first_percents = []
for i in range(len(Cad_info)):
    row = [search[0],Cad_info[i][0], len(Cad_info[i][2])]
    first.append(row)
    first_percents.append(Cad_info[i][1])

second= []
second_percents = []
for i in range(len(Cad2_info)):
    row = [search[1],Cad2_info[i][0], len(Cad2_info[i][2])]
    second.append(row)
    second_percents.append(Cad2_info[i][1])
               
data_matrix = [['CadUnit','Dispatch Type','Number of Occurances']]

for item in first:
    data_matrix.append(item)

for item in second:
    data_matrix.append(item)

table = ff.create_table(data_matrix)
py.plot(table, filename='simple_table')

# Set pie chart 1

labels1 = []
values1 = first_percents

for i in range(len(first)):
    labels1.append(first[i][1])

trace = go.Pie(labels=labels1, values=values1)
py.plot([trace], filename='basic_pie_chart1')

# Set pie chart 2

labels2 = []
values2 = second_percents

for i in range(len(second)):
    labels2.append(second[i][1])

trace = go.Pie(labels=labels2 values=values2)
py.plot([trace], filename='basic_pie_chart2')

fp.close()

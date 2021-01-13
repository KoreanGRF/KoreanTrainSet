"""
  한국 열차 세트(Korean Train Set)
  * Official download site : https://telk.kr/ottd/newgrf/ko_train_set
  * Github repository      : https://github.com/KoreanGRF/KoreanTrainSet
"""

# Define a dictionary
trainList = {}

#                       speed    cost   running_cost capacity loading_speed introduction
trainList['K4x00']    = 150,     1,     10,           0,       0,           (1963, 1, 1)
trainList['K7000']    = 150,     1,     10,           0,       0,           (1963, 1, 1)
trainList['K7x00']    = 150,     2,     10,           0,       0,           (1986, 1, 1)
trainList['K8000']    =  90,     3,     10,           0,       0,           (1972, 1, 1)
trainList['K8100']    = 150,     3,     10,           0,       0,           (1990, 1, 1)
trainList['K8200']    = 150,     3,     10,           0,       0,           (2002, 1, 1)
trainList['K8500']    = 150,     3,     10,           0,       0,           (2012, 1, 1)
trainList['DHC']      = 150,     3,     10,          10,      22,           (1987, 1, 1)


# Generates spec.pnml
content = ""
for _name in trainList:
  content += "#define " + _name + "_SPEED " + str(trainList[_name][0]) + "\n"
  content += "#define " + _name + "_COST " + str(trainList[_name][1]) + "\n"
  content += "#define " + _name + "_RUNNINGCOST " + str(trainList[_name][2]) + "\n"
  content += "#define " + _name + "_CAPACITY " + str(trainList[_name][3]) + "\n"
  content += "#define " + _name + "_LOADINGSPEED " + str(trainList[_name][4]) + "\n"
  content += "#define " + _name + "_INTRODUCTION date" + str(trainList[_name][5]) + "\n"

f = open("./generated/spec.pnml", "w")
f.write(content)
f.close()
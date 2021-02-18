"""
  한국 열차 세트(Korean Train Set)
  * Official download site : https://telk.kr/ottd/newgrf/ko_train_set
  * Github repository      : https://github.com/KoreanGRF/KoreanTrainSet
"""
import math

# Define a dictionary
trainList = {}

#                            speed    cost   running_cost capacity loading_speed introduction
trainList['K4x00']         = 150,     1,     10,           0,       0,           (1963, 1, 1)
trainList['K7000']         = 150,     1,     10,           0,       0,           (1963, 1, 1)
trainList['K7x00']         = 150,     2,     10,           0,       0,           (1986, 1, 1)
trainList['K8000']         =  90,     3,     10,           0,       0,           (1972, 1, 1)
trainList['K8100']         = 150,     3,     10,           0,       0,           (1990, 1, 1)
trainList['K8200']         = 150,     3,     10,           0,       0,           (2002, 1, 1)
trainList['K8500']         = 150,     3,     10,           0,       0,           (2012, 1, 1)
trainList['DHC']           = 150,     3,     10,          20,       5,           (1987, 1, 1)
trainList['DHC_wagon']     = 150,     3,     10,          20,       5,           (1987, 1, 1)
trainList['ITXSME']        = 150,     5,     10,          44,       5,           (2014, 1, 1)
trainList['ITXSME_wagon']  = 150,     5,     10,          44,       5,           (2014, 1, 1)
trainList['NURIRO']        = 150,     10,    15,          64,      10,           (2010, 1, 1)
trainList['NURIRO_wagon']  = 150,     10,    15,          64,      10,           (2010, 1, 1)
trainList['CDC']           = 120,     10,    15,          64,      10,           (2010, 1, 1)
trainList['CDC_wagon']     = 120,     10,    15,          64,      10,           (1996, 1, 1)
trainList['KTX1N']         = 330,     10,    15,          64,      10,           (2004, 4, 1)
trainList['KTX2N']         = 330,     10,    15,          64,      10,           (2009, 1, 1)
trainList['SRT']           = 330,     10,    15,          64,      10,           (2015, 1, 1)
trainList['KTX_wagon']     = 330,     10,    15,          29,      10,           (2004, 1, 1)


# Generates spec.pnml
content = ""
for _name in trainList:
  content += "#define var_" + _name + "_SPEED " + str(trainList[_name][0]) + "\n"
  content += "#define var_" + _name + "_COST " + str(trainList[_name][1]) + "\n"
  content += "#define var_" + _name + "_RUNNINGCOST " + str(trainList[_name][2]) + "\n"
  content += "#define var_" + _name + "_CAPACITY " + str(trainList[_name][3]) + "\n"
  content += "#define var_" + _name + "_LOADINGSPEED " + str(trainList[_name][4]) + "\n"
  content += "#define var_" + _name + "_INTRODUCTION date" + str(trainList[_name][5]) + "\n"

f = open("./generated/spec.pnml", "w")
f.write(content)
f.close()
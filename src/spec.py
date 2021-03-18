"""
  한국 열차 세트(Korean Train Set)
  * Official download site : https://telk.kr/ottd/newgrf/ko_train_set
  * Github repository      : https://github.com/KoreanGRF/KoreanTrainSet
"""
import math

# Define a dictionary
trainList = {}

#                                 speed    cost    running_cost capacity loading_speed power   introduction
trainList['K4x00']              = 150,     10,     10,          None,    None,         1230,   (2001, 1, 1)
trainList['K7000']              = 150,     10,     10,          None,    None,         2460,   (1986, 1, 1)
trainList['K7x00']              = 150,     20,     10,          None,    None,         2238,   (1986, 1, 1)
trainList['K7600']              = 150,     20,     12,          None,    None,         2602,   (2014, 1, 1)
trainList['K8000']              = 90,      30,     10,          None,    None,         3900,   (1972, 1, 1)
trainList['K8x00']              = 150,     30,     10,          None,    None,         5200,   (1990, 1, 1)
trainList['K8500']              = 150,     30,     10,          None,    None,         6600,   (2012, 1, 1)
trainList['DHC']                = 150,     30,     10,          20,      5,            2237,   (1987, 1, 1)
trainList['DHC_wagon']          = 150,     30,     10,          20,      5,            0,      (1987, 1, 1)
trainList['ITX_SAEMAEUL']       = 150,     50,     10,          44,      5,            3000,   (2014, 1, 1)
trainList['ITX_SAEMAEUL_wagon'] = 150,     50,     10,          44,      5,            200,    (2014, 1, 1)
trainList['NURIRO']             = 150,     100,    15,          64,      10,           2000,   (2010, 1, 1)
trainList['NURIRO_wagon']       = 150,     100,    15,          64,      10,           200,    (2010, 1, 1)
trainList['CDC']                = 120,     100,    15,          64,      10,           800,    (2010, 1, 1)
trainList['CDC_wagon']          = 120,     100,    15,          64,      10,           0,      (1996, 1, 1)
trainList['NDC']                = 130,     60,     10,          44,      10,           455,    (1984, 1, 1)
trainList['NDC_wagon']          = 130,     60,     10,          44,      10,           0,      (1984, 1, 1)
trainList['KTX1N']              = 300,     100,    15,          64,      10,           13200,  (2004, 4, 1)
trainList['KTX2N']              = 300,     100,    15,          64,      10,           8800,   (2009, 1, 1)
trainList['SRT']                = 300,     100,    15,          64,      10,           8800,   (2015, 1, 1)
trainList['EUM']                = 260,     100,    15,          76,      10,           8800,   (2019, 1, 1)
trainList['KTX_wagon']          = 300,     100,    15,          58,      10,           0,      (2004, 1, 1)
trainList['MUGUNGHWA_wagon']    = 135,     10,     15,          72,      10,           0,      (1972, 1, 1)
trainList['TONGIL_wagon']       = 120,     10,     15,          72,      10,           0,      (1988, 1, 1)
trainList['POWER_CAR']          = 120,     10,     15,          72,      10,           0,      (1972, 1, 1)
trainList['CAFE_CAR']           = 120,     10,     15,          72,      10,           0,      (1972, 1, 1)
trainList['MIKA3']              = 90,      10,      5,          0,       0,            726,    (1927, 1, 1)
trainList['PASHI5']             = 110,     10,      5,          0,       0,            790,    (1939, 1, 1)
trainList['MATE2']              = 90,      10,      5,          0,       0,            1074,   (1943, 1, 1)

trainList['SEOUL_METRO_1']      = 100,     100,    15,          100,     30,           2000,   (1972, 1, 1)
trainList['SEOUL_METRO_2']      = 100,     100,    15,          100,     30,           2000,   (1983, 1, 1)
trainList['SEOUL_METRO_3']      = 100,     100,    15,          100,     30,           2000,   (1983, 1, 1)
trainList['SEOUL_METRO_4']      = 100,     100,    15,          100,     30,           2000,   (1983, 1, 1)
trainList['SEOUL_METRO_5_9']    = 100,     100,    15,          100,     30,           2000,   (1995, 1, 1)
trainList['SUIN_BUNDANG']       = 100,     100,    15,          100,     30,           2000,   (1993, 1, 1)
trainList['GYEONGCHUN']         = 100,     100,    15,          100,     30,           2000,   (2010, 1, 1)
trainList['ITX_CHEONGCHUN']     = 100,     100,    15,          100,     30,           2000,   (2012, 1, 1)
trainList['METRO_wagon']        = 100,     100,    15,          100,     30,           200,    (1972, 1, 1)

trainList['PASSWG']             = None,     10,    15,          None,    10,           200,    (1950, 1, 1)


# Generates spec.pnml
content = ""
for _name in trainList:
  if trainList[_name][0] is not None:
    content += "#define var_" + _name + "_SPEED " + str(trainList[_name][0]) + "\n"
  if trainList[_name][1] is not None:
    content += "#define var_" + _name + "_COST " + str(trainList[_name][1]) + "\n"
  if trainList[_name][2] is not None:
    content += "#define var_" + _name + "_RUNNINGCOST " + str(trainList[_name][2]) + "\n"
  if trainList[_name][3] is not None:
    content += "#define var_" + _name + "_CAPACITY " + str(trainList[_name][3]) + "\n"
  if trainList[_name][4] is not None:
    content += "#define var_" + _name + "_LOADINGSPEED " + str(trainList[_name][4]) + "\n"
  if trainList[_name][5] is not None:
    content += "#define var_" + _name + "_POWER " + str(trainList[_name][5]) + "\n"
  if trainList[_name][6] is not None:
    content += "#define var_" + _name + "_INTRODUCTION date" + str(trainList[_name][6]) + "\n"

f = open("./generated/spec.pnml", "w")
f.write(content)
f.close()
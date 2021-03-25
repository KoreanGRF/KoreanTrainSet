"""
  한국 열차 세트(Korean Train Set)
  * Official download site : https://telk.kr/ottd/newgrf/ko_train_set
  * Github repository      : https://github.com/KoreanGRF/KoreanTrainSet
"""
import math

# Define a dictionary
trainList = {}

#                                 speed    cost    running_cost  capacity loading_speed power   weight  introduction
trainList['MIKA3']              = 90,      10,     20,           0,       0,            726,    113,    (1927, 1, 1)
trainList['PASHI5']             = 110,     10,     20,           0,       0,            790,    113,    (1939, 1, 1)
trainList['MATE2']              = 90,      10,     20,           0,       0,            1074,   113,    (1943, 1, 1)
trainList['K4x00']              = 105,     10,     20,           None,    None,         1230,   88,     (2001, 1, 1)
trainList['K7000']              = 150,     10,     20,           None,    None,         2460,   119,    (1986, 1, 1)
trainList['K7x00']              = 150,     10,     20,           None,    None,         2238,   132,    (1971, 1, 1)
trainList['K7600']              = 165,     10,     20,           None,    None,         2602,   20,     (2014, 1, 1)
trainList['K8000']              = 90,      10,     30,           None,    None,         3952,   132,    (1972, 1, 1)
trainList['K8x00']              = 150,     10,     20,           None,    None,         5200,   132,    (1990, 1, 1)
trainList['K8500']              = 150,     10,     20,           None,    None,         6600,   132,    (2012, 1, 1)
trainList['DHC']                = 150,     10,     20,           22,      5,            4474,   70,     (1987, 1, 1)
trainList['DHC_wagon']          = 150,     100,    10,           64,      5,            0,      20,     (1987, 1, 1)
trainList['ITX_SAEMAEUL']       = 150,     10,     20,           44,      5,            6000,   45,     (2014, 1, 1)
trainList['ITX_SAEMAEUL_wagon'] = 150,     None,   10,           44,      5,            200,    45,     (2014, 1, 1)
trainList['NURIRO']             = 150,     10,     20,           64,      10,           4000,   55,     (2010, 1, 1)
trainList['NURIRO_wagon']       = 150,     None,   10,           64,      10,           200,    55,     (2010, 1, 1)
trainList['CDC']                = 120,     10,     20,           64,      10,           800,    50,     (2010, 1, 1)
trainList['CDC_wagon']          = 120,     None,   10,           64,      10,           0,      50,     (1996, 1, 1)
trainList['NDC']                = 130,     10,     20,           44,      10,           455,    50,     (1984, 1, 1)
trainList['NDC_wagon']          = 130,     None,   10,           44,      10,           0,      20,     (1984, 1, 1)
trainList['DEC']                = 110,     10,     20,           28,      10,           807,    50,     (1980, 1, 1)
#trainList['EEC']                = 110,     10,     20,           64?,     10,           ?,      50,     (1984, 1, 1)
trainList['BIDULGI_CDC']        = 110,     10,     20,           150,     15,           261,    37,     (1961, 1, 1)
trainList['KTX1N']              = 300,     20,     50,           0,       10,           13200,  68,     (2004, 4, 1)
trainList['KTX2N']              = 300,     20,     50,           0,       10,           8800,   68,     (2009, 1, 1)
trainList['SRT']                = 300,     20,     50,           0,       10,           8800,   20,     (2015, 1, 1)
trainList['EUM']                = 260,     20,     50,           76,      10,           8800,   53,     (2019, 1, 1)
trainList['KTX_wagon']          = 300,     None,   40,           58,      10,           0,      20,     (2004, 1, 1)
trainList['MUGUNGHWA_CAR']      = 135,     100,    10,           72,      10,           0,      17,     (1972, 1, 1)
trainList['TONGIL_CAR']         = 120,     100,    10,           72,      10,           0,      17,     (1988, 1, 1)
trainList['BIDULGI_CAR']        = 110,     100,    10,           100,     10,           0,      34,     (1927, 1, 1)
trainList['GENERATOR_CAR']      = 120,     10,     10,           0,       10,           0,      17,     (1972, 1, 1)
trainList['CAFE_CAR']           = 120,     100,    10,           50,      10,           0,      17,     (1972, 1, 1)
trainList['SEOUL_METRO_1']      = 100,     10,     30,           100,     30,           2000,   20,     (1972, 1, 1)
trainList['SEOUL_METRO_2']      = 100,     10,     30,           100,     30,           2000,   20,     (1983, 1, 1)
trainList['SEOUL_METRO_3']      = 100,     10,     30,           100,     30,           2000,   20,     (1983, 1, 1)
trainList['SEOUL_METRO_4']      = 100,     10,     30,           100,     30,           2000,   20,     (1983, 1, 1)
trainList['SEOUL_METRO_5_9']    = 100,     10,     30,           100,     30,           2000,   20,     (1995, 1, 1)
trainList['SUIN_BUNDANG']       = 100,     10,     30,           100,     30,           2000,   20,     (1993, 1, 1)
trainList['GYEONGCHUN']         = 100,     10,     30,           100,     30,           2000,   20,     (2010, 1, 1)
trainList['ITX_CHEONGCHUN']     = 180,     10,     30,           50,      30,           2000,   45,     (2012, 1, 1)
trainList['AREX']               = 110,     10,     30,           100,     30,           2000,   20,     (2007, 1, 1)
trainList['AREX_NONSTOP']       = 110,     None,   None,         45,      10,           None,   20,     (2007, 1, 1)
trainList['SHINBUNDANG']        = 100,     10,     30,           100,     30,           2000,   20,     (2011, 3, 30)
trainList['INCHEON_METRO_1']    = 100,     10,     30,           100,     30,           2000,   20,     (1999, 1, 1)
trainList['BUSAN_METRO_1']      = 100,     10,     30,           100,     30,           2000,   20,     (1985, 1, 1)
trainList['BUSAN_METRO_2']      = 100,     10,     30,           100,     30,           2000,   20,     (1999, 1, 1)
trainList['BUSAN_METRO_3']      = 100,     10,     30,           100,     30,           2000,   20,     (1999, 1, 1)
trainList['BUSAN_METRO_4']      = 70,      10,     30,           42,      20,           1000,   20,     (2011, 1, 1)
trainList['DAEGU_METRO_1']      = 100,     10,     30,           100,     30,           2000,   20,     (1997, 1, 1)
trainList['DAEGU_METRO_2']      = 100,     10,     30,           100,     30,           2000,   20,     (2005, 1, 1)
trainList['DAEJEON_METRO_1']    = 100,     10,     30,           100,     30,           2000,   20,     (2006, 1, 1)
trainList['GWANGJU_METRO_1']    = 100,     10,     30,           100,     30,           2000,   20,     (2004, 1, 1)
trainList['METRO_wagon']        = None,    10,     30,           100,     30,           200,    20,     None
trainList['GIMPO_GOLDLINE']     = 80,      10,     20,           100,     30,           500,    20,     (2019, 1, 1)
trainList['BUSANGIMHAE']        = 70,      10,     20,           100,     30,           500,    20,     (2011, 1, 1)
trainList['INCHEON_METRO_2']    = 80,      10,     20,           100,     30,           500,    20,     (2016, 1, 1)
trainList['DAEGU_METRO_3']      = 80,      10,     20,           100,     30,           500,    20,     (2015, 4, 23)
trainList['UISINSEOL']          = 80,      10,     20,           80,      30,           520,    20,     (2017, 1, 1)
trainList['YONGIN_EVERLINE']    = 80,      10,     20,           80,      30,           500,    20,     (2017, 1, 1)
trainList['UIJEONGBU']          = 80,      10,     20,           80,      30,           500,    20,     (2012, 1, 1)
trainList['PASSENGER_WAGON']    = None,    100,    10,           None,    10,           200,    20,     (1950, 1, 1)
trainList['FLAT_CAR']           = None,    100,    10,           35,      5,            None,   17,     (1950, 1, 1)
trainList['HOPPER_CAR']         = None,    100,    10,           35,      5,            None,   17,     (1950, 1, 1)
trainList['BAGGAGE_CAR']        = 120,     100,    10,           35,      5,            None,   17,     (1950, 1, 1)
trainList['TANK_CAR']           = None,    100,    10,           35,      5,            None,   17,     (1950, 1, 1)
trainList['STAKE_CAR']          = None,    100,    10,           35,      5,            None,   17,     (1950, 1, 1)


# Generates spec.pnml (Do not modified this below!)
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
    content += "#define var_" + _name + "_WEIGHT " + str(trainList[_name][6]) + "\n"
  if trainList[_name][7] is not None:
    content += "#define var_" + _name + "_INTRODUCTION date" + str(trainList[_name][7]) + "\n"

f = open("./generated/spec.pnml", "w")
f.write(content)
f.close()
"""
  한국 열차 세트(Korean Train Set)
  * Official download site : https://telk.kr/ottd/newgrf/ko_train_set
  * Github repository      : https://github.com/KoreanGRF/KoreanTrainSet
"""

# Define a dictionary
trainList = {}

#                                 speed1  speed2  cost    running_cost  capacity loading_speed power   weight  introduction
trainList['HOKEY7']             = 50,     50,     10,     4,            0,       0,            150,    43,     (1952, 1, 1)
trainList['MIKA3']              = 70,     70,     10,     4,            0,       0,            726,    156,    (1927, 1, 1)
trainList['PASHI5']             = 110,    110,    10,     4,            0,       0,            790,    196,    (1939, 1, 1)
trainList['MATE2']              = 90,     90,     10,     4,            0,       0,            1074,   179,    (1943, 1, 1)
trainList['K2x00']              = 105,    105,    10,     4,            None,    None,         597,    95,     (1955, 1, 1)
trainList['K4x00']              = 105,    105,    10,     4,            None,    None,         1230,   88,     (2001, 1, 1)
trainList['K5000']              = 105,    105,    10,     4,            None,    None,         2347,   141,    (1957, 1, 1)
trainList['K6000']              = 105,    105,    10,     4,            None,    None,         2414,   136,    (1963, 1, 1)
trainList['K6100']              = 105,    105,    10,     4,            None,    None,         2414,   139,    (1966, 1, 1)
trainList['K6200']              = 105,    105,    10,     4,            None,    None,         2414,   139,    (1967, 1, 1)
trainList['K6300']              = 105,    105,    10,     4,            None,    None,         2682,   99,     (1969, 1, 1)
trainList['K7000']              = 150,    150,    10,     4,            None,    None,         2460,   119,    (1986, 1, 1)
trainList['K7x00']              = 150,    150,    10,     4,            None,    None,         2238,   130,    (1971, 1, 1)
trainList['K7600']              = 150,    165,    10,     4,            None,    None,         2602,   132,    (2014, 1, 1)
trainList['K8000']              = 85,     90,     10,     6,            None,    None,         3952,   132,    (1972, 1, 1)
trainList['K8x00']              = 150,    220,    10,     4,            None,    None,         5200,   88,     (1990, 1, 1)
trainList['K8500']              = 150,    165,    10,     4,            None,    None,         6600,   132,    (2012, 1, 1)
trainList['DHC']                = 150,    150,    10,     4,            22,      5,            4474,   70,     (1987, 1, 1)
trainList['ITX_SAEMAEUL']       = 150,    165,    10,     4,            58,      5,            3000,   45,     (2014, 1, 1)
trainList['ITX_SAEMAEUL_wagon'] = 150,    165,    None,   2,            74,      5,            200,    45,     (2014, 1, 1)
trainList['NURIRO']             = 150,    165,    10,     4,            64,      10,           4000,   45,     (2010, 1, 1)
trainList['NURIRO_wagon']       = 150,    150,    None,   2,            64,      10,           200,    37,     (2010, 1, 1)
trainList['BIDULGI_CDC']        = 110,    110,    10,     4,            150,     15,           261,    37,     (1961, 1, 1)
trainList['NARROW_DIESEL_CAR']  = 55,     55,     10,     4,            90,      15,           149,    21,     (1965, 1, 1)
trainList['CDC']                = 120,    120,    10,     4,            64,      10,           800,    50,     (1996, 1, 1)
trainList['CDC_wagon']          = 120,    120,    None,   2,            64,      10,           0,      50,     (1996, 1, 1)
trainList['NDC']                = 120,    120,    10,     4,            44,      10,           455,    50,     (1984, 1, 1)
trainList['NDC_wagon']          = 120,    120,    None,   2,            44,      10,           0,      20,     (1984, 1, 1)
trainList['DEC']                = 110,    110,    10,     4,            28,      10,           807,    62,     (1980, 1, 1)
trainList['EEC']                = 110,    110,    10,     4,            56,      10,           2880,   43,     (1980, 1, 1)
trainList['KTX1N']              = 305,    320,    20,     10,           0,       10,           13200,  68,     (2004, 4, 1)
trainList['KTX2N']              = 305,    320,    20,     10,           0,       10,           8800,   68,     (2009, 1, 1)
trainList['SRT']                = 305,    320,    20,     10,           0,       10,           8800,   68,     (2015, 1, 1)
trainList['EUM']                = 260,    286,    20,     10,           76,      10,           8800,   60,     (2019, 1, 1)
trainList['KTX_wagon']          = 300,    300,    None,   8,            58,      10,           0,      20,     (2004, 1, 1)
trainList['SAEMAEUL_CAR']       = 150,    150,    100,    2,            64,      10,           0,      20,     (1969, 1, 1)
trainList['MUGUNGHWA_CAR']      = 135,    135,    100,    2,            72,      10,           0,      17,     (1970, 1, 1)
trainList['TONGIL_CAR']         = 120,    120,    100,    2,            72,      10,           0,      17,     (1963, 1, 1)
trainList['BIDULGI_CAR']        = 110,    110,    100,    2,            100,     10,           0,      35,     (1927, 1, 1)
trainList['GENERATOR_CAR']      = 120,    120,    10,     2,            0,       10,           0,      17,     (1972, 1, 1)
trainList['CAFE_CAR']           = 120,    120,    100,    2,            50,      10,           0,      17,     (1972, 1, 1)
trainList['SEOUL_METRO_1']      = 100,    100,    10,     6,            100,     30,           2000,   20,     (1972, 1, 1)
trainList['SEOUL_METRO_2']      = 100,    100,    10,     6,            100,     30,           2000,   20,     (1983, 1, 1)
trainList['SEOUL_METRO_3']      = 100,    100,    10,     6,            100,     30,           2000,   20,     (1983, 1, 1)
trainList['SEOUL_METRO_4']      = 100,    100,    10,     6,            100,     30,           2000,   20,     (1983, 1, 1)
trainList['SEOUL_METRO_5_9']    = 100,    100,    10,     6,            100,     30,           2000,   20,     (1995, 1, 1)
trainList['SUIN_BUNDANG']       = 100,    100,    10,     6,            100,     30,           2000,   20,     (1993, 1, 1)
trainList['GYEONGCHUN']         = 100,    100,    10,     6,            100,     30,           2000,   20,     (2010, 1, 1)
trainList['ITX_CHEONGCHUN']     = 180,    180,    10,     6,            50,      30,           2000,   45,     (2012, 1, 1)
trainList['AREX']               = 110,    120,    10,     6,            100,     30,           2000,   20,     (2007, 1, 1)
trainList['AREX_NONSTOP']       = 110,    120,    None,   None,         45,      10,           None,   20,     (2007, 1, 1)
trainList['SHINBUNDANG']        = 100,    100,    10,     6,            100,     30,           2000,   20,     (2011, 3, 30)
trainList['INCHEON_METRO_1']    = 100,    100,    10,     6,            100,     30,           2000,   20,     (1999, 1, 1)
trainList['INCHEON_METRO_2']    = 80,     90,     10,     4,            100,     30,           500,    32,     (2016, 1, 1)
trainList['BUSAN_METRO_1']      = 100,    100,    10,     6,            100,     30,           2000,   20,     (1985, 1, 1)
trainList['BUSAN_METRO_2']      = 100,    100,    10,     6,            100,     30,           2000,   20,     (1999, 1, 1)
trainList['BUSAN_METRO_3']      = 100,    100,    10,     6,            100,     30,           2000,   20,     (1999, 1, 1)
trainList['BUSAN_METRO_4']      = 60,     70,     10,     6,            42,      20,           1000,   12,     (2011, 1, 1)
trainList['DAEGU_METRO_1']      = 100,    100,    10,     6,            100,     30,           2000,   20,     (1997, 1, 1)
trainList['DAEGU_METRO_2']      = 100,    100,    10,     6,            100,     30,           2000,   20,     (2005, 1, 1)
trainList['DAEJEON_METRO_1']    = 100,    100,    10,     6,            100,     30,           2000,   20,     (2006, 1, 1)
trainList['GWANGJU_METRO_1']    = 100,    100,    10,     6,            100,     30,           2000,   20,     (2004, 1, 1)
trainList['METRO_wagon']        = None,   None,   10,     6,            100,     30,           200,    20,     None
trainList['GIMPO_GOLDLINE']     = 80,     90,     10,     4,            100,     30,           500,    23,     (2019, 1, 1)
trainList['BUSANGIMHAE']        = 70,     80,     10,     4,            100,     30,           500,    23,     (2011, 1, 1)
trainList['DAEGU_METRO_3']      = 80,     80,     10,     4,            100,     30,           500,    20,     (2015, 4, 23)
trainList['UISINSEOL']          = 70,     80,     10,     4,            80,      30,           520,    23,     (2017, 1, 1)
trainList['YONGIN_EVERLINE']    = 80,     80,     10,     4,            80,      30,           500,    24,     (2017, 1, 1)
trainList['UIJEONGBU']          = 80,     80,     10,     4,            80,      30,           500,    16,     (2012, 1, 1)
trainList['SILLIM']             = 60,     70,     10,     4,            52,      30,           500,    16,     (2020, 1, 1)
trainList['ECOBEE']             = 80,     110,    10,     4,            186,     20,           500,    19,     (2012, 1, 1)
trainList['PASSENGER_WAGON']    = None,   None,   100,    2,            None,    10,           None,   20,     (1950, 1, 1)
trainList['PASSENGER_WAGON_P']  = None,   None,   None,   4,            None,    None,         200,    25,     (1950, 1, 1)
trainList['NARROW_GAUGE_WAGON'] = None,   None,   100,    2,            90,      10,           None,   14,     (1952, 1, 1)
trainList['NARROW_BOXCAR']      = None,   None,   80,     2,            12,      5,            None,   14,     (1952, 1, 1)
trainList['NARROW_HOPPERCAR']   = None,   None,   80,     2,            12,      5,            None,   14,     (1952, 1, 1)
trainList['FLAT_CAR']           = 120,    120,    100,    2,            35,      5,            None,   17,     (1950, 1, 1)
trainList['HOPPER_CAR']         = 120,    120,    100,    2,            35,      5,            None,   17,     (1950, 1, 1)
trainList['BAGGAGE_CAR']        = 120,    120,    100,    2,            35,      5,            None,   17,     (1950, 1, 1)
trainList['BOX_CAR']            = 120,    120,    100,    2,            51,      5,            None,   25,     (1966, 1, 1)
trainList['BOX_CAR_2003']       = 120,    120,    None,   None,         51,      None,         None,   25,     (2003, 1, 1)
trainList['BOX_CAR_1998']       = 100,    100,    None,   None,         51,      None,         None,   28,     (1998, 1, 1)
trainList['BOX_CAR_1996']       = 90,     90,     None,   None,         48,      None,         None,   26,     (1996, 1, 1)
trainList['BOX_CAR_1972']       = 90,     90,     None,   None,         48,      None,         None,   22,     (1972, 1, 1)
trainList['BOX_CAR_1966']       = 90,     90,     None,   None,         48,      None,         None,   22,     (1966, 1, 1)
trainList['TANK_CAR']           = 120,    120,    100,    2,            35,      5,            None,   17,     (1950, 1, 1)
trainList['MAIL_CAR']           = None,   None,   100,    2,            35,      5,            None,   17,     (1950, 1, 1)
trainList['SLEEPING_CAR']       = None,   None,   120,    2,            28,      5,            None,   17,     (1966, 1, 1)
trainList['STAKE_CAR']          = 120,    120,    100,    2,            35,      5,            None,   17,     (1950, 1, 1)


# Generates spec.pnml (Do not modified this below!)
content = ""
for _name in trainList:
  if trainList[_name][0] is not None:
    content += "#define var_" + _name + "_SPEED " + str(trainList[_name][0]) + "\n"
  if trainList[_name][1] is not None:
    content += "#define var_" + _name + "_DESIGN_SPEED " + str(trainList[_name][1]) + "\n"
  if trainList[_name][2] is not None:
    content += "#define var_" + _name + "_COST " + str(trainList[_name][2]) + "\n"
  if trainList[_name][3] is not None:
    content += "#define var_" + _name + "_RUNNINGCOST " + str(trainList[_name][3]) + "\n"
  if trainList[_name][4] is not None:
    content += "#define var_" + _name + "_CAPACITY " + str(trainList[_name][4]) + "\n"
  if trainList[_name][5] is not None:
    content += "#define var_" + _name + "_LOADINGSPEED " + str(trainList[_name][5]) + "\n"
  if trainList[_name][6] is not None:
    content += "#define var_" + _name + "_POWER " + str(trainList[_name][6]) + "\n"
  if trainList[_name][7] is not None:
    content += "#define var_" + _name + "_WEIGHT " + str(trainList[_name][7]) + "\n"
  if trainList[_name][8] is not None:
    content += "#define var_" + _name + "_INTRODUCTION date" + str(trainList[_name][8]) + "\n"

f = open("./generated/spec.pnml", "w")
f.write(content)
f.close()
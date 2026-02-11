3.0.0+
-----
 * Add: English changelog
 * Change: Changed the minimum version of NML to 0.8.1

2.10.1
-----
 * Add: Chinese (Simplified) translation (by [@Maicarons](https://github.com/Maicarons)) [#503]
 * Add: Chungcheongnam-do Provincial Government Railway [#495]
 * Add: Seoul Metro Line 5 5th batch, Line 8 4th batch (manufactured by Dawonsys) liveries
 * Change: Support for FIRS 5.x cargo
 * Change: Support for AXIS cargo
 * Fix: Incorrect display of Pasi 5 capacity in the purchase list [#499]
 * Fix: Corrected minimum version error

2.9.0
-----
 * Add: Postal car "Living Logistics Train" livery [#480]
 * Add: AREX All-stop train 4th batch livery [#438]
 * Add: Gyoeui Line liveries [#483, #488]
   - Can be implemented with the composition: "Class 4400 + Mugunghwa car + Mugunghwa car + Generator car + Class 4400 (flip with Ctrl+Click)"
 * Add: Pasi 5 Steam Locomotive 2024 Preservation Treatment livery [#489]
 * Add: Saemaeul-ho streamlined passenger car 1986-1993 livery, long-type 1990-1994 livery [#486, #487]
 * Change: Updated existing Saemaeul-ho liveries [#490]
 * Change: Support for Improved Town Industries cargo [#482]
 * Fix: Livery errors for Gyeongchun Line 2024 2nd batch and Gyeongui-Jungang Line 2024 batch [#481]
 * Fix: Issue where light rail common passenger cars were not applied to light rail vehicles
 * Fix: Inability to select Saemaeul White/Blue livery when combining Class 7000 + Saemaeul passenger cars [#485]

2.8.1
-----
 * Add: Gyeongchun Line 2024 2nd batch livery [#476]
 * Add: Gyeongui-Jungang Line 2024 batch livery [#477]
 * Fix: Issue where waypoint simplification function did not work
 * Change: Renamed "Daegu Metropolitan Railway" to "Daegyeong Line"
 * Fix: Graphic error in Bidulgi-ho Green/Yellow livery [#479]

2.8.0
-----
 * Add: Class 3x00 Diesel Locomotive [#198]
 * Add: Class 4x00 Diesel Locomotive [#198]
 * Add: Seoul Metropolitan Line 4 5th batch livery [#382]
 * Add: Daegu Metropolitan Railway [#415]
 * Change: Updated KTX-Eum graphics and templates
 * Change: Changed KTX-Eum locomotive power from 8800kW to 6080kW
 * Change: Renamed Class 4x00 Diesel Locomotive to Class 4400
 * Change: Moved Yongin Everline from Electric track to Light Rail track
 * Change: Changed available tracks for Light Rail vehicles when using [Korean Track Set](https://github.com/SerpensNebula/Korean-Tracks)
   - Busan Line 4, Sillim Line, Uijeongbu LRT
     → (When using Korean Track Set v1.6.0+) Available on all Korean Track Sets including "Rubber-tired Track" + "[KTS] Light Rail Track"
     → (When using Korean Track Set version below v1.5.0) Available on all Korean Track Sets including "Urban Railway (Above ground) Track" + "[KTS] Light Rail Track"
     → (When not using Korean Track Set) Available on "[KTS] Light Rail Track"
   - Busan-Gimhae LRT, Gimpo Goldline, Incheon Line 2, Ui-Sinseol Line, Yongin Everline
     → (When using Korean Track Set) Available on all Korean Track Sets including "Light Rail 3rd Rail Track" + "[KTS] Light Rail Track"
     → (When not using Korean Track Set) Available on "[KTS] Light Rail Track"
   - Daegu Line 3
     → (When using Korean Track Set v1.6.0+) Available on all Korean Track Sets including "Monorail Track" + "[KTS] Light Rail Track"
     → (When not using Korean Track Set) Available on "[KTS] Light Rail Track"
 * Change: Updated generator car graphics [#462]
 * Fix: Incorrect shading in the ↖ direction for Saemaeul DHC vehicles [#466]
 * Fix: Errors in generator car livery names and graphics [#462]
 * Fix: Livery name error for DEC Diesel Locomotive [#475]

2.7.1
-----
 * Add: Added KTX-Cheongryong [#469]
 * Change: Removed KTX-Eum livery refit following the addition of KTX-Cheongryong [#469]
 * Fix: Issue where vehicle connection limit parameter was not applied to some vehicles [#467]

2.7.0
-----
 * Add: Added Caboose [#224]
 * Change: Grouped SRT under KTX-Sancheon [#460]

2.7.0-RC1
-----
 * Add: Added GTX-A vehicle [#340]
 * Change: Updated CDC graphics [#434]
 * Change: Updated Dining/Cafe car graphics [#435]
 * Change: Updated 8000, 8x00, 8500 series Electric Locomotive graphics [#456]
 * Change: Updated 5000, 6x00, 7x00, 7600 series Diesel Locomotive graphics [#457]
 * Change: Updated Diesel Hydraulic Car (DHC, PP) graphics [#455]
 * Change: Updated KTX-1 graphics [#454]
 * Change: Removed vehicle flip flag (TRAIN_FLIP) (However, vehicle flipping is always possible in OpenTTD 13.0+ regardless of this flag)
 * Fix: Issue where 1970~1983 livery of Diesel Hydraulic Car (DHC, PP) was displayed as 'Superior Green'

2.6.2
-----
 * Fix: Issue where Bulk Cement wagons could not be attached to any locomotive
 * Fix: Issue where Tongil-ho passenger cars had maintenance costs

2.6.1
-----
 * Fix: Issue where pillars appeared on empty graphics for certain cargo on flatcars [#447]
 * Fix: Updated graphics for some Saemaeul-ho passenger cars [#430]
 * Change: Updated steam locomotive graphics and templates [#445]
 * Change: Renamed Mugunghwa-ho car liveries [#446]
 * Change: Corrected versioning error

2.6.0-RC2
-----
 * Fix: Adjusted ITX-Maum price and maintenance cost
 * Fix: ITX-Maum pantograph and tail light graphic errors [#444]
 * Change: Renamed NDC, DEC, EEC liveries [#443]

2.5.1
-----
 * Add: Added "Disable vehicle connection limits" parameter
 * Add: Added "Disable vehicle length limits" parameter
 * Add: Added ITX-Maum (EMU-150) [#307]
 * Add: Metropolitan Line 4 4th batch livery [#304]
 * Add: Metropolitan Line 8 3rd batch livery [#256]
 * Add: Busan Line 1 3rd generation livery [#363]
 * Add: Mugunghwa-ho old sleeper car livery [#220]
 * Add: Tongil-ho sleeper car livery [#421]
 * Add: Bulk Cement wagon [#372]
 * Add: Mugunghwa-ho old Cafe car livery (Livery F) [#367]
 * Change: Updated ITX-Saemaeul graphics, templates, and added 32bpp support [#428]
 * Change: Updated KTX-1 graphics and templates [#427, #437, #442]
 * Change: Updated Saemaeul-ho car graphics and templates [#429]
 * Change: Updated Mugunghwa-ho car graphics and templates [#430]
 * Change: Updated Tongil-ho car graphics and templates [#431]
 * Change: Updated Bidulgi-ho car and DC DMU graphics and templates [#432]
 * Change: Updated Gwangwang-ho car graphics and templates [#433]
 * Change: Updated Urban Railway vehicle graphics and templates [#441]
 * Change: Adjusted Urban Railway vehicle weights to the average of actual specifications [#80]
 * Change: Updated graphics and lengths of container flatcars and flatcars [#403, #157]
 * Change: Updated oil tanker graphics [#372]
 * Change: Buffer object now provides additional graphics for desert and snow terrain [#425]
 * Change: Updated small parcel car liveries [#389]
   - Removed all existing liveries
   - Added 9 new liveries: 3 types each for Parcel-only 1999, Parcel-only 1998, and Boxcar-converted liveries
   - Added graphics based on load ratio
 * Fix: Alignment error in the ↖ direction for Seoul Metropolitan Line 1, Commuter - 371k unpainted vehicle [#416]
 * Fix: Issue where oil tankers carried kaolin in FIRS Sub-arctic basic mode [#426]
 * Delete: Deleted some Seoul Metropolitan Line 1 liveries as announced in 2.5.0
   - Korail 371k, 381k 1st batch → Moved to Donghae Line vehicles
   - Korail 381k 2nd batch → Moved to Donghae Line vehicles
   - Korail 391k 1st batch → Moved to Seohae Line vehicles

2.5.0
-----
 * Add: Seoul Metropolitan Line 3 2022 Woojin Industrial Systems batch livery [#375]
 * Add: Seohae Line 2nd batch livery [#260]
 * Change: Added "Metropolitan Railway" vehicle category and separated/grouped some line vehicles [#301, #398, #406]
   - Suin-Bundang, Gyeongchun, Shinbundang: Moved under "Metropolitan Railway" grouping
   - Seohae Line, Donghae Line: Newly established independently from Seoul Metropolitan Line 1 vehicles (Existing Line 1 liveries maintained for compatibility)
   - "Metropolitan Railway" category appears at the same time as the Suin-Bundang Line (1993), which has the earliest introduction year
 * Change: Grouped some locomotives
   - 7000, 7x00, 7600 series Diesel Locomotives → Grouped as 7x00 series
   - 8000, 8x00, 8500 series Electric Locomotives → Grouped as 8x00 series
   - Grouped standard gauge steam locomotives into "Steam Locomotive" category
 * Change: Adjusted NDC capacity [#407]
 * Change: Removed maintenance costs for passenger/freight cars [#414]
 * Change: Updated minimum supported OpenTTD version to 13.0 / JGRPP-0.53.0
 * Change: Marked some Seoul Metropolitan Line 1 liveries for future deletion
   - Korail 371k, 381k 1st batch → Scheduled to move to Donghae Line vehicles
   - Korail 381k 2nd batch → Scheduled to move to Donghae Line vehicles
   - Korail 391k 1st batch → Scheduled to move to Seohae Line vehicles
 * Fix: Issue where narrow gauge open wagons lacked empty graphics [#397]
 * Fix: Incorrect headlight display on 8x00, 8500 series locomotives [#399]
 * Fix: Adjusted narrow gauge vehicle offsets [#401]
 * Fix: Issue where steam emitted from the tender of narrow gauge Hyeogi 7 locomotive [#402]
 * Fix: Adjusted steam locomotive offsets [#347]
 * Fix: Issue where DEC 'Saemaeul-ho' livery name was placed in the wrong year [#411]
 * Fix: Adjusted refit costs for some vehicles

2.4.0
-----
 * Fix: Issue where boxcars and sleeper cars could not be attached to steam locomotives [#394]

2.4.0-RC2
-----
 * Add: Added KTX-Eum 320 [#368]
 * Change: Support for 3rd rail in Korean Track Set 1.3.0 [#391]
 * Change: Updated A-train passenger and generator car graphics [#361]
 * Change: Updated G-train passenger car graphics [#361, #387]
 * Change: 8-direction support for S-train passenger cars [#361]
 * Change: 8-direction support and graphic updates for Haerang passenger cars [#361]
 * Change: Updated mail car graphics [#390]
 * Change: Updated V-train passenger car graphics [#390]
 * Change: Adjusted capacity and weight of some freight cars [#291]
 * Fix: Corrected door positions on modified Saemaeul-ho passenger cars [#378]
 * Fix: Issue where maintenance costs were incorrectly calculated for passenger cars when attaching passenger cars (including motor cars) to some locomotives [#388]

2.4.0-RC1
-----
 * Add: Seoul Metropolitan Line 7 5th batch livery [#216]
 * Add: Seoul Metropolitan Line 3 2022 batch livery [#331]
 * Add: Nuriro 2022 batch livery [#362]
 * Add: Incheon Line 1 2022 livery [#373]
 * Add: Seoul Metropolitan Line 1 2022 Woojin Industrial Systems batch livery [#345]
 * Change: Updated steam locomotive graphics [#276]
 * Change: Updated Sillim Line front design [#343]
 * Change: Disabled double-heading for Sillim Line vehicles due to graphic sprite alignment issues [#344]
 * Change: Changed ITX-Saemaeul locomotive power from 6000kW to 3000kW [#342]
 * Change: Adjusted length of 7x00 series locomotives [#350, #351]
 * Change: Adjusted length and updated graphics for 7000 series locomotives [#353]
 * Change: Adjusted length and updated graphics for 5000, 6x00 series locomotives [#352]
   - Known Issue: Gaps appearing between locomotives when flipping the rear locomotive with Ctrl+Click after double-heading
 * Change: Adjusted length and updated graphics for 8x00, 8500 series locomotives [#359]
 * Change: Improved/fixed graphics and added 8-direction support for ITX-Saemaeul, KTX-1, SRT, and KTX-Eum passenger cars [#376, #377]
 * Change: Randomized Single-arm/Double-arm pantographs for Metropolitan Line 4 2019, 2022 batch trains [#380]
 * Fix: Adjusted Sillim Line vehicle capacity [#336]
 * Fix: Incorrect Korail logo position on specific Mugunghwa-ho passenger car liveries [#341]
 * Fix: Sillim Line boarding speed bug [#354]
 * Fix: Color error in the ↑ direction for S-train [#360]
 * Fix: Corrected Mugunghwa-ho and Cafe car liveries and door positions [#357, #358]
 * Fix: Issue where KTX-Eum car 2 was displayed as a middle car [#371]
 * Fix: Incorrect introduction year for Sillim Line [#381]

2.3.0
-----
 * Add: Sillim Line [#16]
 * Change: Adjusted introduction years for some passenger cars [#299]
   - Tongil-ho cars: 1984 → 1963
   - Mugunghwa-ho cars: 1972 → 1970
   - Saemaeul-ho cars: 1984 → 1969
 * Fix: Issue where narrow gauge freight car maintenance costs were excessively higher than standard gauge [#334]

2.2.1
-----
 * Fix: Issue where boxcars were not affected by parameters [#321]
 * Fix: Adjusted graphic positions for Seoul Metropolitan Line 1, Commuter unpainted vehicles, and '371k, 381k 1st batch' vehicles [#322, #327]
 * Fix: Issue where length was always short when attaching a generator car to 7x00 series [#324]
 * Fix: Issue where capacity displayed as 1 when attaching a dining car to Saemaeul DHC motor cars [#325]

2.2.0
-----
 * Change: Updated KTX-Eum graphics using 32bpp for more realism [#319]
 * Change: [FIRS] Removed pillar graphics from empty flatcars when refitted to Farm Supplies or Engineering Supplies [#257]
 * Change: [FIRS] Changed Vehicle Parts (VPTS) to be carried by container cars instead of flatcars [#296]
 * Change: Adjusted horizontal graphic length of Saemaeul-ho cars and improved ITX-Saemaeul graphics [#313]
 * Fix: Issue where smoke emitted from the tender of steam locomotives [#266]
 * Fix: Issue where some freight cars lacked speed limits [#314]
 * Fix: Issue where some batch refits for Gwangwang-ho were not applied [#317]
 * Fix: Passenger capacity issue in Gwangwang-ho dining cars [#318]

2.2.0-rc1
-----
 * Add: Seoul Metropolitan Line 1 371K company color livery [#271]
 * Add: Gwangwang-ho livery for 7x00 series locomotives [#241, #250]
 * Add: 6x00 series locomotives (+ Gwangwang-ho livery) [#250]
 * Add: Boxcars [#138]
 * Change: Updated length and graphics for 5000 series locomotives [#250]
 * Change: [FIRS] Removed pillar graphics when flatcars (stake cars) carry Engineering Supplies (ENSP) or Farm Supplies (FMSP) [#257]
 * Change: Improved Busan Metro train graphics [#270]
 * Change: Improved Korail EMU graphics [#271]
 * Change: Improved and added sprites for Korail EMUs (2019, 2021 batches) [#295]
 * Change: Updated Uijeongbu LRT graphics [#283]
 * Change: Updated 7x00 series and 8000 series locomotive Blue/White livery graphics [#241]
 * Change: Improved Urban Railway EMU graphic sprites [#240, #303, #311]
   * Busan Line 1 2nd batch, Busan Line 3, Daegu Line 2, Daejeon Line 1, Gwangju Line 1, Incheon Line 1 VVVF 1st generation, Seoul Line 2 VVVF 3rd generation
     Metropolitan Line 1 2019·2021 batch, Metropolitan Line 4 2019·2021 batch, 351K 2021 batch, 37·381K 1st generation
     Metropolitan Line 1 Rheostat control vehicles Initial/Middle/Late types
 * Fix: Fixed pantograph error on Line 2 modified rheostat (chopper) vehicles [#245]
 * Fix: Corrected rooftop AC unit count for CDC trains [#255]
 * Fix: Bug where some graphics in certain directions for brown flatcars remained blue [#262]
 * Fix: Corrected rooftop AC unit count for Metropolitan Line 4 2nd generation VVVF trains from 1 to 2 [#267]
 * Fix: Corrected rooftop AC unit count for Metropolitan Line 3 3k VVVF old livery from 2 to 1 [#268]
 * Fix: Corrected rooftop AC unit count for Suin-Bundang Line 1st generation new livery rear car ↖ direction from 1 to 2 [#281]
 * Fix: Incorrect rooftop AC unit count for Seoul Metro 1k, 4k vehicles in specific rear directions [#269]
 * Fix: Issue where ITX-Saemaeul train capacity differed from reality [#263]
 * Fix: Incorrect smoke position for NDC DMUs [#264]
 * Fix: Issue where the order of double-decker cars in ITX-Cheongryun was swapped [#273]
 * Fix: Issue where Uijeongbu LRT used standard electric track instead of light rail track [#282]
 * Fix: Improved some EMU graphic sprites
   * SMETRO_1K_RHEO_FIRST, 2K_CHOPPER, 3K_SMETRO_CHOPPER, 3K_SMETRO_MODIFIED_CHOPPER [#305]
   * Busan-Gimhae LRT, Gimpo Goldline, Ui-Sinseol Line [#306]
   * 3K_VVVF_1ST_2 [#308]
 * Remove: Removed speed limit for Bidulgi-ho passenger cars

2.1.0
-----
 * Add: 762mm narrow gauge track and level crossings [#204, #229]
   * Add: Hyeogi 7 Steam Locomotive [#205]
   * Add: Narrow gauge passenger car [#205]
   * Add: Narrow gauge motor car [#205]
   * Add: Narrow gauge boxcar [#215]
   * Add: Narrow gauge open wagon [#217]
 * Add: Tunnel graphics for light rail/narrow gauge tracks in sub-arctic and sub-tropical climates [#66]
 * Add: Saemaeul-ho old generator car (Red + Blue) livery [#232]
 * Add: Tongil-ho old generator car livery [#233]
 * Add: Japanese translation
 * Change: Aligned purchase list images to the left and added icons for locomotive types (e.g., Steam, Diesel, Electric, EMU) [#209]
 * Change: Unified position standards for all graphic sprites [#252]
 * Change: Added Class 2x00 US Army livery and Black+Wide Orange livery [#90]
 * Change: Reduced generator car length to 6/8 or 7/8 scale [#117]
 * Change: Improved Saemaeul-ho Diesel Hydraulic Car (DHC, PP) graphics [#187]
 * Change: Mater 2 weight [#208]
 * Change: Updated steam locomotive graphics and length [#210]
 * Change: Uijeongbu LRT graphics [#211]
 * Change: Incheon Airport Maglev graphics [#211]
 * Change: Renamed Bidulgi-ho commuter diesel car to 'DC DMU' + Added various liveries + Linked refit capability with Bidulgi-ho passenger cars [#221, #219]
 * Change: Increased G-train car directions from 4 to 9 [#223]
 * Change: Added GEC CHOPPER livery to Metropolitan Line 4 [#230]
 * Change: Randomized Single-arm or Double-arm pantographs on Suin-Bundang Line
 * Change: Removed "[KTS]" prefix from vehicle names
 * Fix & Change: Issue where Metropolitan Line 4 1st/2nd batch liveries used Line 3 liveries instead [#83]
 * Fix & Change: Corrected Nuriro pantograph direction + Improved Nuriro graphics [#140]
 * Fix: Corrected CDC Gyeongbuk Tour Theme Train graphic shading and passenger car order for old livery [#212]
 * Fix: Issue where NDC purchase image showed old livery
 * Fix: Issue where KTX-Eum capacity was doubled [#206]
 * Fix: Adjusted pantograph positions for historical accuracy [#231]
 * Fix: Issue where 'Korail 311k / Initial Livery' sprite was displayed as 'Korail 311k Initial / Current Livery' [#234]
 * Fix: Issue where Bidulgi-ho passenger car capacity was doubled

2.0.4
-----
  * Fix: Corrected dark areas in East-West graphics for Busan Line 1 2nd generation vehicles [#200]
  * Fix: Corrected graphic positioning for Daegu Line 3 [#202]
  * Fix: Issue with slow cargo loading speed for some light rail vehicles [#203]
  * Fix: Issue where Gyeongui-Jungang Line bicycle livery train appeared when refitting to Seoul Metro modified rheostat vehicles [#192]
  * Change: Improved Seoul Metropolitan Subway Line 5 VVVF 4th generation graphics [#193]
  * Change: Improved Class 4x00 Diesel Locomotive graphics [#137]
  * Fix: Issue where some trains/cars could not be attached to Class 2x00 Diesel Locomotives

2.0.3
-----
  * Add: Class 2x00 Diesel Locomotive [#90]
  * Add: Class 5·6000 Diesel Locomotive [#176]
  * Add: Mugunghwa-ho dining car (1980s livery) [#185]
  * Add: Saemaeul-ho dining car (Current Korail livery) [#184]
  * Add: Two 7000 series Diesel Locomotive liveries [#188]
  * Add: Saemaeul-ho First Class (Initial Railroad Administration livery) [#184]
  * Change: Increased Saemaeul-ho car graphics from 4 directions to 8 directions [#184]
  * Change: Improved Busan Line 1 old livery graphics [#183]
  * Change: Improved Mugunghwa-ho car graphics [#180]
  * Change: Improved batch livery refit for mixed formations of Mugunghwa-ho cars, Cafe cars, and CDC
  * Fix: Corrected pantograph vehicle offset for Seoul Metropolitan Line 1/4 2019 batch (aka. Judungi)
  * Fix: Corrected some documentation

2.0.2
-----
  * Add: Saemaeul-ho First Class (Old livery, Recent livery) [#118]
  * Add: Flatcar Black and Brown liveries [#173]
  * Add: Mugunghwa-ho First Class [#113]
  * Add: Sleeper car [#123]
  * Change: Added Line 4 VVVF 1st generation livery to Bundang Line [#156]
  * Fix: [FIRS] Issue where empty cars showed loaded graphics when carrying FMSP or ENSP cargo [#160]
  * Fix: Corrected line position in East-West graphics for Seoul Metropolitan Line 7 4th batch [#165]
  * Fix: Corrected South offset error for KTX-Eum rear pantograph vehicle [#166]
  * Fix: Issue where open wagon purchase image differed from the basic graphic [#158]
  * Fix: Corrected graphic offset position for open wagons [#159]
  * Fix: Corrected Daegu Line 1 and 2 graphic errors [#151]
  * Fix: [FIRS 3.x] Issue where open wagons could not carry Sugar Beet (SGBT) [#171]
  * Fix: Corrected graphic order for FMSP and ENSP cargo on [FIRS] flatcars [#167]
  * Fix: Graphic and offset errors for KTX-Sancheon and SRT [#169]
  * Fix: Diesel smoke position for CDC and NDC was too far forward [#170]
  * Fix: Issue where loading speed was not applied when attaching Mugunghwa cars to 7x00 or 7600 series [#162]
  * Fix: Slow loading speed for ITX-Cheongchun [#175]

2.0.1
-----
  * Fix: Issue where Mugunghwa-ho car capacity showed as 0 when attached to 7x00 or 7600 series locomotives [#153]
  * Fix: Weight error for Class 7600 [#154]
  * Fix: Corrected NDC livery order and re-sorted livery sequence [#155]
  * Fix: Issue where graphics for FMSP and ENSP cargo in FIRS were 4-directional instead of 8-directional [#152]
  * Doc: Fixed cut-off Github link in the introduction image and typos in the changelog [#150]

2.0.0
-----
  * Rebuilt the entire code from scratch
      - Changed folder and file structure
      - Changed build method to make
      - Now uses gcc and python3 for building
  * **Addition**
    * Steam Locomotives
      - Mika 3
      - Pasi 5
      - Mater 2
    * Class 7600 Diesel Freight Locomotive and Jeongseon Arirang Train [#7]
    * NDC Liveries
      - Business DMU
      - 1984~1994 Initial Livery
    * Diesel Electric Car (DEC) [#14]
    * Electric Car (EEC) [#15]
    * Re-added Gyeongui-Jungang Line Bicycle Train
    * Seoul Metropolitan Line 1 New Rheostat vehicle [#115]
    * Seoul Metropolitan Line 3 Modified Chopper vehicle [#10]
    * Seoul Metro 3000 series VVVF 2nd generation vehicle [#51]
    * Seoul Metro 5000 series 3rd batch vehicle [#11]
    * Seoul Metro 5000 series 4th batch vehicle [#41]
    * Seoul Metropolitan Line 4 VVVF 3rd batch (aka. Babtong) vehicle
    * Seoul Metropolitan Line 2 VVVF 4th batch (aka. Babtong) vehicle
    * AREX Express Orange livery [#6]
    * Nuriro Donghae Santa Train [#106]
    * Various Dining and Cafe car liveries
    * Uijeongbu LRT [#33]
    * Incheon Airport Maglev [#38]
    * KTX-Sancheon: Added 2018 Pyeongchang Winter Olympics livery [#81]
    * Bidulgi-ho passenger cars and DMUs
    * Oil tanker Silver and Black liveries
    * Added Flatcar (Stake car)
      - Cargo: Wood, Steel, Paper
    * Added Daegu Line 3 Late-type livery
    * Open wagons and flatcars now display different graphics based on cargo (FIRS supported)
  * **Change**
    * **Unified specific cars (e.g., KTX, Nuriro, CDC, Subway, etc.) into Passenger Common Car and Passenger Common Car (Motor Car)**
    * Removed freight car speed limit parameter [#59]
    * Updated Seoul Line 2 VVVF 3rd batch graphics [#47]
    * Busan Line 3 rooftop color
    * Unified Class 8100 and 8200 into 8x00 series locomotives
    * Changed ↔ direction graphic height for 7x00 series from 11px to 12px [#116]
    * Changed engine section horizontal length for NDC(+DEC+EEC) from 33px to 31px
    * Changed single locomotive purchase image from 2 cars to 1 car
    * Renamed Bundang Line to 'Suin-Bundang Line'
    * Separated Daejeon Line 1 and Gwangju Line 1
    * Implemented tunnel graphics for light rail tracks that were previously missing
    * Renamed existing 'Flatcar' to 'Container Flatcar'
      - Cargo: Fruit, Valuables, Goods, Food, Batteries, Toys
  * **Bug Fixes**
    * Issue where error messages appeared when cargo loading speed parameter was set to 32x [#20]
    * Issue where initial Line 1 vehicles were named 'Korail' instead of 'Railroad Administration' [#21]
    * Issue where Line 4 2019 batch (aka. Judungi) was placed under Seoul Metropolitan Line 1, Commuter [#22]
    * Historical introduction year error for Class 4400 and 7000 Diesel Locomotives [#25]
    * Changed power output of Class 7x00 and 4400 to actual values [#26]
    * Issue where open wagons carried livestock and parcel cars carried passengers [#27, #70]
    * Issue where Busan Line 1 had 4 doors instead of 3 [#42]
    * Issue where Metropolitan Line 1 'Middle Rheostat' livery was labeled as 'Modified Rheostat' [#60]
    * Issue where Metropolitan Line 3 3k VVVF 1st generation was mislabeled as 2nd generation [#75]
    * Historical introduction year error for Class 7x00 [#74]
    * Issue where Line 1 311k initial livery was labeled as New Rheostat [#72]
    * Issue where Line 3 livery names were incorrectly labeled [#82]
    * Shading on G-train
    * Shading on Class 4x00
    * Issue where CDC introduction year was 2010 instead of 1996
    * Issue where shading was inconsistent between RDC DMUs and passenger cars
    * Issue where door opening graphics were missing for Busan Line 4

1.6.13
-----
  * Renamed EMU-250 to "KTX-Eum" (20210105)

1.6.12
-----
  * Fixed issue where KTX passenger car speed was set to EMU-250 speed (20200209)

1.6.11
-----
  * Resolved loading speed issue for EMU-250 DMUs (20200205)

1.6.10
-----
  * Changed development versioning from r### to date (########) format (20191115)
  * Added EMU-250 motor and passenger cars (20191115)
  * Slightly changed Gimpo Goldline colors (20191115)

1.6.01
-----
  * Fixed graphic error for Incheon Line 2 (r181)

1.6.00
-----
  * Changed KTX-1 power from 5650kW to 6600kW (r176)
  * Changed KTX-Sancheon power from 5650kW to 4400kW (r176)
  * Changed KTX-Sancheon introduction year from 2004 to 2010 (r176)
  * Changed Light Rail exclusive vehicles to be usable on electric tracks (r177)
  * Fixed Ui-Sinseol LRT graphics (r178)
  * Deleted pantographs from Incheon Line 2 (r178)
  * Adjusted diagonal shading for Busan-Gimhae LRT, Ui-Sinseol LRT, and Incheon Line 2 (r178)
  * Added Yongin LRT (r179)
  * Added Gimpo Goldline (r180)
  * Added rear graphics for Busan-Gimhae LRT and Incheon Line 2 (r180)

1.5.70 (2019.09.15)
-----
  * Renamed Sosa-Wonsi Line livery in Line 1 to Seohae Line (r175)
  * Fixed issue where CDC and NDC sale prices were too low (CDC 2→6 / NDC 3→6) (r175)
    * Fixed flatcar graphics to change to steel wagons when carrying FIRS metal (r175)
  * Added "Judungi" livery (Line 1, Line 4, Donghae Line) (r176)

1.5.61 (2019.05.18)
-----
  * Fixed issue where Daegu Line 3 was not affected by light rail parameters (r171)
  * Fixed flatcar graphics to change when carrying steel (r172)
  * Added oil tankers (r173)
  * Enabled use in Toyland climate (r173)
  * Changed livery refit labels from A, B, C... to Black, Blue, etc. (r174)

1.5.50 (2019.01.31)
-----
  * Updated flatcars (r170, Thanks to skyu)
    - Changed basic flatcar graphics
    - Significantly increased random container types from 5 to 27
    (9 types of 40ft containers + 18 types of 20ft containers)
    - Flatcars can no longer carry passengers
  * Added freight car speed limit parameter (r171)
    - Allows disabling speed limits for freight vehicles exclusively for Korean Train Set

1.5.11 (2018.08.14)
-----
  * Renamed Line 1 vehicle: "Seoul Metropolitan Line 1, Commuter"

1.5.10 (2018.06.04)
-----
  * Updated Sosa-Wonsi Line livery
  * Removed animation colors

1.5.00 (2018.04.14)
-----
  * Updated from GRFv7 to GRFv8
    - Discontinued compatibility with Chillcore's Patch Pack
  * Allowed Saemaeul-ho passenger cars to be refitted to passenger car-type ITX-Saemaeul (r161)
  * Adjusted purchase list offset position for Busan Line 4 vehicles and cars (r161)

1.4.10 (2017.09.25)
-----
  * Fixed graphic offset error for KTX-Sancheon (Class 120k) adjusted in r146 (r158)
    - Rear section 7(←) raised by 1px
  * Internal code cleanup (r159)
  * Added Sosa-Wonsi Line livery (391k) (r160)
  * Changed pantograph positions for Line 1 liveries with default 4-car formation (371k, 381k) (r160)

1.4.00 (2017.05.06)
-----
  * Fixed graphic error in Busan Line 1 Dadaepo extension livery (r149)
  * Added new Sea Train livery for CDC (r150)
  * Fixed English typo in CDC Dolphin livery: Dolphine → Dolphin (r151)
  * Corrected other English translations (Thanks to Gimel) (r151)
  * Fixed graphic errors in CDC standard and RDC liveries (r152)
  * Renamed vehicle: "KTX-Sancheon" → "KTX-Sancheon, SRT" (r153)
  * Added Daegu Line 3 (r154)
    - Operable on monorail and light rail tracks
    - Capacity: Front/Rear (84 passengers), Middle car (97 passengers)
    - Max speed: 70km/h
  * Slightly reduced maintenance costs for light rail (r155)
    - Target: Busan-Gimhae LRT, Ui-Sinseol Line, Busan Line 4
  * Changed website address (r156)
    - (Old) ``http://korct.com`` → (New) ``https://telk.kr``
  * Added Seoul Subway Line 2 new livery (r157)

1.3.60 (2017.01.20)
-----
  * Added Seoul Subway Line 2 modified rheostat livery (r147)
  * Added Busan Subway Dadaepo extension livery (r148)

1.3.51 (2016.10.30)
-----
  * Renamed vehicle: Metropolitan Line 2 → Seoul Line 2 (r145)
  * Fixed bug where KTX-Sancheon sprite was 1px higher than intended (r146)
  * Removed temporary text for flatcars and Incheon Line 2

1.3.50 (2016.07.23)
-----
  * Corrected Class 8200 introduction year from 1990 to 2002 (r143)
  * Fixed bug where AREX All-stop/Express trains applied speed parameters inversely (r142)
  * Added Daejeon/Gwangju Subway Line 1 vehicles (r140, r141)
    - Basic exterior is Daejeon Line 1; Gwangju Line 1 is available via livery refit

1.3.20 (2016.05.05)
-----
  * Fixed sprite bug for Metropolitan Line 1 3xxk AL livery (r139)
  * Added Metropolitan Line 1 371k livery (unpainted version) (r137)
  * Added Metropolitan Line 1 381k livery (r138)

1.3.01 (2016.04.14)
-----
  * Updated readme.txt and readme_en.txt
  * Fixed KTX-1 and KTX-Sancheon to prevent coupling together (r136)
  * Unified/Changed CDC motor and passenger car introduction years to 1996 (r135)

1.3.00 (2016.02.14)
-----
  * Temporarily added "KTS Seoul Ui-Sinseol LRT" (r134)
    - Composition: Ui-Sinseol LRT Motor car + Ui-Sinseol LRT Motor car
    - Max speed: 80km/h
    - Capacity: 80 passengers
  * Temporarily added "KTS Incheon Line 2" (r133)
    - Composition: Incheon Line 2 Motor car + Incheon Line 2 Motor car
    - Max speed: 90km/h
    - Capacity: 100 passengers
  * Unified internal IDs used for Incheon Line 1 (r131)
  * Added "KTS Busan-Gimhae LRT" (r130)
    - Composition: Busan-Gimhae LRT Motor car + Busan-Gimhae LRT Motor car
    - Max speed: 80km/h
    - Capacity: 96 passengers
      (Busan-Gimhae LRT, Incheon Line 2, and Ui-Sinseol LRT are only usable on 3rd rail tracks if a NewGRF (e.g., Metro Track Set) is used. Otherwise, usable on electric tracks.)
  * Thanks to 라스 for Graphics

  * Fixed bug where non-KTX cars could be attached to KTX motor cars (r132)
  * Unified/Changed CDC motor and passenger car introduction years to 2004 (r129)
  * Fixed some incorrect colors in graphics
  * Changed graphic sprite IDs

1.2.52 (2016.01.23)
-----
  * 1.2.52
    * Temporarily restored Japanese translation (r128)
    * Fixed the following for Mugunghwa-ho RDC Cafe car (r127)
      - Corrected reversed shading direction in the ↖ front graphic
      - Fixed Cafe car appearing slightly brighter than regular cars
  * 1.2.51
    * Fixed ↖ offset for KTX-Sancheon rear graphic (r126)
    * Temporarily removed (r126):
      - Parts of Japanese translation
      - 2 types of "Gyeongui-Jungang Line Bicycle Train" livery (forward, reverse)
    * Changed NewGRF display name from "Korean Train Set v#.#.##" to "Korean Train Set #.#.##" (r126)
    * Unified KTX common car introduction years from 1970 to 2004 (r125)

1.2.50 (2015.12.16)
-----
  * Added "Daegu Subway Line 2" vehicle
  * Fixed a subtle line appearing on Line 1 vehicles
  * Fixed swapped positions of red and green lines in Seoul Metro 1000 series VVVF graphics
  * Fixed bright color artifact on the bottom of Daegu Line 1 vehicles
  * Linked website addresses in NewGRF to language-specific pages

1.2.41 (2015.11.20)
-----
  * 1.2.41
    * Renamed vehicles:
      - "Line 1, Gyeongui-Jungang Line" → "Line 1, Gyeongui-Jungang Line, Suin Line"
    * Fixed Japanese translation
    * Updated readme.txt and readme_en.txt
  * 1.2.40
    * Added "Daegu Subway Line 1" vehicle
    * Added 2 types of "Gyeongui-Jungang Line Bicycle Train" livery (forward, reverse)
      - Available by refitting Line 1, Gyeongui-Jungang, Suin Line vehicles.

1.2.30 (2015.10.07)
-----
  * 1.2.30
    * Added light rail speed increase parameter (Currently applied to Busan Line 4)
    * Changed parameter order (Requires reset)
    * Updated/removed outdated parameter descriptions
  * 1.2.21
    * Fixed bug where company colors were included in various trains

1.2.20 (2015.10.04)
-----
  * 1.2.20
    * Added 2 types of CDC "Gyeongbuk Tour Theme Train Livery"
    * Added "Busan Subway Line 3" vehicle
    * Added 'Seoul Metropolitan' prefix to Line 1 ~ Line 9 names
  * 1.2.03
    * Fixed bug where Metropolitan Line 4 Seoul Metro livery disappeared
    * Fixed bug where Mugunghwa-ho 1970s livery disappeared
    * Fixed DMZ-train rooftop color
    * Corrected ↖ shading for current CDC front livery

1.2.01 (2015.09.03)
-----
  * 1.2.01
    * Fixed bug where Busan Subway Line 2 graphics appeared as Busan Line 1
  * 1.2.00
    * Added "KTS Parcel Car" (7 liveries)
      - Cargo: Mail, Grain, Paper
      - Capacity: 30 units
    * Added Saemaeul-ho "Mugunghwa-ho Downgraded Old Special Livery"
      - Creation: Refit from Saemaeul-ho passenger car
    * Added Nuriro "Hallyu Tour Theme Livery"
      - Creation: Compose * Nuriro Motor + * Nuriro Car + * Nuriro Motor, then refit
    * Added "Namdo Sea Tour Train (S-train) Livery"
      - Creation: Compose * K7x00 Diesel Loco + * Mugunghwa Car + ..., then refit
    * Added "West Sea Golden Train (G-train) Livery"
      - Creation: Compose * K7x00 Diesel Loco + * Mugunghwa Car + ..., then refit
    * Added "Peace Train (DMZ-train) Livery"
      - Creation: Refit from CDC
    * Fixed subtle company colors appearing in subways
  * 1.1.00
    * Added Incheon Line 1 "2nd Livery (Songdo Extension)"
    * Added "KTS 4400 series Diesel Locomotive" (3 liveries)
      - Refits: Old Korail / New Korail / V-train
      - Max speed: 100km/h
    * Added "Baekdudaegan Canyon Train (V-train) Livery"
      - Loco max speed: 100km/h
      - Passenger car max speed: 60km/h
      - Capacity: Car (3n-2) 56, Car (3n-1) 46, Car (3n) 46
      - Composition: * 4400 Diesel (Refit) + * Parcel Car (Refit) + ...
    * Added "KTS 7000 series Diesel Locomotive"
      - Max speed: 150km/h
    * Fixed bug where Mugunghwa car purchase image showed old livery
    * Reserved slots in parameters
  * 1.0.12
    * Adjusted graphic sprite positions
    * Commented out unused sprite declarations

1.0.11 (2015.07.15)
-----
  * 1.0.11
    * Adjusted output for following train:
      - ITX-Saemaeul: 800kW → 3000kW

1.0.10 (2015.07.14)
-----
  * 1.0.10
    * Added " * KTS Hopper Car"
      - Speed limit: 130km/h
      - Cargo: Coal, Iron Ore, Copper Ore
      - Refit to 3 liveries (Blue, Brown, Black)
    * Changed flatcars to no longer carry passengers or mail
    * Updated internal code for freight vehicles
    * Adjusted speeds for following trains:
      - Class 8000 Electric Locomotive: 150km/h → 90km/h
      - ITX-Cheongchun: 180km/h → 190km/h
    * Updated and corrected readme.txt and readme_en.txt
  * 1.0.02
    * Fixed bug where AREX was affected by loading speed instead of cargo capacity parameter

1.0.01 (2015.05.05)
-----
  * 1.0.01
    * Fixed bug where subway cars attached to most motor cars didn't apply cargo capacity parameter, showing 'None'
  * 1.0.00
    * Added KTX-Sancheon 120k (KTX-Dalian) livery (Thanks to 라스)
      - Available via KTX-2 Sancheon front refit, specs same as Sancheon
    * Updated KTX-Sancheon 110k livery (Thanks to 라스)
    * Added Busan Subway Line 1
    * Added Busan Subway Line 2
    * Added Busan Subway Line 4
      - Added light rail tracks; future compatibility with Uijeongbu, Yongin LRT, Daegu Line 3, etc.
    * Changed default purchase cost parameter to 1/4 level
    * Renamed some vehicles
      - "Gyeongchun Line 368k ITX-Cheongchun" → "ITX-Cheongchun (Gyeongchun Line 368k)"
      - Removed VVVF term from names
      - Simplified other names
    * Enabled installation of track buffer objects on slopes

  * 0.9.38
    * Changed code for waypoint simplification

0.9.37 (2015.02.21)
-----
  * 0.9.37
    * Adjusted output for following train:
      - ITX-Cheongchun: 800kW → 2000kW
  * 0.9.36
    * Lowered default cargo capacity for all trains to roughly half
    (Exception: Flatcars 100 → 25)
    * Increased purchase and maintenance costs for most trains
    * Fixed subway to apply purchase and maintenance cost parameters

0.9.35 (2015.02.09)
-----
  * 0.9.35
    * Added Track Buffer object
    : Constructible via 'Object Construction' in Landscaping window
    * Re-adjusted outputs for:
      - NDC: 231kW → 1000kW
      - CDC: 261kW → 800kW
      - 7x00: 2800kW → 3000kW
      - Nuriro Motor: 500kW → 2000kW

0.9.34 (2014.12.15)
-----
  * 0.9.34
    * Fixed bug where cargo capacity parameter was not applied to:
      - All Subways
      - ITX-Saemaeul DMUs
    * Cleaned up redundant source code
    * Updated Readme

  * 0.9.33
    * Fixed bug where NDC was recognized as an electrified vehicle

0.9.34 (2014.11.28)
-----
  * 0.9.34
    * Fixed bug where cargo capacity parameter was not applied to:
      - All Subways
      - ITX-Saemaeul DMUs
    * Cleaned up redundant source code
  * 0.9.32
    * Further adjusted subway graphic sprite positions
    * Fixed graphic sprite error for Line 1 (Korail 311k / Current livery)
      - Fixed missing rear red lights
      - Fixed single pixel color error
    * Re-adjusted outputs for:
      - KTX-1: 1130kW → 5650kW
      - KTX-Sancheon: 1100kW → 5650kW
      - ITX-Cheongchun: 500kW → 800kW
      - ITX-Saemaeul: 500kW → 800kW
    * Changed NDC minimum formation from 4 to 2 cars
    * Reflected update history in Readme

0.9.31 (2014.11.28)
-----
  * 0.9.31
    * Adjusted subway graphic sprite positions
    * Adjusted Nuriro passenger car purchase list sprite position
  * 0.9.30
    * Added NDC DMU (Uses Mugunghwa cars)
    * Adjusted outputs for:
      - KTX-1: 13560kW → 1130kW
      - KTX-Sancheon: 13560kW → 1100kW
      - CDC: 2000kW → 545kW
      - Nuriro Motor: 3500hp → 500kW(≒670hp)
      - ITX-Cheongchun: 3000hp → 500kW
      - ITX-Saemaeul: 4021hp → 500kW

0.9.20 (2014.09.13)
-----
  * 0.9.20 (2014.09.13)
    * Added Spanish Translation (Thanks to SilverSurferZzZ)
    * Changed Nuriro graphic sprites
    * Added O-train (Available via Nuriro refit)
    * Fixed 2nd company color used in some sprites
  * 0.9.11 (2014.08.23)
    * Fixed bug where ITX-Saemaeul refit option appeared on Saemaeul-ho DMUs
    * Fixed changelog.txt display format

0.9.10 (2014.08.22)
-----
  * 0.9.10 (2014.08.22)
    * Fixed bug where back half of KTX-1 appeared as regular cars when all cars were refitted to First Class
    * Fixed incorrect parameter coefficient application
    * Added parameter to adjust cargo loading speed
    * Lowered default loading speed for all trains to roughly half
      - Saemaeul DMU: 10 → 5
      - ITX-Saemaeul DMU: 20 → 5
      - Nuriro Motor/Car: 20 → 10
      - CDC Motor/Car: 50 → 20
      - KTX Car: 20 → 5
      - Saemaeul Car: 60 → 10
      - Mugunghwa Car: 20 → 5
      - Cafe Car: 20 → 5
      - Tongil Car: 10 → 5
      - Generator Car: 10 → 5
      - Flatcar: 20 → 5
      - All Subways: 50 → 20
      - ITX-Cheongchun: 20 → 10
      - AREX: 20 → 10

0.9.02 (2014.07.31)
-----
  * 0.9.02 (2014.07.31)
    * Adjusted KTX-Sancheon sprite positions and colors
  * 0.9.01 (2014.07.29)
    * CDC
      - Harmonized colors for some livery sprites
      - Fixed explosion cycling colors in some liveries
      - Fixed color error in Dolphin theme livery
    * Fixed KTX-Sancheon sprites
  * 0.9.00 (2014.06.13)
    * Added Japanese Translation
    * Changed Mugunghwa Cafe car to Common Cafe car and applied:
      - Fixed Common Mugunghwa Cafe car sprites
      - Added Saemaeul-ho Cafe car livery to Cafe car
    * Corrected livery names:
      - CDC: Kkotdongsan Livery → Kkotdongsan Theme Livery
      - CDC: Sea Tour Train Livery → Dolphin Theme Livery
    * Added Sea Tour Train livery to CDC
    * Preliminary work for future Flatcar (Container) addition
    * Fixed following errors:
      - Nuriro Motor loading speed (10 → 20)
      - CDC (Sea Tour Train) sprite error
      - CDC (Mugunghwa) sprite color adjustment
    * Added speed limits to following cars (based on default):
      - Saemaeul Car: 150km/h
      - Mugunghwa Car: 130km/h
      - Tongil Car: 120km/h
      - CDC Car: 110km/h
    * Renamed NewGRF (Korea Train Set → Korean Train Set)
    * Renamed NewGRF file (ko_train.grf → ko_train_set.grf)
    * Changed distribution URL: http://telk.kr/ottd/newgrf/ko_train_set/
  * 0.8.50
    * Added following CDC liveries:
      - Kkotdongsan Livery
      - Sea Tour Train Livery
      - Korail 100th Anniversary, Baekje Crown Commemorative Livery
      - Old Railroad Admin Livery (Green+Yellow)
      - Mugunghwa RDC Livery
    * Renamed vehicles and liveries:
      - CDC → Commuter Diesel Car (CDC)
      - Saemaeul DHC → Saemaeul Diesel Hydraulic Car (DHC)
      - 7x00 Early RR Admin Livery (Tiger) → 7x00 Early RR Admin Livery (Black+Orange)
    * Changed CDC vehicle order
    * Added CDC passenger car
  * 0.8.41
    * Corrected 7x00 series Diesel Loco English name (Electric → Diesel)
    * Cleaned up CDC sprites
      - Removed unnecessary CDC sprites (pantograph cars)
      - Created CDC exclusive sprite template
      - Repositioned CDC sprites in the sprite sheet

0.8.40 (2014.04.30)
-----
  * 0.8.40 (2014.04.30)
    * Added following 7x00 series Diesel Loco liveries:
      - Early RR Admin (Blue+White)
      - Early RR Admin (Tiger)
      - Old RR Admin (Green+Yellow)
      - Freight Livery
    * Fixed issue where double-deck cars disappeared when double-heading ITX-Cheongchun
    * Fixed issue where Nuriro rear car didn't flip automatically
    * Changed 7x00 internal ID (K7000 → K7x00)
    * Discontinued compatibility with 0.7.xx
  * 0.8.39
    * Fixed Haerang generator car appearing as dining car
    * Discontinued downloads for 0.7.xx
  * 0.8.38
    * Fixed maintenance cost appearing as 0 for all cars except subways in purchase list
    * Fixed subways having 10x higher purchase/maintenance costs than regular trains
    * Unified subway purchase prices
    * Code cleanup
    * Fixed changelog format
    * Corrected AREX name (Airport Railroad → Incheon Airport Railroad (A'REX))
  * 0.8.35
    * Removed passenger capacity from following locos and allowed refit without capacity:
      - 7x00 series Diesel
      - 8000 series Electric

0.8.34 (2014.04.13)
-----
  * 0.8.33
    * Adjusted ITX-Saemaeul loco capacity (20 → 45 passengers)
  * 0.8.34
    * Fixed ITX-Saemaeul loco capacity in purchase list (20 → 45 passengers)

0.8.32 (2014.04.12)
-----
  * 0.8.23
    * Internal code cleanup
  * 0.8.30
    * Added ITX-Saemaeul
      - Max speed: 150km/h
      - Capacity: Loco 20, Car 64
      - Composition: Attaching Saemaeul cars to ITX-Saemaeul loco automatically converts them
  * 0.8.31
    * Changed headlight color for rear locos
  * 0.8.32
    * Bug fixes

0.8.23 (2014.01.18)
-----
  * 0.8.23
    * Fixed unnatural Northeast sprite in Saemaeul-ho old livery
  * 0.8.22
    * Fixed Diesel/Electric loco speeds showing as 1/10 level in purchase list

0.8.21 (2013.12.28)
-----
  * 0.8.21
    * Added Haerang generator and cafe car liveries
    * Allowed batch refit for 7000 series and Mugunghwa cars to Haerang livery
  * 0.8.20
    * Changed cost/maintenance parameters from integer input to selection (x1/32 ~ x128)
    * Added cargo capacity option (x1 ~ x256)
    * Stopped KTX First Class from appearing automatically
    * Enabled KTX First Class via refit
    * Changed Tongil car capacity (72 → 76 passengers)
  * 0.8.12
    * Unified model names by removing 'Korail' from purchase window

0.8.11 (2013.12.23)
-----
  * 0.8.11
    * Improved refit descriptions beyond A, B, C...
    * Fixed company colors in 8000 series blue livery
    * Discontinued support for 0.7.08 and below
  * 0.8.10
    * Added Haerang refit to 7000 series
  * 0.8.08
    * Fixed 8000 series Electric unable to carry passengers (Loading speed: 0 → 10)

0.8.07 (2013.11.19)
-----
  * 0.8.07
    * Fixed bug where Saemaeul cars attached to regular locos (non-PP) couldn't change liveries
    * Allowed flipping Mugunghwa Cafe cars
  * 0.8.06
    * Added Generator Cars (4 liveries, 10 passengers)

0.8.05 (2013.10.27)
-----
  * 0.8.05
    * Adjusted KTX-Sancheon default max speed to 330km/h (same as KTX-1)
    * Adjusted default purchase price parameter from 10 to 3
  * 0.8.04
    * Fixed bug where Line 2 (SMetro 2k VVVF 1st) rear loco flipped incorrectly
    * Fixed KTX-Sancheon First Class position (moved back one car)
    * Added English Readme (readme_en.txt)

0.8.03 (2013.08.12)
-----
  * 0.8.03
    * Renamed Line 3 models:
      - SMetro 3k VVVF 1st gen → SMetro 3k VVVF 2nd gen
      - Reserved space for 1st gen; currently refits to newest livery
    * Fixed bug where ITX-Cheongchun front flipped on reversal

0.8.02 (2013.08.07)
-----
  * 0.8.02
    * Fixed Line 2 development year set to 1893
    * Fixed company colors in Line 1 initial livery
  * 0.8.01
    * Fixed bug where cloned refittable subways reverted to Line 1 default

0.8.00 (2013.08.04)
-----
  * 0.8.00
    * Changed subway system from individual listing to refit-based livery/model selection
      - Lines 1-4 separated; Lines 5-9 unified
      - Jungang and Gyeongui unified with Line 1
      - Gyeongchun, Bundang, Shinbundang, Incheon 1 remained separate
    * Removed auto-formation to allow double-heading
      - Rear cars for Saemaeul, Nuriro, KTX must be flipped with CTRL+Click
      - Locos in middle of formation can be flipped with CTRL+Click for double-heading
    * Removed STOP image for short trains
    * Changed some colors in Nuriro sprites
    * Restricted subway cars from being attached to non-subway trains
  * 0.7.61
    * Added vehicles:
      - Line 1 Korail 311k initial livery
      - Line 2 SMetro 2k Chopper
  * 0.7.60
    * Fixed Line 2 MELCO mislabeled as Chopper
  * 0.7.50
    * Cleaned up subway sprite files
  * 0.7.44
    * Corrected Nuriro English name: Nooriro → Nuriro
  * 0.7.43
    * Allowed Saemaeul DMUs to carry mail

0.7.42 (2013.07.30)
-----
  * 0.7.42
    * Increased Korail 7x00 series power (2237kW → 2800kW)
    * Added 2 old liveries for Saemaeul DHC(PP) locos
  * 0.7.41
    * Slightly increased CDC maintenance cost (18 → 21)

0.7.40 (2013.06.08)
-----
  * 0.7.40
    * Cleaned up internal code, sprites, and filenames
    * Renamed ko_trainset.grf to ko_train.grf
    * Added parameter to selectively add regular trains or subways
    * Updated readme.txt
  * 0.7.36
    * Added Korail KTX-Sancheon
   (Graphics: 라스, Max speed: 350km/h, Capacity same as KTX-1)

0.7.35 (2013.05.10)
-----
  * 0.7.35
    * Adjusted Korail 8x00 series sprite positions
    * Adjusted Korail Saemaeul DHC(PP) sprite positions

0.7.34 (2013.03.10)
-----
  * 0.7.34
    * Added parameter to toggle maintenance cost increase with vehicle age
    * Updated readme.txt

0.7.33 (2013.03.02)
-----
  * 0.7.33
    * Doubled default purchase price for all trains
    * Fixed maintenance costs to increase slightly with age
  * 0.7.32
    * Added Tongil-ho passenger car

0.7.31 (2013.02.02)
-----
  * 0.7.31
  * Fixed issue where CDC was replaced by Nuriro
  * 0.7.30
  * Added Korail 7x00 series (GT26CW)
  * Added Korail Nuriro
  * Adjusted Korail 8000 series max speed (90km/h → 100km/h)
  * 0.7.26
  * Absorbed TK Waypoint Simplification features (toggleable via parameter)

0.7.25 (2013.01.16)
-----
  * 0.7.25
  * Reduced tractive effort for all vehicles (Coefficient: 0.5 → 0.3)
  * Increased air resistance for all vehicles (Coefficient: 0.08 → 0.1)
  * Fixed x-coordinate alignment for ITX-Cheongchun sprites
  * 0.7.24
  * Reduced power for all subways (2880kW → 2000kW)
  * Updated changelog.txt format
  * 0.7.23
  * Assigned weight to subway common cars (0t → 15t)
  * Added 'Purchase cost coefficient' and 'Maintenance cost coefficient' parameters

0.7.22 (2013.01.06)
-----
  * 0.7.22
  * Renamed GRF from 'Korean Railroad Set' to 'Korean Train Set'
  * Fixed inconsistent AREX passenger counts
    (Unified Express: 48/car, All-stop: 100/car)
  * Added refit to allow Saemaeul and Mugunghwa cars to carry mail

0.7.21 (2012.12.24)
-----
  * 0.7.21
    * Adjusted CDC operating cost (ELECTRIC → DIESEL)
    * Re-adjusted ↖ and ↘ sprite positions for Saemaeul front/rear locos
  * 0.7.20
    * Added CDC Commuter Train
  * 0.7.19
    * Updated readme.txt
  * 0.7.15
    * Restricted operation of short trains (displaying STOP image) and added error output
  * 0.7.13
    * Adjusted ↖ and ↘ sprite positions for Saemaeul front/rear locos (0.7.13)

0.7.12 (2012.12.09)
-----
  * Adjusted ↖ sprite position for K8x00 Electric
  * Adjusted ↖ sprite position for Mugunghwa car/Cafe car

0.7.11 (2012.11.25)
-----
  * Adjusted Saemaeul DHC(PP) rear sprite position
  * Fixed issue where AREX All-stop capacity didn't change

0.7.10 (2012.11.24)
-----
  * 0.7.10
    * Added Saemaeul PP DMU
    * Changed AREX All-stop capacity (48 → 100)
    * Adjusted tractive effort for 8x00 series and KTX-1 (0.5 → 0.3)
    * Changed KTX car cargo (Passengers → Passengers, Mail)
    * Updated Saemaeul car graphics
  * 0.7.09
    * Unified GRF name to 'Korean Railroad Set'

0.7.08 (2012.11.17)
-----
  * 0.7.08
    * Added Saemaeul car (New livery)
    * Added Mugunghwa Cafe car
  * 0.7.06
    * Corrected Mugunghwa car capacity (58 → 74)
  * 0.7.05
    * Separated common passenger cars into KTX, Saemaeul, and Mugunghwa cars
    * Corrected KTX-1 First Class count in fixed formation (3 → 4 cars)
  * 0.7.04
    * Corrected Gyeongchun Line 361k VVVF introduction date (2012 → Dec 21, 2010)
    * Reduced AREX (Express) operating costs
  * 0.7.03
    * Added Incheon Subway Line 1
  * 0.7.02
    * Changed versioning format (x.x.x → x.x.xx)
    * Discontinued compatibility with previous versions
    * Fixed bug where cars reverted to different locomotives upon version upgrade
      (Will be effective from next version; existing trains must be repurchased)
    * Assigned unique internal IDs to all vehicles to fix the above bug

0.7.1 (2012.10.07)
-----
  * Corrected vehicle names:
    - Korail 4k VVVF → SMetro 4k VVVF
    - Korail AREX 1k All-stop → Korail AREX 2k All-stop
    - Korail AREX 2k Express → Korail AREX 1k Express
  * Changed AREX max speed (130km/h → 120km/h)
  * Fixed issue where vehicles could be used on non-electrified tracks
  * Fixed bug where Line 9 Car 1 showed Car 4 graphics in fixed formation
  * Adjusted KTX-1 sprite positions

0.7 (2012.09.27)
-----
  * Released Beta version for external testing
  * Added fixed/free formation options and updated code
  * Added KTX vehicles
  * Fixed Mugunghwa car liveries to change by year

0.5
-----
  * Added following vehicles:
    - Metropolitan Subway Line 1 (Korail 1k Rheo, 3xxk VVVF, SMetro 1k Rheo)
    - Metropolitan Subway Line 2 (SMetro 2k Chopper, VVVF 1st/2nd)
    - Metropolitan Subway Line 3 (Korail 3k VVVF, SMetro 3k Chopper, VVVF)
    - Metropolitan Subway Line 4 (Korail 4k VVVF, 341k VVVF 1st/2nd gen)
    - Metropolitan Subway Line 5 (SMetro 5k VVVF)
    - Metropolitan Subway Line 6 (SMetro 6k VVVF)
    - Metropolitan Subway Line 7 (SMetro 7k VVVF, SR0x VVVF)
    - Metropolitan Subway Line 8 (SMetro 8k VVVF)
    - Metropolitan Subway Line 9 (SMetro9 9k VVVF)
    - Gyeongchun Line (361k VVVF, 368k ITX-Cheongchun)
    - AREX (1k, 2k)
    - Bundang Line (351k VVVF 1st/2nd/3rd gen)
    - Shinbundang Line (D000 VVVF)
    - Korail Class 8000 Electric Locomotive
    - Korail Class 8100 Electric Locomotive
    - Korail Class 8200 Electric Locomotive
    - Korail Class 8300 Electric Locomotive

0.2
-----
  * Alpha version production and internal review

0.1
-----
  * Initial NewGRF production
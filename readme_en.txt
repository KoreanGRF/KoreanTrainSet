================================================================================
                             Korea Train Set Readme
================================================================================


==========
List
==========
1. About
2. How to install and apply
3. FAQ
4. Known-bugs
5. Contact & Translation
6. Copyrights





1. About
==========
  This Korean Train Set has train vehicles of the Republic of Korea(South Korea)
incluing Seoul/Incheon/Busan metropolitan subways, KTX, KTX-Sancheons, Saemaeul,
Mugunghwa, Tongil, CDC(Cummutor Diesel Car), NDC(New Diesel Car), Nuriro,
ITX-Cheongchun, ITX-Saemaeul and so on.
('KTX' and 'ITX' stand for 'Korea Train eXpress' and 'Intercity Train eXpress', respectively.)


Korean Train Set adds vehicles such as below:
  - Seoul metropolitan subway Line 1 (Korail 1k Rheostatic, 3xxk VVVF, SeoulMetro 1k Rheostatic)
  - Seoul metropolitan subway Line 2 (SeoulMetro 2k MELCO, Chopper, VVVF 1st/2nd)
  - Seoul metropolitan subway Line 3 (Korail 3k VVVF, SeoulMetro 3k Chopper, VVVF)
  - Seoul metropolitan subway Line 4 (Korail 4k VVVF, 341k VVVF 1st/2nd)
  - Seoul metropolitan subway Line 5 (SeoulMetro 5k VVVF)
  - Seoul metropolitan subway Line 6 (SeoulMetro 6k VVVF)
  - Seoul metropolitan subway Line 7 (SeoulMetro 7k VVVF, SR0x VVVF)
  - Seoul metropolitan subway Line 8 (SeoulMetro 8k VVVF)
  - Seoul metropolitan subway Line 9 (SeoulMetro9 9k VVVF)
  - Seoul metropolitan subway Gyeongchun-line (361k VVVF, 368k ITX-Cheongchun)
  - Seoul metropolitan subway Airport Railroad (1k, 2k)
  - Seoul metropolitan subway Bundang-line (351k VVVF 1st/2nd/3rd)
  - Seoul metropolitan subway Sinbundang-line (D000 VVVF)
  - Seoul Ui-Sinseol LRT Line
  - Incheon subway Line 1 (1k 1st/2nd)
  - Incheon subway Line 2
  - Daegu subway Line 1
  - Daegu subway Line 2
  - Busan subway Line 1
  - Busan subway Line 2
  - Busan subway Line 3
  - Busan subway Line 4
  - Busan-Gimhae LRT
  - Korail 4400 Diesel Locomotive (2 models/paintings + V-train)
  - Korail 7x00 Diesel Locomotive (5 models/paintings + Haerang the rail cruise + G-train + S-train)
  - Korail 8000 Electric Locomotive (3 models/paintings)
  - Korail 8100 Electric Locomotive
  - Korail 8200 Electric Locomotive
  - Korail 8500 Electric Locomotive
  - Korail Commuter Diesel Car(CDC), RDC (6 models/paintings + DMZ-train + Gyeongbuk Circular theme tour train)
  - Korail New Diesel Car(NDC)
  - Saemaeul Diesel Hydraulic Car(PP-car) and coach (3 model/paintings)
  - ITX-Saemaeul and coach
  - KTX-1 and its passenger coach
  - KTX-Sancheon and its passenger coach
  - Nuriro Locomotive and coach (1 model/painting + O-train + Korean wave tour wrapping)
  - Mugunghwa's passenger coach and cafe coach
  - Tongil's passenger coach
  - Generator (4 model/paintings)
  - Flat cargo car
  - Luggage van
  - Hopper car

Korean Train Set adds a new railtype such as below:
  - [KTS] Light railway



2. How to install and apply
==========
  (1) Go to the folder where OpenTTD is installed(ex. C:\OpenTTD\)
  (2) Go to '/newgrf' or '/content_download/newgrf' folder
  (3) Move/Copy downloaded file(Korean_Train_Set-#.#.##.tar) without unzipping
      to 'newgrf' folder.
  (4) Run OpenTTD game, and click [NewGRF Settings]
  (5) Find 'Korean Train Set v#.#.##' in below list and click [Add].
  (6) Click [Parameter Setting] button to adjust train's speed or capacity and
      play the new game.



3. FAQ
==========
Q. It's too few that train added (or) There's no (painted) vehicle what I want!
A. Every model of train showed up until v0.7.x, but now there displays only
   certain representative vehicle on v0.8.x. If you want to make other model
   which is on the same/similar line, first you make a vehicle that is
   similar with what you want, then change its model into 'Refit' button when the
   train is in depot.
   Nevertheless, if vehicle what you want didn't display, wait until 2013. Every
   train of Korea Train Set introduced from 1970 to 2013.

Q. Some of trains (eg. Line 1) does not appear in the purchase list.
A. First check that the depot is for "Electrified Railway". Most of trains of
   Korean Train Set is for the electrified railway. Secondly, try to turn the
   'Vehicles never expire' setting on in the (Advanced) Setting window. Or, it
   might be caused by using duplicated vehicle ID between KTS and the other grf.

Q. How to construct a train in detail?
A. We recommend like below. CTRL+Click to reverse the engine in the tail(enclosed
   by <> in the list below)

   (1) Subways:         [Subway locomotive] + [subway coach] + ... + [subway coach] + [Subway locomotive]
   (2) ITX-Cheongchun:  [ITX locomotive] + [subway coach] + ... + [subway coach] + <ITX locomotive>
   (3) Mugunghwa/Saemaeul(K8x00, K7x00):
                        [Locomotive] + [Mugunghwa/Saemaeul passenger coach] + ...
   (4) Demoted to Mugunghwa, former executive car:
			[Locomotive] + [Saemaeul passenger coaches] + ...
			(Change by the refit)
   (5) Saemaeul(PP):    [PP locomotive] + [coach] + ... + [coach] + <PP locomotive>
   (6) KTX:             [KTX locomotive] + [KTX coach] + ... + [KTX coach] + <KTX locomotive>
   (7) NDC:             [NDC locomotive] + [Mugunghwa passenger coach] + ... + [NDC locomotive]

Q. What can I do in the parameter settings?
A. You can make the train's speed faster, or change the capacity larger.

Q. How to make double-head train?
A. Please construct the train like below (please CTRL+click the part enclosed by <>)
   : [Locomotive #1] + [coach] + … + [coach] + <Locomotive #1> + [Locomotive #2] + [coach] + … + [coach] + <Locomotive #2>

Q. It errors that the train is too short!
A. Some models(KTX, Saemaeul, subways etc.) must be more than two or four cars
   to run.

Q. Where is the passenger coach of ITX-Saemaeul?
A. You need to construct ITX-Saemaeul like below
   : [ITX-Saemaeul Locomotive] + [Saemaeul Passenger Car] + … + [Saemaeul Passenger Car] + [ITX-Saemaeul Locomotive]
   If you attach [Saemaeul passenger car] to [ITX-Saemaeul] engine, it changes
   into ITX-Saemaeul passenger car, automatically. If not, you can use refit
   button to change it.



4. Known-bugs
==========
+ The fact that the maximum speed of KTX is 331km/h, not 330km/h, and ITX is 181
  km/h, not 180km/h.
  : It comes from the problem of units between miles and kilometers.
    By the way, can you realize the difference of 1km/h? :D

+ The fact that is impossible to make [8x00 locomotive] + [subways]
  : I used a complex method to make subway's appearance naturally according to its
    length. It crashes with locomotives so that subway cars appears abnormally.
    I wish I could fix it, but it seems to be difficult.



5. Contact & Translation
==========
+ If you have found a bug or you have a sugguestion, please visit
  TELKLAND(http://telk.kr) or email to TELK(telk5093@gmail).
+ If you want to translate Korean Train Set and the download page of Korean Train Set
  into your language, please ask TELK(telk5093@gmail) as well.
+ Please ask TELK(telk5093@gmail.com) to get more information in English or Korean.



6. Copyrights
==========
- Code:		TELK (telk5093@gmail.com, http://telk.kr)
- Graphic:	TELK (telk5093@gmail.com, http://telk.kr)
		skyu (skyu2947@gmail.com)
		Las (wlq10000@naver.com)
		Chojeohang (yunggu7410@naver.com)
		OPENTRAIN (gks3900@naver.com)

  This NewGRF adds a lot of Korean trains on OpenTTD. The original author of sprites
used in this NewGRF is skyu and one of some sprites' is Las and TELK. The right of
raw source code to make this NewGRF into .grf file is belongs to TELK.
  This NewGRF is uploaded only on BaNaNaS(http://bananas.openttd.org/) and TELKLAND
(http://telk.kr) and shouldn't be uploaded on the place that TELK didn't allowed.
If you want to give a download link of this NewGRF on the place other than the both
place, please ask to TELK(telk5093@gmail.com).
  In addition, let you know that all authors of Korean Train Set is Korean user
so that their english is not so good. If you want to ask something in english,
please ask to TELK(OpenTTD Korean translator).
# Korean Train Set
[English](./README.md) | [한국어](./README.ko.md)

**Korean Train Set** is an OpenTTD NewGRF that offers various trains and railway of the Republic of Korea, a.k.a South Korea.   
You can download this via Online content in-game, or [Github release page](https://github.com/KoreanGRF/KoreanTrainSet/releases).

## Vehicle list and specifications
You can see the whole vehicle list and their specifications(speed, weight, power, etc.) at [this page](../docs/download_page/english.md).

## Development
### How to build
You need [NML](https://github.com/OpenTTD/nml), `make` and **Python 3** to build this NewGRF.  
Run `make` in terminal shell. If you are on Windows, open a command prompt and type `bash` before it.  
`make clean` will clean all generated & compiled files.

### Translations
First, please be aware that the official language of Korean Train Set is Korean, not English.  
I'm not a fluent English speaker, so english texts might have different meanings from than Korean.

To translate the Korean Train Set into your native language, please pull the request via this github project.  
If you don't know how to make a Pull Request, uploading them at Issues is fine, too.
You shall translate:
- [./lang/english.lng](../lang/english.lng)  

You don't need to translate these below files (since they are generated automatically):  
- `./docs/download_page/*.html` and `./docs/download_page/*.md`  

And if you want to translate [the download page of my own site](https://telk.kr/ottd/newgrf/ko_train_set?lang=en), translate below (note: `LANGUAGE_NAME` should the file name of `./lang/(LANGUAGE_NAME).lng`):  
```
LANGUAGE_NAME             :english
GRF_NAME                  :Korean Train Set
MORE                      :more
MAIN_IMAGE_ALT            :Image of Korean Train Set
INTRODUCTION              :Introduction
GRF_DESC                  :<b>Korean Train Set</b> is an OpenTTD NewGRF that adds South Korea's trains, such as KTX(Korea Train eXpress)'s, ITX(Intercity Train eXpress)'s, Saemaeul, Mugunghwa, Tongil, Nuriro, CDC, subways of Seoul Metropolitan area, some diesel/electric locomotives of Korail, some tourist train such as O-train, V-train, DMZ-train, S-train and so on. It has parameters so that you can change the train's speeds for each class, purchase costs, running costs, capacities or loading speeds. And it also contains 'TK simple waypoint' function so that you can easily make a graphic of waypoint simple by parameter settings. It is the essential NewGRF to make South korean contents.
DOWNLOAD                  :Download
DOWNLOAD_DESC             :Available on the online-contents in the game!<br />Search <strong>Korean Train Set</strong> in the <b>Check Online Content</b> menu ingame.
GITHUB_REPO               :Github repository
GITHUB_REPO_DESC          :<b>Korean Train Set</b> is an open-source project. All sprites and codes are opened at Github repository.<br />Please visit <a href="https://github.com/KoreanGRF/KoreanTrainSet" target="_blank" class="external">Korean Train Set Github repo</a> if you have any issues, suggestions, featrue requests, translations or contributes.
VEHICLE_LIST_TITLE        :Vehicles added & Vehicle specifications
VEHICLE_LIST_IMAGE        :Image
VEHICLE_LIST_NAME         :Name
VEHICLE_LIST_SPEED        :Speed
VEHICLE_LIST_MAX_SPEED    :Max speed
VEHICLE_LIST_CAPACITY     :Capacity
VEHICLE_LIST_POWER        :Power
VEHICLE_LIST_WEIGHT       :Weight
VEHICLE_LIST_INTRODUCTION :Introduced
```

## Links
- [TELKLAND](http://telk.kr)
- Official Download Page ([Korean](https://telk.kr/ottd/newgrf/ko_train_set/?lang=kr) / [English](https://telk.kr/ottd/newgrf/ko_train_set/?lang=en) / [Japanese](https://telk.kr/ottd/newgrf/ko_train_set/?lang=jp) / [Spanish](https://telk.kr/ottd/newgrf/ko_train_set/?lang=es))

## Contributors
All names of contributors can be found at [Contributors](https://github.com/KoreanGRF/KoreanTrainSet/graphs/contributors) in this Repository and [contributors.md](../docs/contributors.md).

## License
This NewGRF follows **[the Creative Commons License v3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/)** (CC-BY-NC-SA v3.0)  
By contributing this project, it means that you agree to this license.
# Korean Train Set
[English](./README.md) | [한국어](./README.ko.md)

**한국 열차 세트**는 대한민국의 열차 차량과 철도 시설을 추가해주는 OpenTTD NewGRF입니다.  
게임 내 온라인 콘텐츠에서 다운로드하거나, [Github release 페이지](https://github.com/KoreanGRF/KoreanTrainSet/releases)에서 다운로드할 수 있습니다.

## 차량 목록 및 스펙
[이 페이지](../docs/download_page/korean.md)에서 전체 차량 목록과 각각의 스펙(속력, 무게, 출력 등)을 확인하실 수 있습니다.

## 개발
### 빌드하는 방법
이 NewGRF를 빌드하려면 [NML](https://github.com/OpenTTD/nml)(>= 0.8.1), `make` 그리고 **Python 3**이 필요합니다.  
터미널 쉘에서 `make`를 실행하세요. Windows 환경이라면, 그 전에 명령 프롬포트를 열고 `bash`를 입력하세요.  
`make clean`을 입력하면 모든 생성된 파일이 초기화됩니다.

### 번역
한국 열차 세트의 공식 언어는 한국어입니다.  
저는 유창한 영어 실력자가 아니기 때문에, 영어 텍스트가 한국어와 다른 의미를 갖고 있을 수도 있습니다.

한국 열차 세트를 다른 언어로 번역하시려면, 이 Github 프로젝트에 Pull Request를 열어주세요.  
Pull Request를 열 줄 모르신다면, Issues에 올리셔도 괜찮습니다.
이 파일을 번역하시면 됩니다:
- [./lang/english.lng](../lang/english.lng)  

아래의 파일은 (자동으로 생성되는 파일이므로) 번역할 필요가 없습니다:  
- `./docs/download_page/*.html` and `./docs/download_page/*.md`  

또, [제 사이트의 다운로드 페이지](https://telk.kr/ottd/newgrf/ko_train_set?lang=en)도 번역하길 원하신다면, 아래 내용을 번역해주세요 (참고: `LANGUAGE_NAME`은, `english` 처럼 `./lang/(LANGUAGE_NAME).lng`의 파일 이름이어야 합니다):   
```
LANGUAGE_NAME             :korean
GRF_NAME                  :한국 열차 세트
MORE                      :더 보기
MAIN_IMAGE_ALT            :한국 열차 세트 모음 이미지
INTRODUCTION              :소개
GRF_DESC                  :<b>한국 열차 세트</b>는 OpenTTD에 KTX, ITX-청춘, 새마을호, 무궁화호, 누리로, CDC(통근열차), 수도권 지하철, Korail의 디젤/전기 기관차, 일부 관광열차(O-train, V-train, DMZ-train, S-train) 등의 각종 한국 열차와 경전철 선로 등을 추가해주는 NewGRF입니다. OpenTTD의 NewGRF 설정창의 매개 변수 설정을 통해 각 등급별 열차의 속력, 구입 가격, 유지비, 수송량, 수송 속도 등을 조절할 수 있으며 경유지 간소화 기능을 포함하고 있어서 지저분한 경유지의 그래픽을 간소화시킬 수도 있습니다. 한국 관련 컨텐츠를 제작하실 때 반드시 필요한 NewGRF입니다.
DOWNLOAD                  :다운로드
DOWNLOAD_DESC             :온라인 콘텐츠에서 다운로드할 수 있습니다!<br />게임 안의 <b>온라인 콘텐츠 다운로드</b> 메뉴에서 <strong>Korean Train Set</strong>으로 검색하세요.
GITHUB_REPO               :Github 저장소
GITHUB_REPO_DESC          :<b>한국 열차 세트</b>는 오픈 소스입니다. Github 저장소에 모든 소스가 공개되어 있습니다.<br />버그 신고, 건의 사항/기능 추가 요청, 번역, 그래픽/코드 기여 등은 <a href="https://github.com/KoreanGRF/KoreanTrainSet" target="_blank" class="external">한국 열차 세트 Github 저장소</a>에서 해주시기 바랍니다.
VEHICLE_LIST_TITLE        :추가되는 차량 & 차량 스펙
VEHICLE_LIST_IMAGE        :이미지
VEHICLE_LIST_NAME         :이름
VEHICLE_LIST_SPEED        :영업속력
VEHICLE_LIST_MAX_SPEED    :최고속력
VEHICLE_LIST_CAPACITY     :수송량
VEHICLE_LIST_POWER        :출력
VEHICLE_LIST_WEIGHT       :무게
VEHICLE_LIST_INTRODUCTION :도입
```

## 링크
- [TELKLAND](http://telk.kr)
- 공식 다운로드 페이지 ([Korean](https://telk.kr/ottd/newgrf/ko_train_set/?lang=kr) / [English](https://telk.kr/ottd/newgrf/ko_train_set/?lang=en) / [Japanese](https://telk.kr/ottd/newgrf/ko_train_set/?lang=jp) / [Spanish](https://telk.kr/ottd/newgrf/ko_train_set/?lang=es))

## 기여하신 분들
모든 기여하신 분들의 이름은 이 저장소의 [Contributors](https://github.com/KoreanGRF/KoreanTrainSet/graphs/contributors)와 [contributors.md](../docs/contributors.ko.md)에서 볼 수 있습니다.

## 라이선스
이 NewGRF는 **[크리에이티브 커먼스 라이선스 v3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/)** (CC-BY-NC-SA v3.0)을 따릅니다.  
이 프로젝트에 기여함은 이 라이선스에 동의함을 의미합니다.

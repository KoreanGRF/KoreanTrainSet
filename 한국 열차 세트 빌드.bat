@echo off
title 한국 열차 세트 빌드
rem echo 한국 열차 세트를 빌드합니다. 계속하시겠습니까?
rem pause

:first_level
echo.
echo #1. NML 컴파일
echo 컴파일을 실행합니다.....
echo ─────────────────────────────
"..\NML\0.2.2\nmlc.exe" --custom-tags="./custom_tags.txt" --lang-dir="./lang/" --grf="./ko_train_set.grf" --nfo="./ko_train_set.nfo" "./ko_train_set.nml"
echo.
if ERRORLEVEL 1 (
	echo [결과] 오류!! 컴파일에 실패하였습니다!
	goto stop_process
) else (
	echo [결과] 컴파일에 성공하였습니다.
)
echo ─────────────────────────────
echo.
echo.
echo.

echo #2. 파일 압축
echo 한국 열차 세트 관련 파일을 TAR 파일로 압축합니다.
echo 오류 메시지가 뜨지 않았다면 압축에 성공한 것입니다.
echo ─────────────────────────────
echo (1) 한국 열차 세트 버전 불러오기
for /f "eol=; tokens=2 delims=:" %%i in (./custom_tags.txt) do (
	set KTS_VERSION=%%i
	goto out
)
:out
echo [결과] 찾아낸 버전: %KTS_VERSION%
echo ─────────────────────────────
echo.
echo.
echo.
echo (2) 압축
echo ─────────────────────────────
"C:\Program Files\Bandizip\bz.exe" /archive "Korean_Train_Set-%KTS_VERSION%.tar" "ko_train_set.grf" "changelog.txt" "readme.txt" "readme_en.txt"
:: "C:\Program Files (x86)\ESTsoft\ALZip\alzipcon.exe" -a -nq -m0 "ko_train_set.grf";"changelog.txt";"readme.txt";"readme_en.txt" "Korean_Train_Set-%KTS_VERSION%.tar"
echo ─────────────────────────────
echo.
echo.
echo.

echo #3. NML 원본 백업
echo ─────────────────────────────
xcopy /F /Y "./ko_train_set.nml" "./NML_backup/ko_train_set_%KTS_VERSION%.*"
echo [결과] ko_train_%KTS_VERSION%.nml 파일로 백업 완료
echo ─────────────────────────────
echo.
echo.
echo.


echo 한국 열차 세트 %KTS_VERSION% 빌드가 완료되었습니다.

:stop_process
set /P WILL_YOU_RETRY="다시 처음부터 시작하시겠습니까? [Y/N] ..... "
if %WILL_YOU_RETRY% == y (
	cls
	goto first_level
)

:eof
echo.
pause
exit
@echo off
title �ѱ� ���� ��Ʈ ����
rem echo �ѱ� ���� ��Ʈ�� �����մϴ�. ����Ͻðڽ��ϱ�?
rem pause

:first_level
echo.
echo #1. NML ������
echo �������� �����մϴ�.....
echo ����������������������������������������������������������
"..\NML\0.2.2\nmlc.exe" --custom-tags="./custom_tags.txt" --lang-dir="./lang/" --grf="./ko_train_set.grf" --nfo="./ko_train_set.nfo" "./ko_train_set.nml"
echo.
if ERRORLEVEL 1 (
	echo [���] ����!! �����Ͽ� �����Ͽ����ϴ�!
	goto stop_process
) else (
	echo [���] �����Ͽ� �����Ͽ����ϴ�.
)
echo ����������������������������������������������������������
echo.
echo.
echo.

echo #2. ���� ����
echo �ѱ� ���� ��Ʈ ���� ������ TAR ���Ϸ� �����մϴ�.
echo ���� �޽����� ���� �ʾҴٸ� ���࿡ ������ ���Դϴ�.
echo ����������������������������������������������������������
echo (1) �ѱ� ���� ��Ʈ ���� �ҷ�����
for /f "eol=; tokens=2 delims=:" %%i in (./custom_tags.txt) do (
	set KTS_VERSION=%%i
	goto out
)
:out
echo [���] ã�Ƴ� ����: %KTS_VERSION%
echo ����������������������������������������������������������
echo.
echo.
echo.
echo (2) ����
echo ����������������������������������������������������������
"C:\Program Files\Bandizip\bz.exe" /archive "Korean_Train_Set-%KTS_VERSION%.tar" "ko_train_set.grf" "changelog.txt" "readme.txt" "readme_en.txt"
:: "C:\Program Files (x86)\ESTsoft\ALZip\alzipcon.exe" -a -nq -m0 "ko_train_set.grf";"changelog.txt";"readme.txt";"readme_en.txt" "Korean_Train_Set-%KTS_VERSION%.tar"
echo ����������������������������������������������������������
echo.
echo.
echo.

echo #3. NML ���� ���
echo ����������������������������������������������������������
xcopy /F /Y "./ko_train_set.nml" "./NML_backup/ko_train_set_%KTS_VERSION%.*"
echo [���] ko_train_%KTS_VERSION%.nml ���Ϸ� ��� �Ϸ�
echo ����������������������������������������������������������
echo.
echo.
echo.


echo �ѱ� ���� ��Ʈ %KTS_VERSION% ���尡 �Ϸ�Ǿ����ϴ�.

:stop_process
set /P WILL_YOU_RETRY="�ٽ� ó������ �����Ͻðڽ��ϱ�? [Y/N] ..... "
if %WILL_YOU_RETRY% == y (
	cls
	goto first_level
)

:eof
echo.
pause
exit
@echo off
title SSH_PUTTY_WINSCP - BY: Matheus Johann Araujo
color 1f
mode 100,25
cls
echo.
echo  ) SSH_PUTTY_WINSCP (
echo.  
set host=192.168.0.1
set /p host=: QUAL O IP DO SERVIDOR SSH?=^>
set host="%host%"
cls
echo.
set user=nao
set /p user=: QUAL O NOME DE USUARIO?=^>
set user="%user%"
cls
echo.
set pass=nao
set /p pass=: QUAL A SENHA DO USUARIO?=^>
set pass="%pass%"
for %%I in (.) do set CurrDirName=%%~nxI
set nameDir=%CurrDirName%
cls
set /p nameDir=: QUAL O NOME DO PROJETO?=^>
set dirDestino="/home/%user%/_%nameDir%"
set pathDir=%cd%
set port=22
:update
taskkill /f /im putty.exe
cls
plink %user%@%host% -pw %pass% "rm -rf %dirDestino%; mkdir %dirDestino%; chmod +x %dirDestino%; rm -f %nameDir%.sh; echo 'cd %dirDestino%/' > %nameDir%.sh; echo 'python main.py' >> %nameDir%.sh; chmod +x %nameDir%.sh"
winscp.com /command "open sftp://%user%:%pass%@%host%:%port%" "synchronize remote %pathDir% %dirDestino%" "exit"
start putty %user%@%host% -pw %pass%
set /p num=: DIGITE 1 PARA REPETIR A OPERACAO OU OUTRA TECLA PARA SAIR=^>
if %num% EQU 1 (
	goto update
) else (
	exit
)
timeout /t 60
exit

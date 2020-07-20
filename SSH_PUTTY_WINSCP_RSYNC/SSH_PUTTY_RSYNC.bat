@echo off
title SSH_PUTTY_RSYNC - BY: Matheus Johann Araujo
color 1f
mode 100,25
cls
echo.
echo  ) SSH_PUTTY_RSYNC (
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
:update
taskkill /f /im putty.exe
cls
REM apt-get install sshpass
REM wsl rsync -uahv --progress --delete -ratlz --rsh="/usr/bin/sshpass -p %pass% ssh -o StrictHostKeyChecking=no -l %user%" ./ %user%@%host%:%dirDestino%
wsl rsync -uahv --progress --delete ./ %user%@%host%:%dirDestino%
plink %user%@%host% -pw %pass% "chmod +x %dirDestino%; rm -f %nameDir%.sh; echo 'cd %dirDestino%/' > %nameDir%.sh; echo 'python main.py' >> %nameDir%.sh; chmod +x %nameDir%.sh"
start putty %user%@%host% -pw %pass%
set /p num=: DIGITE 1 PARA REPETIR A OPERACAO OU OUTRA TECLA PARA SAIR=^>
if %num% EQU 1 (
	goto update
) else (
	exit
)
timeout /t 60
exit
rem https://www.youtube.com/watch?v=djtMHTA_aBA
rem # Comandos
rem rsync -ahv ./ ubuntu@192.168.0.105:/home/ubuntu/sincronizacao
rem rsync -uahv ./ ubuntu@192.168.0.105:/home/ubuntu/sincronizacao
rem rsync -uahv --delete ./ ubuntu@192.168.0.105:/home/ubuntu/sincronizacao
rem rsync -uahv --progress --delete ./ ubuntu@192.168.0.105:/home/ubuntu/sincronizacao
rem apt-get install openssh-server
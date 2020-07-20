@echo off
title SSH_PUTTY - BY: Matheus Johann Araujo
color 1f
mode 100,25
cls
echo.
echo  ) SSH_PUTTY (
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
:update
taskkill /f /im putty.exe
cls
start putty %user%@%host% -pw %pass%
set /p num=: DIGITE 1 PARA REPETIR A OPERACAO OU OUTRA TECLA PARA SAIR=^>
if %num% EQU 1 (
	goto update
) else (
	exit
)
timeout /t 60
exit
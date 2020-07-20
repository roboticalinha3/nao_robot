#!/bin/sh
clear
echo NAOLIBS - Instalando...
mount -w -o remount /
pkill -f /usr/lib/python2.7/NAOLIBS/Main.py
rm -rf /usr/lib/python2.7/NAOLIBS/
cd ..
mv NAOLIBS/ /usr/lib/python2.7
sleep 1
clear
echo NAOLIBS - Instalado com sucesso.
mv /usr/lib/python2.7/NAOLIBS/main-naolibs.sh /etc/init.d/
cd /etc/init.d/
chmod +x main-naolibs.sh
# update-rc.d main-naolibs defaults
# update-rc.d main-naolibs remove
# update-rc.d main-naolibs defaults
# echo NAOLIBS - Autostart configurado com sucesso.
#---------------------------------------------------------------
# incluir o comando abaixo no arquivo /etc/init.d/naoqi
# nohup sh /etc/init.d/main-naolibs.sh > /dev/null 2>&1
#---------------------------------------------------------------
python /usr/lib/python2.7/NAOLIBS/Main.py
# nao restart
#---------------------------------------------------------------
# GitHub: https://github.com/matheusjohannaraujo/nao_robot
# Country: Brasil
# State: Pernambuco
# Developer: Matheus Johann Araujo
# Date: 2020-07-29
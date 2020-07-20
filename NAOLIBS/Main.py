# -*- encoding: utf-8 -*-
#coding: utf-8

"""
  GitHub: https://github.com/matheusjohannaraujo/nao_robot
  Country: Brasil
  State: Pernambuco
  Developer: Matheus Johann Araujo
  Date: 2021-12-16
"""

try:
    from NAOLIBS import *
except Exception as e:
    print("Erro ao importar bibliotecas", e)
    exit()

print("NAOLIBS - Executando Main.py")
Sistema.comando("mount -w -o remount /")
time.sleep(3)
ModoAutonomo.desligar()
Led.corpoAzul(255)
Motor.posturaCrouch()
Motor.rigidezCorpo(10)
Led.corpoVerde(255)
Sensor.cabeca(lambda: Sistema.redeWifi())
Led.corpoVermelho(255)
Audio.falar("O Main do NAOLIBS foi iniciado com sucesso")
Led.corpo(hex = "#FFFFFF")

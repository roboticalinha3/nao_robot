# -*- encoding: utf-8 -*-
#coding: utf-8

"""
  GitHub: https://github.com/matheusjohannaraujo/nao_robot
  Country: Brasil
  State: Pernambuco
  Developer: Matheus Johann Araujo
  Date: 2020-07-29
"""

try:
    from NAOLIBS import *
except Exception as e:
    print("Erro ao importar bibliotecas no arquivo main.py", e)

Led.corpoAzul(255)
Motor.posturaCrouch()

Sensor.cabeca(lambda: Led.corpoRGB(False))
Sensor.cabecaFrente(lambda: Motor.posturaStandInit())
Sensor.cabecaMeio(lambda: Motor.posturaStand())
Sensor.cabecaTras(lambda: Motor.posturaCrouch())

Led.corpo(hex = "#FFFFFF")
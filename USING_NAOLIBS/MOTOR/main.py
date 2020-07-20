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

Led.corpoVermelho(255)
Motor.posturaCrouch()

Led.corpoVerde(255)
Audio.volume(65)
Audio.falar("Olá, meu nome é NAO")
Motor.posturaStand()

time.sleep(1)
Motor.bracos("antebraco", 120)
time.sleep(1)
Motor.bracos("antebraco", -120)
time.sleep(1)
Motor.bracos("mao", 105)
time.sleep(1)
Motor.bracos("mao", -105)
time.sleep(1)
Motor.bracos("cotovelo", 0)
time.sleep(1)
Motor.bracos("cotovelo", -90)
time.sleep(1)
Motor.bracos("ombro", 80)
time.sleep(1)
Motor.bracos("ombro", -18)
time.sleep(1)
Motor.bracos("ombro", 0)
Motor.bracos("cotovelo", 0)
Motor.bracos("mao", 0)
Motor.bracos("antebraco", 0)
Motor.posturaStandInit()
Led.corpoAzul(255)
arrListar = Comportamento.listar()
strListar = ""
for i in range(0, len(arrListar)):
    strListar += arrListar[i] + "; "
Audio.falar("Meus comportamentos são. " + strListar, True)

time.sleep(35)
Led.corpo(255, 255, 255)
Motor.mao(True)
Motor.mao(False)
Motor.andarFrente(0.125)
Motor.andarTras(0.125)
Motor.andarDireita(0.125)
Motor.andarEsquerda(0.125)
Motor.andarGirandoHorario(45)
Motor.andarGirandoAntiHorario(45)

Motor.posturaStandZero()
time.sleep(10)
Motor.posturaCrouch()
Led.corpo()

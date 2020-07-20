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

Motor.cabecaCentro()
time.sleep(1.5)
Motor.cabecaCima(38.5)
time.sleep(1.5)
Motor.cabecaBaixo(29.5)
time.sleep(1.5)
Motor.cabecaBaixo()
time.sleep(1.5)
Motor.cabecaDireita(119.5)
time.sleep(1.5)
Motor.cabecaEsquerda(119.5)
time.sleep(1.5)
Motor.cabecaEsquerda()

Camera.conn()
Camera.iniciarCaptura()

def procuraBola(anguloCabecaBaixo, anguloBusca, numCamera, callback = lambda params: params):
    Camera.conn()
    if numCamera == 1:
        Camera.cima()
    else:
        Camera.baixo()
    Motor.posturaStand()
    Motor.cabecaEsquerda(0)
    Motor.cabecaBaixo(anguloCabecaBaixo)
    anguloBusca = int((anguloBusca ** 2) ** 0.5)
    nameUID = str(uuid.uuid4())
    for i in range(-anguloBusca, anguloBusca + 1, 20):
        Motor.cabecaEsquerda(i)
        callback([nameUID, i, anguloCabecaBaixo, numCamera])
        j = int((i ** 2) ** 0.5)
        if j <= 10:
            time.sleep(0.25)
            Motor.cabecaBaixo(anguloCabecaBaixo)
            time.sleep(0.25)
            print("menor")
    print("Fim")
    return True

def processaIMG(params):
    print(params)
    print(Camera.imagemSaida(str(params) + "_"))

procuraBola(35, 40, 2, processaIMG)
procuraBola(35, 40, 1, processaIMG)

procuraBola(25, 40, 2, processaIMG)
procuraBola(25, 40, 1, processaIMG)

procuraBola(15, 40, 2, processaIMG)
procuraBola(15, 40, 1, processaIMG)

Motor.cabecaCima(0)
Motor.cabecaDireita(0)

Motor.posturaCrouch()

"""
  GitHub: https://github.com/matheusjohannaraujo/nao_robot
  Country: Brasil
  State: Pernambuco
  Developer: Matheus Johann Araujo
  Date: 2020-11-13
"""

try:
    import time
    from AsyncThread import AsyncThread    
    from Memoria import Memoria
except Exception as e:
    print("Erro ao importar bibliotecas no arquivo Sensor.py", e)

class Sensor:

    listaEventos = []
    bloqueio = False

    @staticmethod
    def adicionar(name, call):
        try:
            if not call:
                return Memoria.ler(name)
            Sensor.listaEventos.append([name, call])
            if len(Sensor.listaEventos) == 1:
                return AsyncThread.call(Sensor.monitor)
            return True
        except Exception as e:
            print("Exception -> Sensor.adicionar():", e)
        return False

    @staticmethod
    def eventos():
        return Sensor.listaEventos

    @staticmethod
    def monitor():
        try:
            while True:
                for i in Sensor.eventos():
                    time.sleep(0.125)
                    if Memoria.ler(i[0]) == 1 and not Sensor.bloqueio:
                        AsyncThread.call(i[1])
                        time.sleep(1)
        except Exception as e:
            print("Exception -> Sensor.monitor():", e)
        return AsyncThread.call(Sensor.monitor)

    @staticmethod
    def cabeca(call = False, async = True):
        if async:
            return AsyncThread.call(lambda: Sensor.cabeca(call, False))
        while True:
            if Sensor.cabecaFrente() and Sensor.cabecaMeio() and Sensor.cabecaTras():                
                Sensor.bloqueio = True
                call()
                Sensor.bloqueio = False
                time.sleep(2)

    @staticmethod
    def cabecaFrente(call = False):
        return Sensor.adicionar("FrontTactilTouched", call)

    @staticmethod
    def cabecaMeio(call = False):
        return Sensor.adicionar("MiddleTactilTouched", call)

    @staticmethod
    def cabecaTras(call = False):
        return Sensor.adicionar("RearTactilTouched", call)

    @staticmethod
    def maoDireita(call = False):
        return Sensor.adicionar("HandRightRightTouched", call)
        #return Sensor.adicionar("HandRightBackTouched", call)

    @staticmethod
    def maoEsquerda(call = False):
        return Sensor.adicionar("HandLeftLeftTouched", call)
        #return Sensor.adicionar("HandLeftBackTouched", call)
    
    @staticmethod
    def peDireito(call = False):
        return Sensor.adicionar("RightBumperPressed", call)

    @staticmethod
    def peEsquerdo(call = False):
        return Sensor.adicionar("LeftBumperPressed", call)

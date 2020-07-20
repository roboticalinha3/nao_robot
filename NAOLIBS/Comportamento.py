"""
  GitHub: https://github.com/matheusjohannaraujo/nao_robot
  Country: Brasil
  State: Pernambuco
  Developer: Matheus Johann Araujo
  Date: 2020-07-29
"""

try:
    import Config
    from naoqi import ALProxy
    from AsyncThread import AsyncThread
    import os
    import sys
    import time
    sys.path.append(os.path.join("/home/nao/.local/share/PackageManager/apps/", '../lib'))
    import re
    from Motor import Motor
    from Led import Led
except Exception as e:
    print("Erro ao importar bibliotecas no arquivo Comportamento.py", e)

class Comportamento:

    @staticmethod
    def conn():
        try:
            return ALProxy('ALBehaviorManager', Config.ip_addr, Config.port_num)
        except Exception as e:
            print("Exception -> Comportamento.conn():", e)
        return False

    @staticmethod
    def listar():
        try:
            bm = Comportamento.conn()
            behaviors = bm.getUserBehaviorNames()
            for i in range(len(behaviors)):
                for j in range(2):
                    behaviors[i] = "/" + behaviors[i]
                    behaviors[i] = re.sub('/[^>]+?/', '', behaviors[i])
                behaviors[i] = re.sub('/', '', behaviors[i])
            return behaviors
        except Exception as e:
            print("Exception -> Comportamento.listar():", e)
        return []

    @staticmethod
    def iniciar(nome, runBehavior = True, async = True):
        try:
            if async:
                return AsyncThread.call(lambda: Comportamento.iniciar(nome, runBehavior, False))
            if nome in Comportamento.listar():
                bm = Comportamento.conn()
                if runBehavior:
                    bm.runBehavior(nome)
                    return True
                else:
                    bm.startBehavior(nome)
                    return True
        except Exception as e:
            print("Exception -> Comportamento.iniciar():", e)
        return False

    @staticmethod
    def parar(nome, posturaCrouch = True, async = False):
        try:
            if async:
                return AsyncThread.call(lambda: Comportamento.parar(nome, posturaCrouch, False))
            if nome in Comportamento.listar():
                Led.corpoVermelho(255)
                bm = Comportamento.conn()
                bm.stopBehavior(nome)
                if posturaCrouch:
                    Motor.posturaCrouch()
                else:
                    time.sleep(1)
                Led.corpoVerde(255)
                time.sleep(1)
                Led.corpo(255, 255, 255)
                return True
        except Exception as e:
            print("Exception -> Comportamento.parar():", e)
        return False

    @staticmethod
    def pararTodos(posturaCrouch = True):
        try:
            Led.corpoRGB()
            bm = Comportamento.conn()
            bm.stopAllBehaviors()
            if posturaCrouch:
                Motor.posturaCrouch()
            return True
        except Exception as e:
            print("Exception -> Comportamento.pararTodos():", e)
        return False

"""
  GitHub: https://github.com/matheusjohannaraujo/nao_robot
  Country: Brasil
  State: Pernambuco
  Developer: Matheus Johann Araujo
  Date: 2021-01-04
"""

try:
    import Config
    from naoqi import ALProxy
    import os
    import time
    from Audio import Audio
    from AsyncThread import AsyncThread
except Exception as e:
    print("Erro ao importar bibliotecas no arquivo Sistema.py", e)

class Sistema:

    @staticmethod
    def conn():
        try:
            return ALProxy("ALSystem", Config.ip_addr, Config.port_num)
        except Exception as e:
            print("Exception -> Sistema.conn():", e)
        return False        

    @staticmethod
    def reiniciar():
        try:
            return Sistema.conn().reboot()
        except Exception as e:
            print("Exception -> Sistema.reiniciar():", e)
        return False

    @staticmethod
    def desligar():
        try:
            return Sistema.conn().shutdown()
        except Exception as e:
            print("Exception -> Sistema.desligar():", e)
        return False

    @staticmethod
    def robotName(name = ""):
        try:
            if name != "":
                return Sistema.conn().setRobotName(name)
            return str(Sistema.conn().robotName())
        except Exception as e:
            print("Exception -> Sistema.robotName():", e)
        return False

    @staticmethod
    def comando(cmd):
        try:
            os.system(cmd)
            return True
        except Exception as e:
            print("Exception -> Sistema.comando():", e)
        return False

    @staticmethod
    def reiniciarNAO():
        try:
            return Sistema.comando("/etc/init.d/naoqi restart")
        except Exception as e:
            print("Exception -> Sistema.reiniciarNAO():", e)
        return False

    @staticmethod
    def rede():
        try:
            return ALProxy("ALConnectionManager", Config.ip_addr, Config.port_num)
        except Exception as e:
            print("Exception -> Sistema.rede():", e)
        return False        

    @staticmethod
    def redeWifi(ssid = False, password = "0123456789"):
        try:
            alConnectionManager = Sistema.rede()
            apWifi = alConnectionManager.getTetheringEnable("wifi")
            if not ssid:
                ssid = Sistema.robotName()
            else:
                ssid = str(ssid)
            sentence = "Erro no uai fai"
            if apWifi == 0:                
                alConnectionManager.enableTethering("wifi", ssid, password)
                sentence = "Uai fai direto ativado. Sua rede se chama " + ssid
            elif apWifi == 1:
                alConnectionManager.disableTethering("wifi")
                sentence = "Uai fai direto desativado. A rede de nome " + ssid + " deixou de existir"
            Audio.falar(sentence, async = True)
            return True
        except Exception as e:
            print("Exception -> Sistema.redeWifi():", e)
        return False

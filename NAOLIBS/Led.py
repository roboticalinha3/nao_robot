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
    import time
    from AsyncThread import AsyncThread
except Exception as e:
    print("Erro ao importar bibliotecas no arquivo Led.py", e)

class Led:

    @staticmethod
    def conn():
        try:
            return ALProxy("ALLeds", Config.ip_addr, Config.port_num)
        except Exception as e:
            print("Exception -> Led.conn():", e)
        return False

    @staticmethod
    def hexParaRGB(value):
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

    @staticmethod
    def mudar(r = 0, g = 0, b = 0, hex = "", group = "AllLeds", async = True):
        try:
            if async:
                return AsyncThread.call(lambda : Led.mudar(r, g, b, hex, group, False))
            if hex:
                rgb = Led.hexParaRGB(hex)
                r = rgb[0]
                g = rgb[1]
                b = rgb[2]
            Led.conn().fadeRGB(group, 256 * 256 * r + 256 * g + b, 0.100000, _async=True)
            return True
        except Exception as e:
            print("Exception -> Led.mudar():", e)
        return False

    @staticmethod
    def alternar(on = False, group = "AllLeds", async = True):
        try:
            if async:
                return AsyncThread.call(lambda: Led.alternar(on, group, False))
            leds = Led.conn()
            if on:            
                leds.on(group)
                return True
            else:
                leds.off(group)
                return True   
        except Exception as e:
            print("Exception -> Led.alternar():", e)
        return False

    @staticmethod
    def botoesCabeca(b = 0):
        return Led.mudar(b = b, group = "BrainLeds")

    @staticmethod
    def botoesCabecaFrente(b = 0):
        return Led.mudar(b = b, group = "BrainLedsFront")
    
    @staticmethod
    def botoesCabecaMeio(b = 0):
        return Led.mudar(b = b, group = "BrainLedsMiddle")

    @staticmethod
    def botoesCabecaTras(b = 0):
        return Led.mudar(b = b, group = "BrainLedsBack")

    @staticmethod
    def orelhas(b = 0):
        return Led.mudar(b = b, group = "EarLeds")

    @staticmethod
    def orelhaEsquerda(b = 0):
        return Led.mudar(b = b, group = "LeftEarLeds")

    @staticmethod
    def orelhaDireita(b = 0):
        return Led.mudar(b = b, group = "RightEarLeds")

    @staticmethod
    def olhos(r = 0, g = 0, b = 0, hex = ""):        
        return Led.mudar(r, g, b, hex, "FaceLeds")

    @staticmethod
    def olhoEsquerdo(r = 0, g = 0, b = 0, hex = ""):
        return Led.mudar(r, g, b, hex, "LeftFaceLeds")

    @staticmethod
    def olhoDireito(r = 0, g = 0, b = 0, hex = ""):
        return Led.mudar(r, g, b, hex, "RightFaceLeds")

    @staticmethod
    def botaoPeito(r = 0, g = 0, b = 0, hex = ""):
        return Led.mudar(r, g, b, hex, "ChestLeds")

    @staticmethod
    def pes(r = 0, g = 0, b = 0, hex = ""):
        return Led.mudar(r, g, b, hex, "FeetLeds")

    @staticmethod
    def peEsquerdo(r = 0, g = 0, b = 0, hex = ""):
        return Led.mudar(r, g, b, hex, "LeftFootLeds")

    @staticmethod
    def peDireito(r = 0, g = 0, b = 0, hex = ""):
        return Led.mudar(r, g, b, hex, "RightFootLeds")

    @staticmethod
    def corpo(r = 0, g = 0, b = 0, hex = ""):
        return Led.mudar(r, g, b, hex)

    @staticmethod
    def corpoVermelho(r = 0):
        return Led.mudar(r = r)
    
    @staticmethod
    def corpoVerde(g = 0):
        return Led.mudar(g = g)

    @staticmethod
    def corpoAzul(b = 0):
        return Led.mudar(b = b)

    @staticmethod
    def corpoRGB(async = True):
        if async:
            return AsyncThread.call(lambda : Led.corpoRGB(False))
    
        for i in range(0, 255):
            Led.corpoVermelho(i)
            time.sleep(0.005)

        for i in range(0, 255):
            Led.corpoVerde(i)
            time.sleep(0.005)

        for i in range(0, 255):
            Led.corpoAzul(i)
            time.sleep(0.005)

        for i in range(0, 255):
            Led.corpo(i, i, i)
            time.sleep(0.005)
    
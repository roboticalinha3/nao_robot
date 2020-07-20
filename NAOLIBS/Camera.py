"""
  GitHub: https://github.com/matheusjohannaraujo/nao_robot
  Country: Brasil
  State: Pernambuco
  Developer: Matheus Johann Araujo
  Date: 2021-02-06
"""

try:
    from naoqi import ALProxy
    import Config
    import numpy as np
    import cv2
except Exception as e:
    print("Erro ao importar bibliotecas no arquivo Camera.py", e)

class Camera:

    device = False
    capture = False

    @staticmethod
    def conn():
        try:
            if not Camera.device:
                Camera.device = ALProxy('ALVideoDevice', Config.ip_addr, Config.port_num)
            return Camera.device
        except Exception as e:
            print("Exception -> Camera.conn():", e)
        return False

    @staticmethod
    def cima():
        try:
            Camera.device.setParam(18, 0)
            return True
        except Exception as e:
            print("Exception -> Camera.cima():", e)
        return False

    @staticmethod
    def baixo():
        try:
            Camera.device.setParam(18, 1)
            return True
        except Exception as e:
            print("Exception -> Camera.baixo():", e)
        return False

    AL_kTopCamera = 0
    AL_kQVGA = 1 # 320x240
    width = 320
    height = 240
    AL_kBGRColorSpace = 13
    
    @staticmethod
    def iniciarCaptura():
        try:
            Camera.capture = Camera.device.subscribeCamera("test", Camera.AL_kTopCamera, Camera.AL_kQVGA, Camera.AL_kBGRColorSpace, 10)
            return Camera.capture
        except Exception as e:
            print("Exception -> Camera.iniciarCaptura():", e)
        return False
 
    @staticmethod
    def obterCaptura():
        try:
            return Camera.device.getImageRemote(Camera.capture)
        except Exception as e:
            print("Exception -> Camera.obterCaptura():", e)
        return False

    @staticmethod
    def pararCaptura():
        try:
            Camera.device.unsubscribe("test")
            return True
        except Exception as e:
            print("Exception -> Camera.pararCaptura():", e)
        return False

    @staticmethod
    def pararCapturas():
        try:
            capturas = Camera.device.getSubscribers()
            print(capturas)
            if(len(capturas) >= 5):
                for i in range(5, len(capturas)):
                    Camera.device.unsubscribe(capturas[i])
                    print(capturas[i])
                return True
        except Exception as e:
            print("Exception -> Camera.pararCapturas():", e)
        return False
        
    @staticmethod
    def imagemSalvar(img, nome = "", caminho = "./img/"):
        try:
            nome = str(caminho) + str(nome)
            cv2.imwrite(nome, img)
            return True
        except Exception as e:
            print("Exception -> Camera.imagemSalvar():", e)
        return False

    @staticmethod
    def imagemRGB():
        try:
            width = Camera.width
            height = Camera.height
            image = np.zeros((height, width, 3), np.uint8)
            result = Camera.obterCaptura()
            if result == None:
                print 'Cannot capture.'
                Camera.pararCapturas()
                Camera.iniciarCaptura()
                return Camera.imagemRGB()
            elif result[6] == None:
                print 'No image data string.'
                Camera.pararCapturas()
                Camera.iniciarCaptura()
                return Camera.imagemRGB()
            else:
                values = map(ord, list(result[6]))
                i = 0
                for y in range(0, height):
                    for x in range(0, width):
                        image.itemset((y, x, 2), values[i + 0])
                        image.itemset((y, x, 1), values[i + 1])
                        image.itemset((y, x, 0), values[i + 2]) 
                        i += 3
                return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        except Exception as e:
            print("Exception -> Camera.imagemRGB():", e)
        return False

    @staticmethod
    def imagemCinza(img):
        try:
            return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        except Exception as e:
            print("Exception -> Camera.imagemCinza():", e)
        return False

    @staticmethod
    def imagemMASK(img):
        try:
            lower_green = np.array([30,30,30], dtype = np.uint8) #valor original (0,0,0)
            upper_green = np.array([165,255,165], dtype = np.uint8) #valor original (117,255,117
            return cv2.inRange(img, lower_green, upper_green)
        except Exception as e:
            print("Exception -> Camera.imagemMASK():", e)
        return False

    @staticmethod
    def imagemSaida(name = ""):   
        try:     
            rgb = Camera.imagemRGB()
            Camera.imagemSalvar(rgb, name + "_imagemRGB.png")

            gray = Camera.imagemCinza(rgb)
            Camera.imagemSalvar(gray, name + "_imagemGRAY.png")

            mask = Camera.imagemMASK(rgb)
            Camera.imagemSalvar(mask, name + "_imagemMASK.png")

            width = Camera.width
            height = Camera.height
            saida = np.zeros((height, width, 1), np.uint8)
            for y in range(0, height):
                for x in range(0, width):
                    if mask.item(y, x) == 255:
                        saida.itemset((y, x, 0), gray.item(y, x))
                    elif mask.item(y, x) == 0:
                        saida.itemset((y, x, 0), 0)

            Camera.imagemSalvar(saida, name + "_imagemSAIDA.png")
            return True
        except Exception as e:
            print("Exception -> Camera.imagemSaida():", e)
        return False

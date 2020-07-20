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
    from Memoria import Memoria
except Exception as e:
    print("Erro ao importar bibliotecas no arquivo Ouvinte.py", e)

class Ouvinte:

    asr = False

    @staticmethod
    def conn():
        try:
            if not Ouvinte.asr:
                Ouvinte.asr = ALProxy("ALSpeechRecognition", Config.ip_addr, Config.port_num)                
                try:
                    Ouvinte.asr.removeAllContext()
                    Ouvinte.asr.unsubscribe("Test_ASR")
                except:
                    pass
            return Ouvinte.asr
        except Exception as e:
            print("Exception -> Ouvinte.conn():", e)
        return Ouvinte.asr

    @staticmethod
    def idioma(linguagem = "Brazilian"):
        try:
            Ouvinte.conn().setLanguage(linguagem)
            return True
        except Exception as e:
            print("Exception -> Ouvinte.idioma():", e)
        return False

    precisao = 0.30

    @staticmethod
    def vocabulario(palavras = ["ola", "matheus", "teste", "xuxu"], precisao = 30, detectarPalavra = False):
        try:
            Ouvinte.conn().pause(True)
            Ouvinte.conn().setVocabulary(palavras, detectarPalavra)
            Ouvinte.precisao = float(precisao / 100)
            Ouvinte.conn().pause(False)
            return True
        except Exception as e:
            print("Exception -> Ouvinte.vocabulario():", e)
        return False
        

    @staticmethod
    def parametro(sensibilidade = "Sensitivity", hipoteses = 0.2):
        try:
            Ouvinte.conn().setParameter(sensibilidade, hipoteses)
            return True 
        except Exception as e:
            print("Exception -> Ouvinte.parametro():", e)
        return False

    threadIniciar = False

    @staticmethod
    def iniciar(callback, async = True):
        try:
            if async:
                Ouvinte.threadIniciar = AsyncThread.call(lambda: Ouvinte.iniciar(callback, False))
                return Ouvinte.threadIniciar
            time.sleep(3)
            Ouvinte.conn().subscribe("Test_ASR")
        except Exception as e:
            print("Exception -> Ouvinte.iniciar()-subscribe:", e)
        while True:
            try:
                if Ouvinte.escutando:
                    leitura = Memoria.ler("WordRecognized")
                    if Ouvinte.precisao <= leitura[1]:
                        Ouvinte.conn().unsubscribe("Test_ASR")
                        callback(leitura)
                        Ouvinte.conn().subscribe("Test_ASR")
                    time.sleep(0.25)
            except Exception as e:
                print("Exception -> Ouvinte.iniciar()-while:", e)    

    escutando = True

    @staticmethod
    def pausar(valor = 0):
        try:
            if valor == 0:
                Ouvinte.conn().pause(Ouvinte.escutando)
                Ouvinte.escutando = not Ouvinte.escutando
            else:
                Ouvinte.conn().pause(valor)
                Ouvinte.escutando = not valor
            print("Ouvinte.pausar()", not Ouvinte.escutando)
            return True
        except Exception as e:
            print("Exception -> Ouvinte.pausar():", e)
        return False

    @staticmethod
    def parar(timer = 0, async = True):
        try:
            if async:
                return AsyncThread.call(lambda: Ouvinte.parar(timer, False))
            time.sleep(timer)
            if Ouvinte.conn() and Ouvinte.threadIniciar:
                if Ouvinte.threadIniciar.running():
                    Ouvinte.threadIniciar.stop()
                Ouvinte.conn().unsubscribe("Test_ASR")
                return True
        except Exception as e:
            print("Exception -> Ouvinte.parar():", e)
        return False
        
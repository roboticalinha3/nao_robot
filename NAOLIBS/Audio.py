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
except Exception as e:
    print("Erro ao importar bibliotecas no arquivo Audio.py", e)

class Audio:

    @staticmethod
    def conn(num):
        try:
            if num == 1:
                return ALProxy('ALAudioDevice', Config.ip_addr, Config.port_num)
            elif num == 2:
                return ALProxy('ALAudioPlayer', Config.ip_addr, Config.port_num)
            elif num == 3:
                tts = ALProxy('ALTextToSpeech', Config.ip_addr, Config.port_num)
                tts.setVolume(1)
                return tts
            elif num == 4:
                return ALProxy('ALAnimatedSpeech', Config.ip_addr, Config.port_num)
        except Exception as e:
            print("Exception -> Audio.conn():", e)
        return False

    @staticmethod
    def volume(vol = -1):
        try:
            vol = int(vol)
            if vol > -1 and vol < 101:
                Audio.conn(1).setOutputVolume(vol)
            return Audio.conn(1).getOutputVolume()
        except Exception as e:
            print("Exception -> Audio.setVolume():", e)
        return False
        
    @staticmethod
    def iniciarMusica(name = "", begin = 0, volume = 100, balance = 0, path = ""):
        try:
            volume = volume / 100
            if name != "" and path == "":
                path = os.getcwd()
                #path = os.path.dirname(os.path.realpath(__file__))
                path = path + "/" + name
                print("Audio.iniciarMusica", path)
            return Audio.conn(2).pCall("playFileFromPosition", path, float(begin), volume, balance)
        except Exception as e:
            print("Exception -> Audio.iniciarMusica():", e)
        return False

    @staticmethod
    def pararMusica(id):
        try:
            Audio.conn(2).stop(id)
            return True
        except Exception as e:
            print("Exception -> Audio.pararMusica():", e)
        return False

    @staticmethod
    def pararMusicas():
        try:
            Audio.conn(2).stopAll()
            return True
        except Exception as e:
            print("Exception -> Audio.pararMusicas():", e)
        return False

    @staticmethod
    def falar(texto, animado = False, speed = 80, voice_shaping = 100, configuracao = { "speakingMovementMode": "contextual", "bodyLanguageMode": "contextual" }, async = False):
        try:
            if async:
                return AsyncThread.call(lambda: Audio.falar(texto, animado, speed, voice_shaping, configuracao, False))
            if animado:
                modo = 4
            else:
                modo = 3
            tts = Audio.conn(modo)
            sentence = "\RSPD=" + str(speed) + "\ "
            sentence += "\VCT=" + str(voice_shaping) + "\ "
            sentence += str(texto)
            sentence +=  "\RST\ "
            if animado:
                id = tts.pCall("say", str(sentence), configuracao)
            else:
                id = tts.pCall("say", str(sentence))
            tts.wait(id, 0)
            return True
        except Exception as e:
            print("Exception -> Audio.falar():", e)
        return False


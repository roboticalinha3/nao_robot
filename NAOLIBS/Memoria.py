"""
  GitHub: https://github.com/matheusjohannaraujo/nao_robot
  Country: Brasil
  State: Pernambuco
  Developer: Matheus Johann Araujo
  Date: 2020-10-27
"""

try:
    import Config
    from naoqi import ALProxy
except Exception as e:
    print("Erro ao importar bibliotecas no arquivo Memoria.py", e)

class Memoria:

    @staticmethod
    def conn():
        try:
            return ALProxy('ALMemory', Config.ip_addr, Config.port_num)
        except Exception as e:
            print("Exception -> Memoria.conn():", e)
        return False

    @staticmethod
    def ler(chave):
        try:
            return Memoria.conn().getData(chave)
        except Exception as e:
            print("Exception -> Memoria.ler():", e)
        return ""

    @staticmethod
    def escrever(chave, valor):
        try:
            Memoria.conn().insertData(chave, valor)
            return True
        except Exception as e:
            print("Exception -> Memoria.escrever():", e)
        return False

    @staticmethod
    def apagar(chave):
        try:
            Memoria.conn().removeData(chave)        
            return True
        except Exception as e:
            print("Exception -> Memoria.apagar():", e)
        return False

    @staticmethod
    def inscreverEvento(chave, nome, evento):
        try:
            Memoria.conn().subscribeToEvent(chave, nome, evento)
            return True
        except Exception as e:
            print("Exception -> Memoria.inscreverEvento():", e)
        return False
    
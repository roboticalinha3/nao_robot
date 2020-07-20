"""
  GitHub: https://github.com/matheusjohannaraujo/nao_robot
  Country: Brasil
  State: Pernambuco
  Developer: Matheus Johann Araujo
  Date: 2021-01-17
"""

try:
    import Config
    from naoqi import ALProxy
    from AsyncThread import AsyncThread
except Exception as e:
    print("Erro ao importar bibliotecas no arquivo ModoAutonomo.py", e)

class ModoAutonomo:

    @staticmethod
    def conn():
        try:
            ma = ALProxy('ALAutonomousLife', Config.ip_addr, Config.port_num)
            print("ModoAutonomo.conn().getState():", str(ma.getState()))
            return ma
        except Exception as e:
            print("Exception -> ModoAutonomo.conn():", e)
        return False

    @staticmethod
    def alternar():
        try:
            ma = ModoAutonomo.conn()
            if ma.getState() != "disabled":
                return ModoAutonomo.desligar(ma)
            elif ma.getState() == "disabled":
                return ModoAutonomo.ligar(ma)
        except Exception as e:
            print("Exception -> ModoAutonomo.alternar():", e)
        return False

    @staticmethod
    def ligar(ma = False, async = True):
        try:
            if async:
                return AsyncThread.call(lambda: ModoAutonomo.ligar(ma, False))
            if not ma:
                ma = ModoAutonomo.conn()
            if ma.getState() == "disabled":
                ma.setState("safeguard")
            print("ModoAutonomo.conn().getState():", str(ma.getState()))
            return True
        except Exception as e:
            print("Exception -> ModoAutonomo.ligar():", e)
        return False

    @staticmethod
    def desligar(ma = False, async = True):
        try:
            if async:
                return AsyncThread.call(lambda: ModoAutonomo.desligar(ma, False))
            if not ma:
                ma = ModoAutonomo.conn()
            if ma.getState() != "disabled":
                ma.setState("disabled")
            print("ModoAutonomo.conn().getState():", str(ma.getState()))
            #ma.stopAll()
            return True
        except Exception as e:
            print("Exception -> ModoAutonomo.desligar():", e)
        return False

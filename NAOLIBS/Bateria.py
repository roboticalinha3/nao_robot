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
except Exception as e:
    print("Erro ao importar bibliotecas no arquivo Bateria.py", e)

class Bateria:

    @staticmethod
    def conn():
        try:
            return ALProxy('ALBattery', Config.ip_addr, Config.port_num)
        except Exception as e:
            print("Exception -> Bateria.conn():", e)
        return False

    @staticmethod
    def nivel():
        try:
            return Bateria.conn().getBatteryCharge()
        except Exception as e:
            print("Exception -> Bateria.conn():", e)
        return -1

    @staticmethod
    def monitorar(bool_value):
        try:
            Bateria.conn().enablePowerMonitoring(bool_value)
            return True
        except Exception as e:
            print("Exception -> Bateria.monitorar():", e)
        return False
        
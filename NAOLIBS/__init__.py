"""
  GitHub: https://github.com/matheusjohannaraujo/nao_robot
  Country: Brasil
  State: Pernambuco
  Developer: Matheus Johann Araujo
  Date: 2021-03-14
"""

try:
    import os
    import time
    import sys
    import uuid
    import naoqi
    from naoqi import ALProxy
    from AsyncThread import AsyncThread
    from Audio import Audio
    from Bateria import Bateria
    from Camera import Camera
    from Comportamento import Comportamento
    import Config
    from Led import Led
    from Memoria import Memoria
    from ModoAutonomo import ModoAutonomo    
    from Motor import Motor
    from Ouvinte import Ouvinte
    from Print import Print
    from Sensor import Sensor    
    from Sistema import Sistema
    print("NAOLIBS - OK")
except Exception as e:
    print("NAOLIBS - ERROR: ", e)

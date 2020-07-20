"""
  GitHub: https://github.com/matheusjohannaraujo/nao_robot
  Country: Brasil
  State: Pernambuco
  Developer: Matheus Johann Araujo
  Date: 2021-03-05
"""

try:
    import Config
    from naoqi import ALProxy
    import almath
    from AsyncThread import AsyncThread
    from ModoAutonomo import ModoAutonomo
    import time
except Exception as e:
    print("Erro ao importar bibliotecas no arquivo Motor.py", e)

class Motor:

    almotion = False     

    @staticmethod
    def movimento():
        try:
            if Motor.almotion:
                Motor.almotion.stopMove()
                Motor.almotion = False
            Motor.almotion = ALProxy('ALMotion', Config.ip_addr, Config.port_num)
            Motor.almotion.stopMove()        
            return Motor.almotion    
        except Exception as e:
            print("Exception -> Motor.movimento():", e)
        return False

    @staticmethod
    def angulo(nome, tempo = 1.0, angulo = 0):
        try:
            motion = Motor.movimento()
            if motion:
                motion.angleInterpolationBezier(nome, tempo, angulo)
            return True
        except Exception as e:
            print("Exception -> Motor.angulo():", e)
        return False

    """
        MENCAO - By Matheus Johann Araujo
        As funcoes de nome "bracoEsquerdo(params...)" e
        "bracoDireito(params...)" foram desenvolvidas por: 
            Laura Gabrielle de Lira Silva e
            Wesley Oliveira de Souza            
    """
    @staticmethod
    def bracoEsquerdo(nome, angulo = 0, tempo = 1.0, rigidez = 100, async = True):
        if async:
            return AsyncThread.call(lambda: Motor.bracoEsquerdo(nome, angulo, tempo, rigidez, False))
        Motor.rigidezBracoEsquerdo(rigidez)
        angulo = [[float(angulo) * almath.TO_RAD]]
        tempo  = [[tempo]]
        if "antebraco" == nome:# Angulo -120 ate 120
            nome = ["LElbowYaw"]
        elif "mao" == nome:# Angulo -105 ate 105
            nome = ["LWristYaw"]
        elif "cotovelo" == nome:# Angulo -90 ate 0
            nome = ["LElbowRoll"]
        elif "ombro" == nome:# Angulo -18 ate 80
            nome = ["LShoulderRoll"]
        Motor.angulo(nome, tempo, angulo)
        return True

    @staticmethod
    def bracoDireito(nome, angulo = 0, tempo = 1.0, rigidez = 100, async = True):
        if async:
            return AsyncThread.call(lambda: Motor.bracoDireito(nome, angulo, tempo, rigidez, False))
        Motor.rigidezBracoDireito(rigidez)
        angulo = [[float(angulo) * almath.TO_RAD]]
        tempo  = [[tempo]]
        if "antebraco" == nome:# Angulo -120 ate 120
            nome = ["RElbowYaw"]
        elif "mao" == nome:# Angulo -105 ate 105
            nome = ["RWristYaw"]
        elif "cotovelo" == nome:# Angulo -90 ate 0
            nome = ["RElbowRoll"]
        elif "ombro" == nome:# Angulo -18 ate 80
            nome = ["RShoulderRoll"]
        Motor.angulo(nome, tempo, angulo)
        return True

    @staticmethod
    def bracos(nome, angulo = 0, tempo = 1.0, rigidez = 100):
        return Motor.bracoEsquerdo(nome, angulo, tempo, rigidez, True) and Motor.bracoDireito(nome, angulo * -1, tempo, rigidez, False)

    @staticmethod
    def cabecaDireita(angulo = 0, tempo = 1.0, async = False):
        # Angulo de 0 ate 119.5
        if async:
            return AsyncThread.call(lambda: Motor.cabecaDireita(angulo, tempo, False))
        Motor.rigidezCabeca(100)
        nome = ["HeadYaw"]
        tempo  = [[ tempo ]]
        angulo = [[ float(angulo) * almath.TO_RAD]]        
        Motor.angulo(nome, tempo, angulo)
        Motor.rigidezCabeca(10)
        return True

    @staticmethod
    def cabecaEsquerda(angulo = 0, tempo = 1.0, async = False):
        # Angulo de -119.5 ate 0
        return Motor.cabecaDireita(float(angulo) * -1, tempo, async) 

    @staticmethod
    def cabecaBaixo(angulo = 0, tempo = 1.0, async = False):
        # Angulo de 0 ate 29.5
        if async:
            return AsyncThread.call(lambda: Motor.cabecaBaixo(angulo, tempo, False))        
        Motor.rigidezCabeca(100)
        nome = ["HeadPitch"]
        angulo = [[ float(angulo) * almath.TO_RAD]]
        tempo  = [[ tempo ]]
        Motor.angulo(nome, tempo, angulo)
        Motor.rigidezCabeca(10)
        return True
    
    @staticmethod
    def cabecaCima(angulo = 0, tempo = 1.0, async = False):
        # Angulo de 0 ate -38.5
        return Motor.cabecaBaixo(float(angulo) * -1, tempo, async)

    @staticmethod
    def cabecaCentro():
        return Motor.cabecaCima(async = True) and Motor.cabecaDireita()

    @staticmethod
    def rigidez(nome, valor = 100, tempo = 0.1, async = True):
        try:
            motion = Motor.movimento()
            if motion:
                valor = float(valor) / 100
                motion.stiffnessInterpolation(nome, valor, tempo, _async = async)
            return True
        except Exception as e:
            print("Exception -> Motor.rigidez():", e)
        return False

    @staticmethod
    def rigidezCabeca(valor = 100):
        return Motor.rigidez("Head", valor)

    @staticmethod
    def rigidezBracoEsquerdo(valor = 100):
        return Motor.rigidez("LArm", valor)

    @staticmethod
    def rigidezBracoDireito(valor = 100):
        return Motor.rigidez("RArm", valor)

    @staticmethod
    def rigidezBracos(valor = 100):
        return Motor.rigidezBracoEsquerdo(valor) and Motor.rigidezBracoDireito(valor)

    @staticmethod
    def rigidezPernaEsquerda(valor = 100):
        return Motor.rigidez("LLeg", valor)

    @staticmethod
    def rigidezPernaDireita(valor = 100):
        return Motor.rigidez("RLeg", valor)

    @staticmethod
    def rigidezPernas(valor = 100):
        return Motor.rigidezPernaEsquerda(valor) and Motor.rigidezPernaDireita(valor)

    @staticmethod
    def rigidezCorpo(valor = 100):        
        return Motor.rigidez("Body", valor)
        
    @staticmethod
    def maoEsquerda(abrir = True, async = True):
        try:
            if async:            
                return AsyncThread.call(lambda: Motor.maoEsquerda(abrir, False))
            motion = Motor.movimento()
            if motion:
                if abrir:
                    motion.openHand("LHand", _async = True)
                else:
                    motion.closeHand("LHand", _async = True)
                return True
        except Exception as e:
            print("Exception -> Motor.maoEsquerda():", e)
        return False

    @staticmethod
    def maoDireita(abrir = True, async = True):
        try:
            if async:
                return AsyncThread.call(lambda: Motor.maoDireita(abrir, False))
            motion = Motor.movimento()
            if motion:
                if abrir:
                    motion.openHand("RHand", _async = True)
                else:
                    motion.closeHand("RHand", _async = True)
                return True
        except Exception as e:
            print("Exception -> Motor.maoDireita():", e)
        return False

    @staticmethod
    def maos(abrir = True):
        return Motor.maoEsquerda(abrir) and Motor.maoDireita(abrir, False)

    @staticmethod
    def moverPernas(xMetros, yMetros, eixoGraus, posturaStandInit = True):
        try:
            if posturaStandInit:
                Motor.posturaStandInit()
            motion = Motor.movimento()
            initPosition = almath.Pose2D(motion.getRobotPosition(True))
            targetDistance = almath.Pose2D(xMetros, yMetros, eixoGraus * almath.PI / 180)
            expectedEndPosition = initPosition * targetDistance
            motion.setMoveArmsEnabled(True, True)
            varmovimento = motion.moveTo(xMetros, yMetros, eixoGraus * almath.PI / 180)            
            positionErrorThresholdPos = 0.01
            positionErrorThresholdAng = 0.03
            # The move is finished so output
            realEndPosition = almath.Pose2D(motion.getRobotPosition(False))
            positionError = realEndPosition.diff(expectedEndPosition)
            positionError.theta = almath.modulo2PI(positionError.theta)
            if (abs(positionError.x) < positionErrorThresholdPos
                and abs(positionError.y) < positionErrorThresholdPos
                and abs(positionError.theta) < positionErrorThresholdAng):
                print("Movimento OK")
            else:
                print("Movimento ERROR", positionError.toVector())
                Motor.posturaCrouch()
                ModoAutonomo.on()
                time.sleep(0.25)
                ModoAutonomo.off()
                time.sleep(0.25)
                Motor.posturaStandInit()
            return varmovimento
        except Exception as e:
            print("Exception -> Motor.moverPernas():", e)
        return False                    

    @staticmethod
    def pararAndar():
        return Motor.movimento()

    @staticmethod
    def andarFrente(xMetros = 0.025, qtd = 1):
        return Motor.moverPernas(xMetros * qtd, 0, 0)

    @staticmethod
    def andarTras(xMetros = 0.025, qtd = 1):
        return Motor.moverPernas((xMetros * qtd) * -1, 0, 0)

    @staticmethod
    def andarEsquerda(yMetros = 0.025, qtd = 1):
        return Motor.moverPernas(0, yMetros * qtd, 0)

    @staticmethod
    def andarDireita(yMetros = 0.025, qtd = 1):
        return Motor.moverPernas(0, (yMetros * qtd) * -1, 0)

    @staticmethod
    def andarGirandoHorario(eixoGraus = 1):
        return Motor.moverPernas(0, 0, eixoGraus * -1)

    @staticmethod
    def andarGirandoAntiHorario(eixoGraus = 1):
        return Motor.moverPernas(0, 0, eixoGraus)

    @staticmethod
    def postura(pos = "Stand", vel = 0.5):
        try:
            postureProxy = ALProxy('ALRobotPosture', Config.ip_addr, Config.port_num)
            numTentativas = 0
            maxTentativas = 3
            conseguiu = False
            while (numTentativas < maxTentativas):
                result = postureProxy.goToPosture(pos, vel)
                if (result):
                    conseguiu = True
                    break
                else:
                    numTentativas = numTentativas + 1
            return conseguiu
        except Exception as e:
            print("Exception -> Motor.postura():", e)
        return False     

    @staticmethod
    def posturaStand(vel = 0.5):
        return Motor.postura("Stand", vel)

    @staticmethod
    def posturaStandInit(vel = 0.5):
        return Motor.postura("StandInit", vel)

    @staticmethod
    def posturaStandZero(vel = 0.5):
        return Motor.postura("StandZero", vel)

    @staticmethod
    def posturaCrouch(vel = 0.5):
        return Motor.postura("Crouch", vel) and Motor.rigidezCorpo(20)

    @staticmethod
    def posturaSit(vel = 0.5):
        return Motor.postura("Sit", vel) and Motor.rigidezCorpo(20)

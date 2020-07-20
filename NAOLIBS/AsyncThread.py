"""
  GitHub: https://github.com/matheusjohannaraujo/nao_robot
  Country: Brasil
  State: Pernambuco
  Developer: Matheus Johann Araujo
  Date: 2021-01-12
"""

try:
    import sys 
    import trace 
    import threading 
    import time 
except Exception as e:
    print("Erro ao importar bibliotecas no arquivo AsyncThread", e)

class thread_with_trace(threading.Thread):

    def __init__(self, *args, **keywords): 
        threading.Thread.__init__(self, *args, **keywords) 
        self.killed = False
  
    def start(self): 
        self.__run_backup = self.run 
        self.run = self.__run       
        threading.Thread.start(self) 
  
    def __run(self): 
        sys.settrace(self.globaltrace) 
        self.__run_backup() 
        self.run = self.__run_backup 
  
    def globaltrace(self, frame, event, arg): 
        if event == 'call': 
            return self.localtrace 
        else: 
            return None
  
    def localtrace(self, frame, event, arg):
        if self.killed:
            if event == 'line':
                raise SystemExit() 
        return self.localtrace 
  
    def kill(self): 
        self.killed = True
  
class AsyncThread:

    @staticmethod
    def call(target, start = True, args = ()):
        return AsyncThread(target, start, args)
    
    def __init__(self, target, start = True, args = ()):
        try:
            self.thread = thread_with_trace(target = target, args = args) 
            if start:
                self.thread.start()
        except Exception as e:
            print("Exception -> AsyncThread.__init__():", e)

    def start(self):
        if self.thread:
            self.thread.start()

    def stop(self):
        if self.thread:
            self.thread.kill()

    def join(self):
        if self.thread:
            self.thread.join()

    def running(self):
        alive = False
        if self.thread:
            alive = self.thread.isAlive()
        if alive:
            print("Running: ", self)
        return alive

    def timer(self, sleep = 0):
        return AsyncThread(lambda: (
            time.sleep(sleep),
            self.stop()
        ))

"""
def test():
    while True:
        time.sleep(1)        
        print("Test Ok")

at = AsyncThread.call(test)
print(at)
at.running()
at.timer(5)
#time.sleep(3)
#at.stop()
"""

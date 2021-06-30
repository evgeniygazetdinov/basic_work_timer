from threading import Timer,Thread,Event
import os
import sys 
import subprocess
import time
import datetime 

class perpetualTimer():

   def __init__(self,t,hFunction):
      self.t=t
      self.hFunction = hFunction
      self.thread = Timer(self.t,self.handle_function)

   def handle_function(self):
      self.hFunction()

      self.thread = Timer(self.t,self.handle_function)
      self.thread.start()


   def count_time(self):
      counter = self.t
      while(counter):
        counter-=1
        time.sleep(1)
        print(str(datetime.timedelta(seconds=counter)))
      print('stop timer') 

   def start(self):
      self.count_time()
      self.thread.start()

   def cancel(self):
      self.thread.cancel()

def printer():
    opener = "open" if sys.platform == "darwin" else "xdg-open"
    subprocess.call([opener, 'as.mp3'])

t = perpetualTimer(1500,printer)
t.start()

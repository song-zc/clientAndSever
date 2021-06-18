import logging
from sys import argv
import xmlrpc.client
import socket

## This class implements an interactive shell to navigate the file system

class ClientShell():
  def __init__(self,port):
    self.port=port
    self.server=xmlrpc.client.ServerProxy(('http://127.0.0.1:'+str(port))) 
  # implements cd (change directory)
  
  def Check(self,floatList):
    listLen=len(floatList)
    #print(type(floatList))
    for idx in range(listLen):
      if not(floatList[idx].replace(".", "").isdigit()):
        #print (idx)
        print('Input must be a list of numbers')
        return
    
    for idx in range(listLen-1):
      try:
          #print(float(floatList[idx]),float(floatList[idx+1]))
          tup=self.server.check(float(floatList[idx]),float(floatList[idx+1]))
          if tup:
            tup=tuple(tup)
            print (tup)
      except socket.error:
          print ('Check: server is failed')
    return 0

  def Interpreter(self):
    while (True):
      command = input("input a list of floats: ")
      splitcmd = command.split(',')
      #print(splitcmd)
      if splitcmd[0].replace(".","").isdigit():
        self.Check(splitcmd)
      elif splitcmd[0] == "shutdown":
        try:
          self.server.shutdown()
          print ('success shutdown server')
        except socket.error:
          print ('Shutdown: server is failed')
      elif splitcmd[0] == "exit":
        return
      else:
        print ("input not valid.\n")

def main(argv):
  if len(argv)!=1 and len(argv)!=2: #default port 9999
    print ('server need one argument for port or use port 9999 as default') 
    return
  
  if len(argv)==2:
    port=int(argv[1])
  else:
    port=9999
  
  #logging.basicConfig(filename='memoryfs.log', filemode='w', level=logging.DEBUG)

  #logging.info('running on port ',port)
  myshell = ClientShell(port)
  myshell.Interpreter()

    
if __name__ == "__main__":
    main(argv)
  
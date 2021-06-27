import logging
from sys import argv
import os
import argparse

import xmlrpc.client
import socket

import pandas as pd
## This class implements an interactive shell to navigate the file system

class ClientShell():
  def __init__(self,port):
    self.port=port
    self.server=xmlrpc.client.ServerProxy(('http://127.0.0.1:'+str(port))) 
  # implements cd (change directory)
  
  def Check(self,floatList):
    listLen=len(floatList)
    """ from previous interview, check input format
    print(type(floatList))
    for idx in range(listLen):
      if not(floatList[idx].replace(".", "").isdigit()):
        #print (idx)
        print('Input must be a list of numbers')
        return
    """
    for idx in range(listLen-1):
      try:
          #print(float(floatList[idx]),float(floatList[idx+1]))
          tup=self.server.check(float(floatList[idx]),float(floatList[idx+1]))
          if tup:
            tup=tuple(tup)
            print (tup)
      except socket.error:
          print ('Check: server is failed')
    print('search finished')
    return 0

  def LoadFromFile(self,filePath):
    #print(os.path.join("./",filePath))
    try:
      inData=pd.read_csv(os.path.join("./",filePath))
    except OSError as e:
      print(e)
      return
    try:
      floatList=inData['Mass'].dropna().tolist()
    except:
      print('LoadFromFile: invalid input file, should have a column named Mass')
      return
    #print (floatList)
    self.Check(floatList)

  def Interpreter(self):
    while (True):
      command = input("input file name: ")
      """ from previous interview
      splitcmd = command.split(',')
      print(splitcmd)
      if splitcmd[0].replace(".","").isdigit():
        self.Check(splitcmd)
      """
      if command == "shutdown":
        try:
          self.server.shutdown()
          print ('success shutdown server')
        except socket.error:
          print ('Shutdown: server is failed')
      elif command == "exit":
        return
      else:
        self.LoadFromFile(command)
      #else:
        #print ("input not valid.\n")


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('-p', type=int, default=19999, help='port number, default as 19999')
  parser.add_argument('-i', type=str, required=True, help='input file name, must under current work directory')
  opt = parser.parse_args()
  
  port=opt.p
  #logging.basicConfig(filename='memoryfs.log', filemode='w', level=logging.DEBUG)

  #logging.info('running on port ',port)
  myshell = ClientShell(port)
  myshell.LoadFromFile(opt.i)
  myshell.Interpreter()
  
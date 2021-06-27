from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from decimal import Decimal
from sys import argv

class MyServer(SimpleXMLRPCServer):
    def serve_forever(self): #can be shutdown using shutdown
        self.quit = 0
        while not self.quit:
            self.handle_request()

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

##### dictonary constants
RNADICT={'A': 329.0525, 'C': 305.0413, 'G': 345.0474, 'U': 306.0253}

def main(argv):
    if len(argv)!=1 and len(argv)!=2: #default port 19999
        print ('server need one argument for port or use port 19999 as default')
        return

    if len(argv)==2:
        port=int(argv[1])
    else:
        port=19999
    
    server = MyServer(('127.0.0.1', port), \
            requestHandler=RequestHandler) 
    print ('running on port ',port)
    
    lookupDict = dict(zip(RNADICT.values(), RNADICT.keys()))
    
    def check(floatm,floatn): #giving two float, return a tuple if found
        tup=() #return value

        diff = float(Decimal(abs(floatn-floatm)) \
            .quantize(Decimal("0.0001"), rounding = "ROUND_HALF_UP")) #round up
        #print (diff)
        base=lookupDict.get(diff)
        #print(base)
        if base:
            tup=(floatm,floatn,base)
            #print(type(tup))
        return tup
    
    def shutdown(): #shutdown server from client
        server.quit=1
        return 1

    server.register_function(check,'check')
    server.register_function(shutdown,'shutdown')
    server.serve_forever()


if __name__ == "__main__":
    main(argv)
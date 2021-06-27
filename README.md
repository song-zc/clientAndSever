# Interview 2 updated:
Please update the previous project with new features:
1. Instead of taking data from the console, the client will receive a CSV file (enclosed a sample, 
the number of data rows might go up to 1000) as a parameter, load floats from the column 
‘Mass’, and send those floats to the server.
2. The server runs on the public port 19999 and can serve multiple clients simultaneously. It 
finds all the basecallings and returns the result to the client.
## server.py:
Run on default port 19999:
```
  $ python server.py
```
Run on other port:
```
  $ python server.py 8888
```
## client.py:
An input file is required(default port 19999):
```
  $ python client.py -i sample.csv
```
Run on other port:
```
  $ python client.py -p 8888 -i sample.csv
```
After initial run, you can input a new file name for another run:
```
  input file name: test.csv
```

Other commands:
#### shutdown: shutdown server from client

#### exit: shutdown client

# First round interview question:
Please use Python3 to implement a network system; it consists of two parts, the client and the server, both running on the console(terminal). The server runs on the local port 9999 and receives data (a list of floats) from clients. It analyzes the floats, finds all the basecallings, and return them to the client. The client receives user input (comma-separated floats) from the console and sends it to the server. If it gets the data responded from the server, it will print the data onto the console. Definitions: basecalling: if the difference between two floats, floatv and floatu, approximately equals any value of the dict { &#39;A&#39;: 329.0525, &#39;C&#39;: 305.0413, &#39;G&#39;: 345.0474, &#39;U&#39;: 306.0253}, it is called a basecalling, denoted as a tuple (floatv, floatu, base). Where base is ‘A’, ‘C’, ‘G’, or ‘U’. Approximately equal: if |floatm – floatn| <= 1E-6 , then we say that floatm approximately equals floatn.
## server.py:
Run on default port 9999:
```
  $ python server.py
```
Run on other port:
```
  $ python server.py 8888
```
## client.py:
Run on default port 9999:
```
  $ python client.py
```
Run on other port:
```
  $ python client.py 8888
```
#### shutdown: shutdown server from client

#### exit: shutdown client

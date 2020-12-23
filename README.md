# network-communication
These files are class activities for the 2021-1 Real-Time Digital Signal Processing course.

## sendMatrix
This program sends a pre-generated numpy matrix from client to server using 8-bit codification on client side and its respective decodification on server side. Both server and client programs should be run in the same computer.

## serverComms
This program implements client-server communication using basic TCP in Python.
Server and client files can be run in different OS.

This also uses ngrok app so that no public IP on the local machine will be needed. Therefore, a ngrok account and running app are necessary.
For information on installation and activation, visit [ngrok website] (https://ngrok.com/)

Once configured, use the command
```
./ngrok tcp 9999
```
And in the emerged window locate the ngrok-assigned server DNS and client port and insert them in your **client.py** code replacing the following line with your real parameters
```
socket_client.connect( (<SERVER DNS>, <CLIENT PORT>))
```
Example with server DNS: * *0.tcp.ngrok.io* * and client port: * *12345* *
```
socket_client.connect( ("0.tcp.ngrok.io", 12345))
```
Then run **server.py** first and **client.py** after that.
To end the process, in the client terminal write `quit`

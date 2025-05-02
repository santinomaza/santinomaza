# Read web page simple-----------

#import socket

#mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#mysock.connect(('data.pr4e.org', 80))
#cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
#mysock.send(cmd)

#while True:
#    data = mysock.recv(512)
#    if (len(data) < 1) :
#        break
#    print(data.decode(), end = '')
#mysock.close()

#Read webpage sort code-------------

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand :
    for line in fhand :
        print(line.decode().strip())

#Read webpage count words--------------
#import urllib.request, urllib.parse, urllib.error

#fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

#count = dict()
#for line in fhand :
#    words = line.decode().strip()
#    for word in words :
#        count[word] = count.get(word, 0) + 1
#print(count)

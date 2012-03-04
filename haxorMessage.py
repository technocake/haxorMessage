#!/usr/bin/python
#
#	@author: technocake
#	a hackers(the movie)-like interface to give battle cries to your nemesis
#	BIG LETTERS WARNING
#
##############################################

import socket, sys

HOST, PORT = '', 8888

s = socket.socket()

s.bind((HOST, PORT))
s.listen(1)

HTML_HEAD = """HTTP/1.1 200

<!DOCTYPE html>
<style>
	h1 { color: red; }
</style>
"""
MSG_WRAPS = """
<h1>%s</h1>
"""
try:
	while 1:		
		(cs, ip) = s.accept()
		print ( cs.recv(32000) )

		cs.send( HTML_HEAD)
		
		while 1:
			line = raw_input("msg> ")
			cs.send(MSG_WRAPS%(line,))
except Exception as e:
	s.close()
	print e

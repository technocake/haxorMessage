#!/usr/bin/python
#
#	@author: technocake and steinbitglis
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
<html>
    <style>
        body {
            background-color: black;
        }
        .black {
            color: black;
            -o-transition-property: color;
            -o-transition-duration: 1s;
        }
        .red {
            color: red;
            -o-transition-property: color;
            -o-transition-duration: 1s;
        }
        h1, h2, h3, h4, h5, p, a {
            color: green;
            font-family: monospace;
        }
    </style>
    <script>
        function setBlack(e) {
            e.className = 'black';
            setTimeout("setRed(document.getElementById('warning'))", 1000);
        }
        function setRed(e) {
            e.className = 'red';
            setTimeout("setBlack(document.getElementById('warning'))", 1000);
        }
        window.onload = function() {
            setBlack(document.getElementById('warning'));
        }
    </script>

"""
MSG_WRAPS = """
<h1>%s</h1>
"""
HTML_TAIL = """    <h1 id="warning" class="black">&lt;Connection reset by server&gt;</h1>
</html>
"""
try:
	while 1:		
		try:
			(cs, ip) = s.accept()
			print ( cs.recv(32000) )

			cs.send( HTML_HEAD)
			
			while 1:
				line = raw_input("msg> ")
				cs.send(MSG_WRAPS%(line,))
		except KeyboardInterrupt:
			cs.send( HTML_TAIL )
			s.close()
			

except Exception as e:
	print e

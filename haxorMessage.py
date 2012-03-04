#!/usr/bin/python
#
#	@author: technocake and steinbitglis
#	a hackers(the movie)-like interface to give battle cries to your nemesis
#	BIG LETTERS WARNING
#
##############################################

import socket, sys

HOST, PORT = '', 8888


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
        window.onkeypress = function(event) {
            var keynum;
            if(window.event) { // IE8 and earlier
                keynum = event.keyCode; }
            else if(event.which) { // IE9/Firefox/Chrome/Opera/Safari
                keynum = event.which; }

            var keychar = String.fromCharCode(keynum);

            element = document.getElementById('prompt');
            element.innerHTML = element.innerHTML + keychar;
        }
    </script>

    <h1 id="prompt">...</h1>
"""
MSG_WRAPS = """
<h1>&gt; %s</h1>
"""
HTML_TAIL = """    <h1 id="warning" class="black">&lt;Connection reset by server&gt;</h1>
</html>
"""
s = socket.socket()
#Making it able to restart asap on quit ;) (not waiting for TIME_WAIT to expire)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(1)

try:
	while True:		
		try:
			(cs, ip) = s.accept()
			print ( cs.recv(32000) )
			running = True

			cs.send( HTML_HEAD)
			
			while running:
				line = raw_input("msg> ")
				if line == 'q':
					running = False
					cs.send( HTML_TAIL )
					cs.close()
					s.close()
				else:
					cs.send(MSG_WRAPS%(line,))
		except KeyboardInterrupt:
			cs.send( HTML_TAIL )
			s.close()

except Exception as e:
	print e

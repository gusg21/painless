#
# A simple webserver MEANT FOR TESTING based off of http.server.
#

import http.server
import socketserver
import os
from multiprocessing import Process
import generate
import yaml
from threading import Timer

# Credit: http://stackoverflow.com/a/13151299/6388442
class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

def serve(PORT=80, SERVE="."):
	# Declare the processes
	serveProcess = Process(target=rawServe, args=[PORT, SERVE])
	genProcess = Process(target=autoGen)

	serveProcess.start()
	genProcess.start()

def rawServe(PORT, SERVE):
	print("rawServe started.")
	web_dir = os.path.join(os.path.dirname(__file__), SERVE)
	os.chdir(web_dir)

	Handler = http.server.SimpleHTTPRequestHandler
	httpd = socketserver.TCPServer(("", PORT), Handler)
	print("Serving at port: ", PORT)
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		print("^C: Ending rawServe...")

def autoGen():
	print("AutoGen started.")
	print("Loading config...")
	config = yaml.load(open("config/painless.yml", "r").read())
	print("Setting timer...")
	rt = RepeatedTimer(config["options"]["reloadTime"], generate.generate, config["options"]["outputDirectory"]) # Auto-starts

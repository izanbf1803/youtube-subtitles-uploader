import os

settings = {
	"extension": "sbv",
	"API_KEY": "<<YOUR KEY>>",   							#YT api Key
	"PAUSE_CMD": "pause>nul", 								#Comando con el que pausas tu consola
	"py_cmd": "python",  									#Comando con el que llamas a python. Ex: <<python main.py>>
}

def pause():
	os.system(settings["PAUSE_CMD"])
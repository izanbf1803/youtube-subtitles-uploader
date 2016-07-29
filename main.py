#!/usr/bin/env python
# -*- coding: utf-8 -*-

#IMPORT -> LOCAL FILES
from _settings import *
#IMPORT -> LIBARIES
import sys
import os
from os import listdir
from os.path import isfile, join

def error(str, id):
	print("\n\tERROR [{0}]: {1}".format(id ,str))
	pause()
	sys.exit(0)

def main():

	ext = settings["extension"]
	path = None
	all_files_raw = None
	all_files = []
	files_data = []

	try:
		path = sys.argv[1]
	except:
		path = input("RUTA (DIR)->")

	try:
		all_files_raw = [f for f in listdir(path) if isfile(join(path, f))]
	except:
		error("RUTA INVÁLIDA", 1);

	for i in all_files_raw:
		if i[len(i)-(len(ext)+1):len(i)] == "."+ext:
			all_files.append(i)
	del all_files_raw

	for i in all_files:
		files_data.append({
			"id": i[0:i.rfind("_")],
			"lang": i[i.rfind("_")+1:i.rfind("."+ext)],
			"file": "\""+path.replace("\\","/")+"/"+i+"\"",
		})
	print(files_data)
	del all_files

	for i in files_data:
		os.system( "{0} captions.py --videoid={1} --file={2} --language={3} --action=upload".
			format( settings["py_cmd"], i["id"], i["file"], i["lang"] ) )




if __name__ == "__main__":
	main()

pause()
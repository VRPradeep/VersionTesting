'''
This script generates .atl files from Studio projects, in order to make peer review easier. It creates 1 file for each script (template) in the project, pretty-printing some HTML tags in the process.
'''

import os
import sys
import json

file = sys.argv[1]

# set constants
SCRIPTS_KEY = 'templates'
OUTPUT_DIR = file[:-5] + '_peer_review'

# create output directory
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# create script files
with open(file) as inFile:
	data = json.load(inFile)
newFiles = []
for script in data[SCRIPTS_KEY]:
	name = script['id']
	code = script['value']
	code = code.replace("<p>", "\n")
	code = code.replace("</p>", "\n")
	code = code.replace("<br>", "\n")
	code = code.replace("<br/>", "\n")
	code = code.replace("&gt;", ">")
	code = code.replace("&lt;", "<")
	code = code.replace("&amp;", "&")
	atlFileName = name + '.atl'
	newFiles.append(atlFileName)
	atlFile = open(OUTPUT_DIR + '/' + atlFileName, 'w')
	code = code.encode('ascii', 'ignore').decode('ascii')
	atlFile.write(code)

# deleted obsolete script files
for (dirpath, dirnames, filenames) in os.walk(OUTPUT_DIR):
	for filename in filenames:
		if filename.endswith('.atl') and filename not in newFiles:
			os.remove(OUTPUT_DIR + '/' + filename)

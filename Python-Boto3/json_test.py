import json, sys
loaded_json = json.load( sys.stdin )
for x in loaded_json:
	print("%s: %s" % (x, loaded_json[x]))
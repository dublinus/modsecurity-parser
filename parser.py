import json
import sys

f = open(sys.argv[1], 'r')
log = f.read()
f.close()

lines = log.splitlines()

data = {}

entry = {}
parsingHeader = False

for line in lines:
	if line == '': continue
	if line.startswith('--'):
		[id, part] = [x for x in line.split('-') if x != '']
		if(id not in data): data[id] = []
		entry = {'part': part}
		data[id].append(entry)
		parsingHeader = True
		continue
	if parsingHeader:
		entry['header'] = line
		if entry['part'] == 'B':
			headerFields = line.split(' ')
			entry['method'] = headerFields[0]
			entry['path'] = headerFields[1]
		parsingHeader = False
		continue
	(k, _, v) = line.partition(':')
	entry[k] = v

print(json.dumps(data))

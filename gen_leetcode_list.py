import json
from easydict import EasyDict as edict
from pathlib import Path
import os
import numpy as np

cfg = edict()
cfg.solution_dir = Path("./solutions")

def parse_single_code(filename,rank):
	with open(filename) as hd:
		text = hd.read().replace("\n","").replace('\t','')
		start = text.index('"""{') + 3
		end = text.index('}"""', start) + 1
		jsonStr = text[start:end]
		try:
			info = json.loads(jsonStr)
		except:
			print(filename)
			print(jsonStr)
			raise Exception
		link = info['link'].split('/')
		name = link[link.index('problems') + 1]
		info['name'] = ' '.join(name.split('-'))
		tmp = filename.name.split('.')
		if len(tmp) > 2:
			info['version'] = ' '.join(tmp[1].split('-'))
		info['id'] = int(tmp[0])
		info['rank'] = rank
	return info

def parse_all_solutions():
	infos = []
	for rank,file in enumerate(os.popen('ls -U -t {}'.format(str(cfg.solution_dir))).read().strip().split('\n')):
		file = cfg.solution_dir/file
		infos.append(parse_single_code(file,rank))
	infos.sort(key=lambda info: info['rank'], reverse=True)
	return infos

def gen_list():
	dct = {}
	infos = parse_all_solutions()
	for info in infos:
		for category in info['category']:
			dct[category] = dct.get(category, []) + [info]
	output = ""
	st = set()
	for category,infoList in sorted(list(dct.items()), key=lambda tup: np.mean(list(map(lambda info:info['rank'], tup[1]))) , reverse=True):
		output += "## {}\n\n".format(category)
		output += "| Difficulty | Question | Link | Version | Tags |\n"
		output += "| ------ | ------ | ------ | ------ | ------ |\n"
		for info in infoList:
			if info['id'] in st:
				output += "| "" | "" | "" | {} | {} |\n".format(
						info.get('version', ''),
						', '.join(info.get('tags',[])),
					)
			else:
				output += "| {} | [{}. {}]({}) | [link]({}) | {} | {} |\n".format(
						info['difficulty'],
						info['id'], info['name'],  "./solutions/{}.py".format(info['id']),
						info['link'],
						info.get('version', ''),
						', '.join(info.get('tags',[])),
					)
			st.add(info['id'])
	with open("leetcode_list.txt",'w') as hd:
		hd.write(output)



def test_parse_single_code():
	info = parse_single_code(str(cfg.solution_dir/'167.py'))
	assert info['id'] == 167

def test_gen_list():
	gen_list()

if __name__ == '__main__':
	gen_list()
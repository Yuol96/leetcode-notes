import json
from easydict import EasyDict as edict
from pathlib import Path

cfg = edict()
cfg.solution_dir = Path("./solutions")

def parse_single_code(filename):
	with open(filename) as hd:
		text = hd.read().replace("\n","").replace('\t','')
		start = text.index('"""{') + 3
		end = text.index('}"""', start) + 1
		jsonStr = text[start:end]
		info = json.loads(jsonStr)
		link = info['link'].split('/')
		name = link[link.index('problems') + 1]
		info['name'] = ' '.join(name.split('-'))
		info['id'] = int(filename.name.split('.')[0])
	return info

def parse_all_solutions():
	infos = []
	for file in cfg.solution_dir.glob('*'):
		infos.append(parse_single_code(file))
	return infos

def gen_list():
	dct = {}
	infos = parse_all_solutions()
	for info in infos:
		for tag in info['tags']:
			dct[tag] = dct.get(tag, []) + [info]
	output = ""
	for tag,infoList in dct.items():
		output += "## {}\n\n".format(tag)
		output += "| Difficulty | Question | Link to Leetcode |\n"
		output += "| ------ | ------ | ------ |\n"
		for info in infoList:
			output += "| {} | [{}. {}]({}) | [link]({}) |\n".format(
					info['difficulty'],
					info['id'], info['name'],  "./solutions/{}.py".format(info['id']),
					info['link']
				)
	with open("leetcode_list.txt",'w') as hd:
		hd.write(output)



def test_parse_single_code():
	info = parse_single_code(str(cfg.solution_dir/'167.py'))
	assert info['id'] == 167

def test_gen_list():
	gen_list()

if __name__ == '__main__':
	gen_list()
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
			for item in ['link','difficulty','category']:
				item in info
		except:
			print(filename)
			print(jsonStr)
			raise Exception
		link = info['link'].split('/')
		name = link[link.index('problems') + 1]
		info['name'] = ' '.join(name.split('-'))
		tmp = filename.name.split('.')
		if len(tmp) > 2:
			info['version'] = [tmp[1]]
		info['id'] = int(tmp[0])
		info['rank'] = rank
		if "author" not in info:
			info['author'] = "Yucheng Huang"
	return info

def parse_all_solutions():
	infos_dict = {}
	for rank,file in enumerate(os.popen('ls -U -t {}'.format(str(cfg.solution_dir))).read().strip().split('\n')):
		file = cfg.solution_dir/file
		info = parse_single_code(file,rank)
		infoId = info['id']
		if infoId in infos_dict:
			infos_dict[infoId]['version'] += info['version']
			infos_dict[infoId]['tags'] = list(set(infos_dict[infoId]['tags']+info['tags']))
			infos_dict[infoId]['category'] = list(set(infos_dict[infoId]['category']+info['category']))
			infos_dict[infoId]['rank'] = info['rank']
		else :
			infos_dict[infoId] = info

	infos = list(map(lambda tup: tup[1], infos_dict.items()))
	infos.sort(key=lambda info: info['rank'], reverse=True)
	return infos

def get_statistics(infos):
	difficultyCount = {}
	for info in infos:
		difficultyCount[info['difficulty']] = difficultyCount.get(info['difficulty'], 0) + 1 
	stat = {
		"totalNum": len(infos),
		"difficultyCount": difficultyCount,
	}
	return stat

def gen_list():
	dct = {}
	infos = parse_all_solutions()
	totNum = len(infos)
	for info in infos:
		for category in info['category']:
			dct[category] = dct.get(category, []) + [info]
	output = "# Leetcode Solutions\n"
	output += "My leetcode notes and solutions\n\n"
	stat = get_statistics(infos)
	output += "**{}** questions solved in total\n\n**{}** easy questions, **{}** medium questions, and **{}** hard questions\n".format(stat['totalNum'], stat['difficultyCount']['easy'], stat['difficultyCount']['medium'], stat['difficultyCount']['hard'])
	for category,infoList in sorted(list(dct.items()), key=lambda tup: np.mean(list(map(lambda info:info['rank'], tup[1]))) , reverse=True):
		output += "## {}\n".format(category)
		output += "| Difficulty | Question | Version | Tags |\n"
		output += "| ------ | ------ | ------ | ------ |\n"
		for info in infoList:
			if "version" not in info:
				versionStr = "[solution](./solutions/{}.py)".format(info['id'])
			else:
				versionStr = ', '.join(["[{0}](./solutions/{1}.{0}.py)".format(version, info['id']) for version in info['version']])
			output += "| {} | [{}. {}]({}) | {} | {} |\n".format(
					info['difficulty'],
					info['id'], info['name'], info['link'],
					versionStr,
					', '.join(info.get('tags',[])),
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
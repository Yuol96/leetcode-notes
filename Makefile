all: README.md

README.md: leetcode_list.txt
	echo "# leetcode-notes" > README.md
	echo "My leetcode notes and solutions" >> README.md
	echo "[TOC]" >> README.md
	echo "" >> README.md
	cat leetcode_list.txt >> README.md
	rm leetcode_list.txt

leetcode_list.txt: gen_leetcode_list.py
	python3 gen_leetcode_list.py
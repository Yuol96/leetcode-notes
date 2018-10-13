# Introduction

Welcome!

In order to hone my algorithm skills, I have been continuing working on leetcode questions since August 2018. 
To put more focus on algorithms, I choose python3 as my programming language, since it seems to be easier to implement an idea.
Most of the questions have a specific `.py` file under the `solutions/` folder, while some of questions have multiple versions of solutions. 

If you are interested in this repo, feel free to fork it and put your solutions to it. 
Whenever you want to add a new python solution, you need first create a `<id-of-leetcode-question>[.<version-name>].py` file under `solutions/` folder.
You also need to prepend a multi-line comment to your code. Typically it looks like:
```python
"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/",
    "beats": 0.9000,
    "category": ["dynamic-programming"],
    "tags": ["your-whatever-tag-name"],
    "questions": []
}
"""
```
You may also want to add some explaination to your code.
Finally, save your file and input `make` command into your command line tool under the root dir of this repo.
This command collects all the information within the headers of all solutions and regenerate the README.md file.

You should note that without prepending a proper header to your solution files, the `make` command might fail.

I will keep on updating this repo and working on more leetcode questions. You can add this repo into your watchlist so that you will get notified whenever there's an new commit.
# Leetcode Solutions
My leetcode notes and solutions

**154** questions solved in total

**71** easy questions, **77** medium questions, and **6** hard questions
## sort
| Difficulty | Question | Version | Tags |
| ------ | ------ | ------ | ------ |
| medium | [215. kth largest element in an array](https://leetcode.com/problems/kth-largest-element-in-an-array/description/) | [quick-select](./solutions/215.quick-select.py), [heap](./solutions/215.heap.py) | heap, quick-select |
| medium | [347. top k frequent elements](https://leetcode.com/problems/top-k-frequent-elements/description/) | [solution](./solutions/347.py) | topk, bucket-sort |
| medium | [451. sort characters by frequency](https://leetcode.com/problems/sort-characters-by-frequency/description/) | [solution](./solutions/451.py) | bucket-sort |
| medium | [75. sort colors](https://leetcode.com/problems/sort-colors/description/) | [solution](./solutions/75.py) | partition, 三向切分快速排序 |
## two pointers
| Difficulty | Question | Version | Tags |
| ------ | ------ | ------ | ------ |
| easy | [167. two sum ii input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/) | [solution](./solutions/167.py) |  |
| easy | [633. sum of square numbers](https://leetcode.com/problems/sum-of-square-numbers/description/) | [solution](./solutions/633.py) |  |
| easy | [345. reverse vowels of a string](https://leetcode.com/problems/reverse-vowels-of-a-string/description/) | [solution](./solutions/345.py) |  |
| easy | [680. valid palindrome ii](https://leetcode.com/problems/valid-palindrome-ii/description/) | [solution](./solutions/680.py) | palindrome |
| easy | [88. merge sorted array](https://leetcode.com/problems/merge-sorted-array/description/) | [solution](./solutions/88.py) |  |
| easy | [141. linked list cycle](https://leetcode.com/problems/linked-list-cycle/description/) | [solution](./solutions/141.py) | linked-list |
| medium | [524. longest word in dictionary through deleting](https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/) | [original](./solutions/524.original.py), [sorted](./solutions/524.sorted.py) |  |
## greedy
| Difficulty | Question | Version | Tags |
| ------ | ------ | ------ | ------ |
| medium | [455. assign cookies](https://leetcode.com/problems/assign-cookies/description/) | [solution](./solutions/455.py) | binary-search |
| medium | [435. non overlapping intervals](https://leetcode.com/problems/non-overlapping-intervals/description/) | [solution](./solutions/435.py) |  |
| medium | [452. minimum number of arrows to burst balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/) | [solution](./solutions/452.py) |  |
| medium | [406. queue reconstruction by height](https://leetcode.com/problems/queue-reconstruction-by-height/description/) | [optimized](./solutions/406.optimized.py), [original](./solutions/406.original.py) |  |
| medium | [763. partition labels](https://leetcode.com/problems/partition-labels/description/) | [solution](./solutions/763.py) |  |
| easy | [605. can place flowers](https://leetcode.com/problems/can-place-flowers/description/) | [solution](./solutions/605.py) |  |
| medium | [392. is subsequence](https://leetcode.com/problems/is-subsequence/description/) | [solution](./solutions/392.py) | two-pointers |
| easy | [665. non decreasing array](https://leetcode.com/problems/non-decreasing-array/description/) | [solution](./solutions/665.py) | adjacent |
| easy | [122. best time to buy and sell stock ii](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/) | [solution](./solutions/122.py) | adjacent-element |
| medium | [646. maximum length of pair chain](https://leetcode.com/problems/maximum-length-of-pair-chain/description/) | [DP](./solutions/646.DP.py), [greedy](./solutions/646.greedy.py) | overlapping-intervals |
## binary-search
| Difficulty | Question | Version | Tags |
| ------ | ------ | ------ | ------ |
| easy | [69. sqrtx](https://leetcode.com/problems/sqrtx/description/) | [solution](./solutions/69.py) |  |
| easy | [744. find smallest letter greater than target](https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/) | [solution](./solutions/744.py) |  |
| easy | [540. single element in a sorted array](https://leetcode.com/problems/single-element-in-a-sorted-array/description/) | [solution](./solutions/540.py) |  |
| easy | [278. first bad version](https://leetcode.com/problems/first-bad-version/description/) | [solution](./solutions/278.py) |  |
| medium | [153. find minimum in rotated sorted array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/) | [solution](./solutions/153.py) |  |
| medium | [34. find first and last position of element in sorted array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/) | [solution](./solutions/34.py) |  |
## divide-and-conquer
| Difficulty | Question | Version | Tags |
| ------ | ------ | ------ | ------ |
| medium | [241. different ways to add parentheses](https://leetcode.com/problems/different-ways-to-add-parentheses/description/) | [solution](./solutions/241.py) |  |
## BFS
| Difficulty | Question | Version | Tags |
| ------ | ------ | ------ | ------ |
| medium | [279. perfect squares](https://leetcode.com/problems/perfect-squares/description/) | [DP](./solutions/279.DP.py), [BFS](./solutions/279.BFS.py) | integer-break |
| medium | [127. word ladder](https://leetcode.com/problems/word-ladder/description/) | [solution](./solutions/127.py) |  |
| medium | [91. decode ways](https://leetcode.com/problems/decode-ways/description/) | [solution](./solutions/91.py) | integer-break |
## DFS
| Difficulty | Question | Version | Tags |
| ------ | ------ | ------ | ------ |
| easy | [695. max area of island](https://leetcode.com/problems/max-area-of-island/description/) | [solution](./solutions/695.py) |  |
| medium | [200. number of islands](https://leetcode.com/problems/number-of-islands/description/) | [solution](./solutions/200.py) |  |
| medium | [547. friend circles](https://leetcode.com/problems/friend-circles/description/) | [solution](./solutions/547.py) |  |
| medium | [130. surrounded regions](https://leetcode.com/problems/surrounded-regions/description/) | [second](./solutions/130.second.py), [first](./solutions/130.first.py) |  |
| medium | [417. pacific atlantic water flow](https://leetcode.com/problems/pacific-atlantic-water-flow/description/) | [optimized](./solutions/417.optimized.py), [backtracking](./solutions/417.backtracking.py) | border2center, backtracking |
| medium | [93. restore ip addresses](https://leetcode.com/problems/restore-ip-addresses/description/) | [solution](./solutions/93.py) | backtracking |
| medium | [17. letter combinations of a phone number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/) | [solution](./solutions/17.py) | backtracking |
| medium | [79. word search](https://leetcode.com/problems/word-search/description/) | [solution](./solutions/79.py) | backtracking |
| medium | [257. binary tree paths](https://leetcode.com/problems/binary-tree-paths/description/) | [non-recursive](./solutions/257.non-recursive.py), [recursive](./solutions/257.recursive.py) | backtracking, binary-tree |
| medium | [46. permutations](https://leetcode.com/problems/permutations/description/) | [solution](./solutions/46.py) | backtracking |
| medium | [47. permutations ii](https://leetcode.com/problems/permutations-ii/description/) | [sort](./solutions/47.sort.py), [set](./solutions/47.set.py) | backtracking |
| medium | [77. combinations](https://leetcode.com/problems/combinations/description/) | [solution](./solutions/77.py) | backtracking |
| medium | [39. combination sum](https://leetcode.com/problems/combination-sum/description/) | [solution](./solutions/39.py) | backtracking |
| medium | [40. combination sum ii](https://leetcode.com/problems/combination-sum-ii/description/) | [solution](./solutions/40.py) | backtracking |
| medium | [216. combination sum iii](https://leetcode.com/problems/combination-sum-iii/description/) | [solution](./solutions/216.py) | backtracking |
| medium | [78. subsets](https://leetcode.com/problems/subsets/description/) | [solution](./solutions/78.py) | backtracking |
| medium | [90. subsets ii](https://leetcode.com/problems/subsets-ii/description/) | [solution](./solutions/90.py) | backtracking |
| medium | [131. palindrome partitioning](https://leetcode.com/problems/palindrome-partitioning/description/) | [solution](./solutions/131.py) | backtracking, palindrome |
| hard | [37. sudoku solver](https://leetcode.com/problems/sudoku-solver/description/) | [solution](./solutions/37.py) | backtracking |
| hard | [51. n queens](https://leetcode.com/problems/n-queens/description/) | [solution](./solutions/51.py) | backtracking |
| medium | [494. target sum](https://leetcode.com/problems/target-sum/description/) | [DFS](./solutions/494.DFS.py), [DP](./solutions/494.DP.py) | knapsack |
## dynamic-programming
| Difficulty | Question | Version | Tags |
| ------ | ------ | ------ | ------ |
| medium | [279. perfect squares](https://leetcode.com/problems/perfect-squares/description/) | [DP](./solutions/279.DP.py), [BFS](./solutions/279.BFS.py) | integer-break |
| easy | [70. climbing stairs](https://leetcode.com/problems/climbing-stairs/description/) | [accumulative](./solutions/70.accumulative.py), [recursive](./solutions/70.recursive.py) | fibonacci |
| easy | [198. house robber](https://leetcode.com/problems/house-robber/description/) | [third](./solutions/198.third.py), [second](./solutions/198.second.py), [first](./solutions/198.first.py) | fibonacci |
| medium | [213. house robber ii](https://leetcode.com/problems/house-robber-ii/description/) | [solution](./solutions/213.py) | fibonacci |
| medium | [64. minimum path sum](https://leetcode.com/problems/minimum-path-sum/description/) | [second](./solutions/64.second.py), [first](./solutions/64.first.py) | matrix-path |
| medium | [62. unique paths](https://leetcode.com/problems/unique-paths/description/) | [solution](./solutions/62.py) | matrix-path |
| medium | [53. maximum subarray](https://leetcode.com/problems/maximum-subarray/description/) | [second](./solutions/53.second.py), [first](./solutions/53.first.py) | subarray |
| medium | [413. arithmetic slices](https://leetcode.com/problems/arithmetic-slices/description/) | [solution](./solutions/413.py) | subarray |
| medium | [343. integer break](https://leetcode.com/problems/integer-break/description/) | [second](./solutions/343.second.py), [first](./solutions/343.first.py) | integer-break |
| medium | [91. decode ways](https://leetcode.com/problems/decode-ways/description/) | [solution](./solutions/91.py) | integer-break |
| medium | [300. longest increasing subsequence](https://leetcode.com/problems/longest-increasing-subsequence/description/) | [binary-search-replace](./solutions/300.binary-search-replace.py), [DP](./solutions/300.DP.py), [original](./solutions/300.original.py) | subsequence |
| medium | [646. maximum length of pair chain](https://leetcode.com/problems/maximum-length-of-pair-chain/description/) | [DP](./solutions/646.DP.py), [greedy](./solutions/646.greedy.py) | overlapping-intervals |
| medium | [376. wiggle subsequence](https://leetcode.com/problems/wiggle-subsequence/description/) | [solution](./solutions/376.py) | subsequence |
| medium | [416. partition equal subset sum](https://leetcode.com/problems/partition-equal-subset-sum/description/) | [space-optimized](./solutions/416.space-optimized.py), [first](./solutions/416.first.py) | knapsack |
| medium | [494. target sum](https://leetcode.com/problems/target-sum/description/) | [DFS](./solutions/494.DFS.py), [DP](./solutions/494.DP.py) | knapsack |
| medium | [139. word break](https://leetcode.com/problems/word-break/description/) | [solution](./solutions/139.py) | 完全背包 |
| medium | [474. ones and zeroes](https://leetcode.com/problems/ones-and-zeroes/description/) | [solution](./solutions/474.py) | knapsack |
| medium | [322. coin change](https://leetcode.com/problems/coin-change/description/) | [solution](./solutions/322.py) | knapsack, 完全背包 |
| medium | [377. combination sum iv](https://leetcode.com/problems/combination-sum-iv/description/) | [solution](./solutions/377.py) | knapsack, 完全背包 |
| medium | [309. best time to buy and sell stock with cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/) | [space-optimized](./solutions/309.space-optimized.py), [first](./solutions/309.first.py) | state-machine |
| medium | [714. best time to buy and sell stock with transaction fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/) | [solution](./solutions/714.py) | state-machine |
| medium | [121. best time to buy and sell stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/) | [solution](./solutions/121.py) |  |
| hard | [123. best time to buy and sell stock iii](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/) | [solution](./solutions/123.py) | state-machine |
| hard | [188. best time to buy and sell stock iv](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/) | [solution](./solutions/188.py) | state-machine |
| medium | [583. delete operation for two strings](https://leetcode.com/problems/delete-operation-for-two-strings/description/) | [solution](./solutions/583.py) | string |
| medium | [72. edit distance](https://leetcode.com/problems/edit-distance/description/) | [solution](./solutions/72.py) | string |
| medium | [650. 2 keys keyboard](https://leetcode.com/problems/2-keys-keyboard/description/) | [solution](./solutions/650.py) | string |
## math
| Difficulty | Question | Version | Tags |
| ------ | ------ | ------ | ------ |
| easy | [204. count primes](https://leetcode.com/problems/count-primes/description/) | [solution](./solutions/204.py) | prime |
| easy | [504. base 7](https://leetcode.com/problems/base-7/description/) | [second](./solutions/504.second.py), [first](./solutions/504.first.py) | base-conversion |
| easy | [405. convert a number to hexadecimal](https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/) | [solution](./solutions/405.py) | base-conversion |
| easy | [168. excel sheet column title](https://leetcode.com/problems/excel-sheet-column-title/description/) | [solution](./solutions/168.py) | base-conversion |
| easy | [172. factorial trailing zeroes](https://leetcode.com/problems/factorial-trailing-zeroes/description/) | [solution](./solutions/172.py) |  |
| easy | [67. add binary](https://leetcode.com/problems/add-binary/description/) | [solution](./solutions/67.py) | binary, string-number |
| easy | [415. add strings](https://leetcode.com/problems/add-strings/description/) | [solution](./solutions/415.py) | string-number |
| medium | [462. minimum moves to equal array elements ii](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/) | [quick-select](./solutions/462.quick-select.py), [quick-sort](./solutions/462.quick-sort.py) | quick-select, median |
| easy | [169. majority element](https://leetcode.com/problems/majority-element/description/) | [quick-select](./solutions/169.quick-select.py), [boyer-moore](./solutions/169.boyer-moore.py), [quick-sort](./solutions/169.quick-sort.py), [naive](./solutions/169.naive.py) |  |
| easy | [367. valid perfect square](https://leetcode.com/problems/valid-perfect-square/description/) | [delta-array](./solutions/367.delta-array.py), [naive](./solutions/367.naive.py) | square |
| easy | [326. power of three](https://leetcode.com/problems/power-of-three/description/) | [mod](./solutions/326.mod.py), [naive](./solutions/326.naive.py) |  |
| medium | [238. product of array except self](https://leetcode.com/problems/product-of-array-except-self/description/) | [solution](./solutions/238.py) |  |
| easy | [628. maximum product of three numbers](https://leetcode.com/problems/maximum-product-of-three-numbers/description/) | [smart-bruteForce](./solutions/628.smart-bruteForce.py) |  |
## linked-list
| Difficulty | Question | Version | Tags |
| ------ | ------ | ------ | ------ |
| easy | [160. intersection of two linked lists](https://leetcode.com/problems/intersection-of-two-linked-lists/description/) | [solution](./solutions/160.py) |  |
| easy | [206. intersection of two linked lists](https://leetcode.com/problems/intersection-of-two-linked-lists/description/) | [iterative](./solutions/206.iterative.py), [recursive](./solutions/206.recursive.py) |  |
| easy | [21. merge two sorted lists](https://leetcode.com/problems/merge-two-sorted-lists/description/) | [solution](./solutions/21.py) |  |
| easy | [83. remove duplicates from sorted list](https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/) | [solution](./solutions/83.py) |  |
| medium | [19. remove nth node from end of list](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/) | [solution](./solutions/19.py) |  |
| medium | [24. swap nodes in pairs](https://leetcode.com/problems/swap-nodes-in-pairs/description/) | [solution](./solutions/24.py) |  |
| medium | [445. add two numbers ii](https://leetcode.com/problems/add-two-numbers-ii/description/) | [solution](./solutions/445.py) |  |
| easy | [234. palindrome linked list](https://leetcode.com/problems/palindrome-linked-list/description/) | [reverse](./solutions/234.reverse.py), [recursive](./solutions/234.recursive.py) |  |
| medium | [725. split linked list in parts](https://leetcode.com/problems/split-linked-list-in-parts/description/) | [solution](./solutions/725.py) |  |
| medium | [328. odd even linked list](https://leetcode.com/problems/odd-even-linked-list/description/) | [solution](./solutions/328.py) |  |
## tree
| Difficulty | Question | Version | Tags |
| ------ | ------ | ------ | ------ |
| easy | [104. maximum depth of binary tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/) | [solution](./solutions/104.py) | DFS, backtracking |
| easy | [110. balanced binary tree](https://leetcode.com/problems/balanced-binary-tree/description/) | [solution](./solutions/110.py) | DFS |
| easy | [543. diameter of binary tree](https://leetcode.com/problems/diameter-of-binary-tree/description/) | [solution](./solutions/543.py) | DFS |
| easy | [226. invert binary tree](https://leetcode.com/problems/invert-binary-tree/description/) | [solution](./solutions/226.py) | DFS |
| easy | [617. merge two binary trees](https://leetcode.com/problems/merge-two-binary-trees/description/) | [solution](./solutions/617.py) | DFS |
| easy | [112. path sum](https://leetcode.com/problems/path-sum/description/) | [solution](./solutions/112.py) | DFS |
| easy | [437. path sum iii](https://leetcode.com/problems/path-sum-iii/description/) | [solution](./solutions/437.py) | DFS |
| easy | [572. subtree of another tree](https://leetcode.com/problems/subtree-of-another-tree/description/) | [optimized](./solutions/572.optimized.py), [first](./solutions/572.first.py) | DFS |
| easy | [101. symmetric tree](https://leetcode.com/problems/symmetric-tree/description/) | [solution](./solutions/101.py) | DFS |
| easy | [111. minimum depth of binary tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/description/) | [solution](./solutions/111.py) | DFS |
| easy | [404. sum of left leaves](https://leetcode.com/problems/sum-of-left-leaves/description/) | [solution](./solutions/404.py) | DFS |
| easy | [687. longest univalue path](https://leetcode.com/problems/longest-univalue-path/description/) | [solution](./solutions/687.py) | DFS |
| medium | [337. house robber iii](https://leetcode.com/problems/house-robber-iii/description/) | [solution](./solutions/337.py) | DFS |
| easy | [671. second minimum node in a binary tree](https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/) | [solution](./solutions/671.py) | DFS |
| easy | [637. average of levels in binary tree](https://leetcode.com/problems/average-of-levels-in-binary-tree/description/) | [solution](./solutions/637.py) | BFS |
| easy | [513. find bottom left tree value](https://leetcode.com/problems/find-bottom-left-tree-value/description/) | [solution](./solutions/513.py) | BFS |
| medium | [144. binary tree preorder traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/description/) | [iterative-optimized](./solutions/144.iterative-optimized.py), [iterative](./solutions/144.iterative.py), [recursive](./solutions/144.recursive.py) | traversal, DFS |
| hard | [145. binary tree postorder traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/description/) | [iterative-optimized](./solutions/145.iterative-optimized.py), [iterative](./solutions/145.iterative.py) | traversal, DFS |
| medium | [94. binary tree inorder traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/description/) | [iterative](./solutions/94.iterative.py) | DFS, traversal |
| easy | [669. trim a binary search tree](https://leetcode.com/problems/trim-a-binary-search-tree/description/) | [solution](./solutions/669.py) | BST |
| medium | [230. kth smallest element in a bst](https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/) | [recursive](./solutions/230.recursive.py), [preorder](./solutions/230.preorder.py) | BST |
| easy | [538. convert bst to greater tree](https://leetcode.com/problems/convert-bst-to-greater-tree/description/) | [solution](./solutions/538.py) | BST |
| easy | [235. lowest common ancestor of a binary search tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/) | [solution](./solutions/235.py) | BST |
| medium | [236. lowest common ancestor of a binary tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/) | [second](./solutions/236.second.py), [first](./solutions/236.first.py) | DFS |
| easy | [108. convert sorted array to binary search tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/) | [optimized](./solutions/108.optimized.py), [naive](./solutions/108.naive.py) | BST |
| medium | [109. convert sorted list to binary search tree](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/) | [first](./solutions/109.first.py) | BST |
| easy | [653. two sum iv input is a bst](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/) | [solution](./solutions/653.py) | BST |
| easy | [530. minimum absolute difference in bst](https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/) | [solution](./solutions/530.py) | BST |
| easy | [501. minimum absolute difference in bst](https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/) | [no-extra-space](./solutions/501.no-extra-space.py) | BST |
| medium | [208. implement trie prefix tree](https://leetcode.com/problems/implement-trie-prefix-tree/description/) | [dict-optimized](./solutions/208.dict-optimized.py), [dict](./solutions/208.dict.py), [naive](./solutions/208.naive.py) | trie |
| medium | [677. map sum pairs](https://leetcode.com/problems/map-sum-pairs/description/) | [solution](./solutions/677.py) | trie |
## stack and array
| Difficulty | Question | Version | Tags |
| ------ | ------ | ------ | ------ |
| easy | [232. implement queue using stacks](https://leetcode.com/problems/implement-queue-using-stacks/description/) | [solution](./solutions/232.py) |  |
| easy | [225. implement stack using queues](https://leetcode.com/problems/implement-stack-using-queues/description/) | [solution](./solutions/225.py) |  |
| easy | [155. min stack](https://leetcode.com/problems/min-stack/description/) | [solution](./solutions/155.py) |  |
| easy | [20. valid parentheses](https://leetcode.com/problems/valid-parentheses/description/) | [solution](./solutions/20.py) |  |
| medium | [739. daily temperatures](https://leetcode.com/problems/daily-temperatures/description/) | [stack](./solutions/739.stack.py), [naive](./solutions/739.naive.py) |  |
| medium | [503. next greater element ii](https://leetcode.com/problems/next-greater-element-ii/description/) | [solution](./solutions/503.py) |  |
## hash table
| Difficulty | Question | Version | Tags |
| ------ | ------ | ------ | ------ |
| easy | [1. two sum](https://leetcode.com/problems/two-sum/description/) | [solution](./solutions/1.py) | two pointers |
| easy | [217. contains duplicate](https://leetcode.com/problems/contains-duplicate/description/) | [set](./solutions/217.set.py) |  |
| easy | [594. longest harmonious subsequence](https://leetcode.com/problems/longest-harmonious-subsequence/description/) | [solution](./solutions/594.py) |  |
| hard | [128. longest consecutive sequence](https://leetcode.com/problems/longest-consecutive-sequence/description/) | [solution](./solutions/128.py) |  |
## string
| Difficulty | Question | Version | Tags |
| ------ | ------ | ------ | ------ |
| easy | [242. valid anagram](https://leetcode.com/problems/valid-anagram/description/) | [list](./solutions/242.list.py) |  |
| easy | [409. longest palindrome](https://leetcode.com/problems/longest-palindrome/description/) | [solution](./solutions/409.py) | palindrome |
| easy | [205. isomorphic strings](https://leetcode.com/problems/isomorphic-strings/description/) | [second](./solutions/205.second.py), [first](./solutions/205.first.py) |  |
| medium | [647. palindromic substrings](https://leetcode.com/problems/palindromic-substrings/description/) | [solution](./solutions/647.py) | palindrome |
| easy | [9. palindrome number](https://leetcode.com/problems/palindrome-number/description/) | [reverse](./solutions/9.reverse.py), [two-pointers](./solutions/9.two-pointers.py) | palindrome |
| easy | [696. count binary substrings](https://leetcode.com/problems/count-binary-substrings/description/) | [alternative](./solutions/696.alternative.py), [center](./solutions/696.center.py) | palindrome |
## array
| Difficulty | Question | Version | Tags |
| ------ | ------ | ------ | ------ |
| easy | [283. move zeroes](https://leetcode.com/problems/move-zeroes/description/) | [solution](./solutions/283.py) |  |
| easy | [566. reshape the matrix](https://leetcode.com/problems/reshape-the-matrix/description/) | [solution](./solutions/566.py) |  |
| easy | [485. max consecutive ones](https://leetcode.com/problems/max-consecutive-ones/description/) | [solution](./solutions/485.py) |  |
| medium | [240. search a 2d matrix ii](https://leetcode.com/problems/search-a-2d-matrix-ii/description/) | [solution](./solutions/240.py) | BST |
| medium | [378. kth smallest element in a sorted matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/) | [heap](./solutions/378.heap.py), [binary-search](./solutions/378.binary-search.py) |  |
| easy | [645. set mismatch](https://leetcode.com/problems/set-mismatch/description/) | [smart](./solutions/645.smart.py), [naive](./solutions/645.naive.py) |  |
| easy | [448. find all numbers disappeared in an array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/) | [solution](./solutions/448.py) |  |
| medium | [442. find all duplicates in an array](https://leetcode.com/problems/find-all-duplicates-in-an-array/description/) | [solution](./solutions/442.py) |  |
| medium | [287. find the duplicate number](https://leetcode.com/problems/find-the-duplicate-number/description/) | [linked-list](./solutions/287.linked-list.py), [binary-search](./solutions/287.binary-search.py) | linked list circle |

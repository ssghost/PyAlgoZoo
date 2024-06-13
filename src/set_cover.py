from itertools import combinations
from typing import List, Set, Tuple

def brute_set_cover(universe: Set[int], setlist: List[Set[int]]) -> Tuple[int, List[Set[int]]]:
	n = len(setlist)
	res = []
	for i in range(1, n+1):
		for subset in combinations(setlist, i):
			if set.union(*subset) == universe:
				res.append(subset)
	return len(res), res

def greedy_set_cover(universe: Set[int], setlist: List[Set[int]]) -> Tuple[int, List[Set[int]]]:
	uncovered = universe.copy()
	res = []
	while uncovered:
		subset = max(setlist, key = lambda s: len(s & uncovered))
		res.append(subset)
		uncovered -= subset
	return len(res), res
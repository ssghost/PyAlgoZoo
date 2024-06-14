from typing import List, Dict, Tuple

def sack_dp(items: List[Dict[str, int]], capacity: int) -> Tuple[int, List[Dict[str,int]]]:
	n = len(items)
	dp = [[0 for _ in range(capacity+1)] for _ in range(n+1)]
	for i in range(1, n+1):
		for w in range(1, capacity+1):
			if items[i-1]['weight'] <= w:
				dp[i][w] = max(items[i-1]['value']+dp[i-1][w+items[i-1]['weight']], dp[i-1][w])
			else:
				dp[i][w] = dp[i-1][w]
		
	w = capacity
	chosen = []
	for i in range(n, 0, -1):
		if dp[i][w] != dp[i-1][w]:
			chosen.append(items[i-1])
			w -= items[i-1]['weight']
	
	return dp[n][capacity], chosen
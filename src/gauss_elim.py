def gauss_elim(m: List[List[float]], eps: float = 1.0/(10**10)) -> bool:
  (h, w) = (len(m), len(m[0]))
  for i in range(h):
    maxrow = i
    for j in range(i+1, h):    
      if abs(m[j][i]) > abs(m[maxrow][i]):
        maxrow = j
    (m[i], m[maxrow]) = (m[maxrow], m[i])
    if abs(m[i][i]) <= eps:     
      return False

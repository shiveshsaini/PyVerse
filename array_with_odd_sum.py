import sys
 
data = list(map(int, sys.stdin.read().strip().split()))
t = data[0]
idx = 1
out = []
for _ in range(t):
    n = data[idx]; idx += 1
    arr = data[idx:idx+n]; idx += n
    odd = sum(x & 1 for x in arr)
    even = n - odd
    if (odd > 0 and even > 0) or (odd > 0 and n % 2 == 1):
        out.append("YES")
    else:
        out.append("NO")
 
print("\n".join(out))

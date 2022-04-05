(n, m) = [int(x) for x in input().split()]

n_set = set()
for _ in range(n):
    n_set.add(int(input()))

m_set = set()
for _ in range(m):
    m_set.add(int(input()))

print(n_set.intersection(m_set))

from collections import deque

text_list = input().split()
reversed_list = deque()
for el in text_list:
    reversed_list.appendleft(el)

print(" ".join(reversed_list))

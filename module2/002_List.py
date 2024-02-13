l = [10,20,30,40,50,60]

# print(l)
# print(l[50])
# print(l[-1])

# print(200 not in l)

# print(len(l))
# print(max(l))
# print(min(l))

# tp = (1,2,3)
# k = list(tp)
# k.append(50)
# # print(k)
# tpx = tuple(k)
# print(tpx)

# l.extend("python")
# l.insert(5,500)
# print(l)

# print(l.count(20))
# print(l.index(20))
# l.pop()
# print(l)

# l.reverse()
# print(l)

from collections import deque

q = deque([1,2,3,4,5])
print(q)
q.append(10)
print(q)
q.appendleft(100)
print(q)
print(q.pop())
print(q)
print(q.popleft())


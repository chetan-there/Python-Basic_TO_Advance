# 🧠 Think:
# 👉 Ordered, index-based, allows duplicates

arr = [10,20,30,40]

# 🔍 Access
print(arr[0])     # first
print(arr[-1])    # last

# ➕ Insert
arr.append(50)        # end
arr.insert(1, 15)     # index

# 🔄 Update
arr[1] = 99

# 🔁 Loop
for i in range(len(arr)):
    print(i, arr[i])

# ❌ Delete
arr.pop()        # last
arr.pop(1)       # index
arr.remove(30)   # value


# 🧠 Think:
# 👉 Key-Value pair, fast lookup

d = {"name": "chetan", "age": 21}

# 🔍 Access
print(d["name"])
print(d.get("age"))

# ➕ Insert / Update
d["city"] = "Nagpur"
d["age"] = 22

# 🔁 Loop
for key in d:
    print(key, d[key])

# ❌ Delete
del d["age"]
d.pop("name")

# 🧠 Think:
# 👉 No duplicates, unordered

s = {1,2,3}

# 🔍 Check
print(2 in s)

# ➕ Insert
s.add(4)

# 🔁 Loop
for x in s:
    print(x)

# ❌ Delete
s.remove(2)    # error if not present
s.discard(5)   # safe


# 🧠 Think:
# 👉 Last In First Out

stack = []

# ➕ Push
stack.append(10)
stack.append(20)

# 👀 Peek
print(stack[-1])

# ❌ Pop
stack.pop()

# 🔁 Loop
for x in stack:
    print(x)


# 🧠 Think:
# 👉 First In First Out

from collections import deque

q = deque()

# ➕ Enqueue
q.append(10)
q.append(20)

# 👀 Peek
print(q[0])

# ❌ Dequeue
q.popleft()

# 🔁 Loop
for x in q:
    print(x)


# 🧠 Think:
# 👉 Insert/Delete from both ends

from collections import deque

dq = deque()

# ➕ Insert
dq.append(10)       # right
dq.appendleft(5)    # left

# 👀 Peek
print(dq[0], dq[-1])

# ❌ Delete
dq.pop()
dq.popleft()

# 🔁 Loop
for x in dq:
    print(x)


# 🧠 Think:
# 👉 Always gives smallest element

import heapq

heap = []

# ➕ Insert
heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 20)

# 👀 Peek
print(heap[0])

# ❌ Remove smallest
heapq.heappop(heap)

# 🔁 Loop (sorted order)
while heap:
    print(heapq.heappop(heap))
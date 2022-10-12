from collections import deque

queue = deque() # 큐 구현을 위한 deque 라이브러리 사용

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()  #
queue.append(1)
queue.append(4)
queue.popleft()


print(queue)
queue.reverse()
print(queue)
import queue

q_1 = queue.Queue()
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for number in numbers:
    q_1.put(number)

print(q_1.get())
print(q_1.get())
print(q_1.get())

q_2 = queue.LifoQueue()
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for number in numbers:
    q_2.put(number)

print(q_2.get())
print(q_2.get())
print(q_2.get())


q_3 = queue.PriorityQueue()
q_3.put((2, "Hellooo"))
q_3.put((11, 199))
q_3.put((5, 33.33))
q_3.put((1, True))

# while not q_3.empty():
#     print(q_3.get())

while not q_3.empty():
    print(q_3.get()[1])

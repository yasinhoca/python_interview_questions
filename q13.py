#13.Use list as stack, array and queue

# as a list
l = [3,4]
l += [5,6] # [3,4,5,6]

# as a stack
l.append(10)
l.pop() # [3,4,5,6]

# as a queue
l.insert(0,5)
l.pop() # [5,4,5]


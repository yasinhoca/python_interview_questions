#15. Flatten a multi-dimensional list
l = [[10,20,30],[40,50,60],[70,80,90]]
flattened = [x for temp in l for x in temp]
print(flattened) #[10, 20, 30, 40, 50, 60, 70, 80, 90]


from here_code_your_class import Mylist

test = [1,2,0,14,859,-2,12,43].sort()
test_reverse = [1,2,0,14,859,-2,12,43].sort(reverse = True)
print(Mylist([1,2,0,14,859,-2,12,43]).custom_sort() == test)
print(Mylist([]).custom__sort() == [])
print(Mylist([2,3,6,1,0,0,0,-1]).custom_sort() == [6,3,2,1,0,0,0,-1])



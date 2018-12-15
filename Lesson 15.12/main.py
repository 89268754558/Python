from dicter import Mydict


print(Mydict({'Derek':1234, 'Suzan':6543, 'Josh':2}).dict_sort() == [('Josh', 2), ('Derek', 1234), ('Suzan', 6543)] )
print(Mydict({'John':0, 'Slash':0, 'Josh':2}).dict_sort() ==  [('John', 0), ('Slash', 0), ('Josh', 2)])
print(Mydict({'Janna':-1}).dict_sort() == [('Janna', -1)])
print(Mydict({}).dict_sort() == [] )
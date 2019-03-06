from calc_clone import add,sub,div,mult



def test_add():
    if add(2,3) == 5:
        print("Test add(a,b) OK!")
    else:
        print("Test add(a,b) NOT OK!")

def test_sub():
    if sub(2,3) == -1:
        print("Test sub(a,b) OK!")
    else:
        print("Test sub(a,b) NOT OK!")

def test_mult():
    if mult(2,3) == 6:
        print("Test mult(a,b) OK!")
    else:
        print("Test mult(a,b) NOT OK!")


test_add()
test_sub()
test_mult()


from add import add,sub,mul
from mymodule import checknum
from module2 import Person
result=add(4,5)
print(result)
result1=sub(5,6)
print(result1)
result2=mul(10,5)
print(result2)
checknum(150)
try:
    checknum(1150)
except Exception as e:
    print(e)
person=Person()
person.printname("sample")


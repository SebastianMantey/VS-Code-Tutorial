print("start of program")

# print elements of the list
lst = [1, 2, 3]
for element in lst:
    print(element)


# working with functions
def square(number):
    result = number**2
    return result

x = square(2)
print(x)

x = square(3)
print(x)


# working with classes
class SomeClass:
    x = square(2)

    def some_method(self):
        print("method executed")
        return

instance = SomeClass()
instance.some_method()


# working with modules
import my_module
my_module.function_1()
my_module.function_2()

print("end of program")

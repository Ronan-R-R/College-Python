class mylist:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)
my_list = mylist([1,2,3,4])
print(len(my_list))

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age}"
    
person = person("john", 30)
print(str(person))
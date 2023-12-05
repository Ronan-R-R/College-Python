from dataclasses import dataclass

@dataclass
class person:
    name: str
    age: int
    email: str = None

person1 = person("John", 30)
person2 = person("Jane", 25, "jane@email.com")
print(person1)
print(person2)
print(person1 == person2) #will be false
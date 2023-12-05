class duck:
    def quack(self):
        print("QUACK, QUACK!")

class person:
    def quack(self):
        print("I'm quacking like a duck!")

def make_quack(obj):
    obj.quack()

duck = duck()
person = person()

make_quack(duck)
make_quack(person)
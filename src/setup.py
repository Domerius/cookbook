class Person:
    def __init__(self, name, age):
        self.forname = name.split()[0]
        self.surname = name.split()[-1]
        self.age = age

    def celebrate_birthsday(self):
        self.age += 1

def run():
    pass

if __name__ == '__main__':
    run()
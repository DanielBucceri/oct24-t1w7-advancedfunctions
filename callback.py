def greet(name, cb):
    print(f'Hello, {name}!')

    cb(name)

def say_bye():
    print(f"Bye!!")

#main
greet('steve')
say_bye()
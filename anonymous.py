def greet(name, cb):
    print(f'Hello, {name}!')

    cb()

# def say_bye():
#     print(f"Bye!!")
say_bye = lambda: print(f"Bye!!")

#main
greet('steve', say_bye)

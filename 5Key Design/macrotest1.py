import pyperclip as pc #mcb libraries

storage = {0:"hi", 1:"hey", 2:"hello"}

def catch(key):
    storage[key] = pc.paste()

def release(key):
    pc.copy(str(storage[key]))
    storage[key] = pc.paste()


pc.copy(input("Enter some shit"))
catch(1)
release(1)

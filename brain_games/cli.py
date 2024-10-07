import prompt

def ask_name():
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")

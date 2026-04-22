import os

def greet(name):
    print("Hello " + name)

def run_command(cmd):
    os.system(cmd)  # ⚠️ vulnerable (command injection)

if __name__ == "__main__":
    user = input("Enter your name: ")
    greet(user)

    command = input("Enter command: ")
    run_command(command)

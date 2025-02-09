import time
import sys
from datetime import datetime

tasks = []
current_color = "\033[0m"  # Default color

def add_task(task):
    tasks.append(task)
    print(f"{current_color}Task '{task}' added.{current_color}")

def view_tasks():
    if tasks:
        print(f"{current_color}Your tasks:{current_color}")
        for idx, task in enumerate(tasks, 1):
            print(f"{current_color}{idx}. {task}{current_color}")
    else:
        print(f"{current_color}No tasks to show.{current_color}")

def remove_task(task_number):
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"{current_color}Task '{removed_task}' removed.{current_color}")
    else:
        print(f"{current_color}Invalid task number.{current_color}")

def echo_command(text):
    print(f"{current_color}Echo: {text}{current_color}")

def fun_command():
    print("\nHere's something fun!")
    print("  _____")
    print(" /     \\")
    print("| () () |")
    print(" \\  ^  /")
    print("  |||||")
    print("  |||||")
    print(f"{current_color}You found a cute owl! 🦉{current_color}")

def animated_train():
    train = [
        "🚂     🚂     🚂     🚂     🚂   ",
        "     🚂     🚂     🚂     🚂     ",
        "   🚂     🚂     🚂     🚂     🚂",
        "     🚂     🚂     🚂     🚂     ",
        "🚂     🚂     🚂     🚂     🚂   "
    ]
    print(f"\n{current_color}Enjoy the animated train!{current_color}")
    while True:
        for frame in train:
            sys.stdout.write("\r" + frame)
            sys.stdout.flush()
            time.sleep(0.2)

def basic_calculator():
    print(f"{current_color}\nBasic Calculator{current_color}")
    print(f"{current_color}Enter operation (e.g. 3 + 4 or 5 * 6):{current_color}")
    expression = input("> ").strip()
    try:
        result = eval(expression)
        print(f"{current_color}Result: {result}{current_color}")
    except Exception as e:
        print(f"{current_color}Error: {e}{current_color}")

def run_test():
    questions = [
        {"question": "What is 2 + 2?", "answer": "4"},
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "What is 5 * 6?", "answer": "30"}
    ]

    score = 0
    print(f"\n{current_color}Test Time! Answer the following questions:{current_color}")

    for q in questions:
        print(f"{current_color}{q['question']}{current_color}")
        user_answer = input("> ").strip()
        if user_answer.lower() == q["answer"].lower():
            score += 1
            print(f"{current_color}Correct!{current_color}")
        else:
            print(f"{current_color}Incorrect. The correct answer is {q['answer']}.{current_color}")

    print(f"{current_color}\nYour score: {score}/{len(questions)}{current_color}")

def view_time():
    """View current time."""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{current_color}Current Time: {current_time}{current_color}")

def change_text_color(color):
    """Change terminal text color."""
    global current_color
    color_dict = {
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "reset": "\033[0m"
    }
    if color in color_dict:
        current_color = color_dict[color]
        print(f"{current_color}Text color changed to {color}.{color_dict['reset']}")
    else:
        print(f"{current_color}Invalid color!{current_color}")

def help_command():
    print(f"\n{current_color}Available Commands:{current_color}")
    print(f"{current_color}  !add <task>       - Add a new task{current_color}")
    print(f"{current_color}  !view             - View all tasks{current_color}")
    print(f"{current_color}  !remove <number>  - Remove a task by its number{current_color}")
    print(f"{current_color}  !echo <text>      - Echo back the text{current_color}")
    print(f"{current_color}  !fun              - Display something fun{current_color}")
    print(f"{current_color}  !train            - Animated moving train{current_color}")
    print(f"{current_color}  !calc             - Launch the basic calculator{current_color}")
    print(f"{current_color}  !test             - Run a basic test{current_color}")
    print(f"{current_color}  !time             - View current time{current_color}")
    print(f"{current_color}  !color <color>    - Change text color{current_color}")
    print(f"{current_color}  !help             - Show this help message{current_color}")
    print(f"{current_color}  !exit             - Exit the program{current_color}")

def start_cli():
    print(f"{current_color}Welcome to the Enhanced To-Do List CLI!{current_color}")
    print(f"{current_color}Type '!help' to see a list of commands.\n{current_color}")

    while True:
        command = input("> ").strip().split(maxsplit=1)
        cmd = command[0].lower()
        args = command[1] if len(command) > 1 else None

        if cmd == "!add":
            if args:
                add_task(args)
            else:
                print(f"{current_color}Error: Please provide a task to add.{current_color}")
        elif cmd == "!view":
            view_tasks()
        elif cmd == "!remove":
            if args and args.isdigit():
                remove_task(int(args))
            else:
                print(f"{current_color}Error: Please provide a valid task number.{current_color}")
        elif cmd == "!echo":
            if args:
                echo_command(args)
            else:
                print(f"{current_color}Error: Please provide text to echo.{current_color}")
        elif cmd == "!fun":
            fun_command()
        elif cmd == "!train":
            animated_train()
        elif cmd == "!calc":
            basic_calculator()
        elif cmd == "!test":
            run_test()
        elif cmd == "!time":
            view_time()
        elif cmd == "!color":
            if args:
                change_text_color(args)
            else:
                print(f"{current_color}Error: Please provide a valid color.{current_color}")
        elif cmd == "!help":
            help_command()
        elif cmd == "!exit":
            print(f"{current_color}Exiting...{current_color}")
            break
        else:
            print(f"{current_color}Error: Unknown command. Type '!help' for a list of commands.{current_color}")

if __name__ == "__main__":
    start_cli()

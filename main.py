tasks = []

def menu():
	print("1. Add Task")
	print("2. View Tasks")
	print("3. Complete Tasks")
	print("4. Do nothing ")


def add_task():
	task = input("Enter task: ")
	tasks.append(task)
	print("Tasks added")

def do_nothing():
	pass

menu()

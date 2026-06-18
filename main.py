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

def view_tasks():
	for task in tasks:
		print(task)

def complete_task():
	task = input("Enter task to complete:")
	if task in tasks:
		tasks.remove(task)
		print("Task completed")


def do_nothing():
	print("Did nothing")
	pass

while True:
	menu()
	choice = input("Choose option: ")

	if choice == "1":
		add_task()

	elif choice == "2":
		view_tasks()
	elif choice == "3":
		complete_task()
	elif choice == "4":
		do_nothing()

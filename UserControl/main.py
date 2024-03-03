import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dj_users_tasks.settings")
django.setup()

from users.models import User, Task

def add_user(login, email, role):
    if role in User.Role:
        user = User(
            login=login,
            email=email,
            role=role
        )
        user.save()
        return user

def add_task(name, description):
    task = Task(
        title=name,
        description=description
    )
    
    task.save()
    return task


def add_user_task(task_id, user_id):
    task = Task.objects.get(id=task_id)
    user = User.objects.get(id=user_id)
    task.user = user
    task.save()
    return task.user


def change_task_status(task_id, status):
    if status in Task.Status:
        task = Task.objects.get(id=task_id)
        task.status = status
        task.save()
    

def main():
    while True:
        ask = int(input("Add user - 1\nAdd task - 2\nAdd to user task - 3\nShow tasks - 4\nChange task status - 5\nExit - 0\n"))

        match ask:
            case 1:
                name = input("Name: ")
                email = input("Email: ")
                role = input("Role (admin/user):")
                print(add_user(name, email, role))
            case 2:
                title = input("Title: ")
                description = input("Description:")
                print(add_task(title, description))
            case 3:
                user_id = int(input("User id: "))
                task_id = int(input("Task id: "))
                print(add_user_task(task_id, user_id))
            case 4:
                print("Here is all tasks:")
                for task in Task.objects.all():
                    print(f"{task.id}. Task name: {task.title}, user: {task.user.login if task.user != None else "No user"}, status: {task.status}")
            case 5:
                task_id = int(input("Enter task id:"))
                status = input("Enter task status(done, processing, no work): ")
                change_task_status(task_id, status)
            case 0:
                break



if __name__ == "__main__":
    main()

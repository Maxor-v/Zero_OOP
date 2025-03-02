# Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.due_date}, Статус: {status}"

# Список для хранения задач
tasks = []

# Функция для добавления задачи
def add_task(description, due_date):
    new_task = Task(description, due_date)
    tasks.append(new_task)
    print(f"Задача добавлена: {new_task}")


# Функция для отметки задачи как выполненной
def complete_task(description):
    for task in tasks:
        if task.description == description:
            task.mark_as_completed()
            print(f"Задача выполнена: {task}")
            return
    print(f"Задача с описанием '{description}' не найдена.")


# Функция для вывода текущих (не выполненных) задач
def show_current_tasks():
    current_tasks = [task for task in tasks if not task.completed]
    if not current_tasks:
        print("Нет текущих задач.")
    else:
        print("Текущие задачи:")
        for task in current_tasks:
            print(task)


# Пример использования
add_task("Купить молоко", "2023-10-15")
add_task("Позвонить другу", "2023-10-16")
add_task("Записаться на курс", "2023-10-20")

show_current_tasks()

complete_task("Купить молоко")

show_current_tasks()
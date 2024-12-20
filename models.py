from datetime import datetime
from enum import Enum
from typing import Optional, List


class TaskPriority(Enum):
    """Перечисление для приоритетов задачи.

    Attributes:
        LOW: Низкий приоритет
        MEDIUM: Средний приоритет
        HIGH: Высокий приоритет
        URGENT: Срочный приоритет
    """
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    URGENT = 4


class TaskStatus(Enum):
    """Перечисление для статусов задачи.

    Attributes:
        NEW: Новая задача
        IN_PROGRESS: В работе
        ON_REVIEW: На проверке
        DONE: Выполнена
    """
    NEW = "new"
    IN_PROGRESS = "in_progress"
    ON_REVIEW = "on_review"
    DONE = "done"


class Task:
    """Класс для представления задачи в системе.

    Args:
        title (str): Название задачи
        description (str): Описание задачи
        priority (TaskPriority): Приоритет задач��
        deadline (datetime): Срок выполнения

    Attributes:
        id (int): Уникальный идентификатор задачи
        status (TaskStatus): Текущий статус задачи
        created_at (datetime): Дата создания
        assigned_to (Optional[User]): Исполнитель задачи
    """

    def __init__(self, title: str, description: str,
                 priority: TaskPriority, deadline: datetime):
        self.title = title
        self.description = description
        self.priority = priority
        self.deadline = deadline
        self.status = TaskStatus.NEW
        self.created_at = datetime.now()
        self.assigned_to = None

    def assign_to(self, user: 'User') -> None:
        """Назначает задачу пользователю.

        Args:
            user (User): Пользователь, которому назначается задача
        """
        self.assigned_to = user

    def change_status(self, new_status: TaskStatus) -> None:
        """Изменяет статус задачи.

        Args:
            new_status (TaskStatus): Новый статус задачи
        """
        self.status = new_status 
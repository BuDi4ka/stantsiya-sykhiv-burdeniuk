from src.scripts.database import DatabaseConnection
from src.scripts.dao.user_dao import UserDAO
from src.scripts.dao.project_dao import ProjectDAO
from src.scripts.dao.board_dao import BoardDAO
from src.scripts.dao.column_dao import ColumnDAO
from src.scripts.dao.task_dao import TaskDAO
from src.scripts.dao.task_column_link_dao import TaskColumnLinkDAO
from src.scripts.dao.comment_dao import CommentDAO

from src.scripts.models import User, Project, Board, Column, Task, Comment
from datetime import datetime, date

import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

def main():
    db = DatabaseConnection()

    user_dao = UserDAO(db)
    project_dao = ProjectDAO(db)
    board_dao = BoardDAO(db)
    column_dao = ColumnDAO(db)
    task_dao = TaskDAO(db)
    task_column_link_dao = TaskColumnLinkDAO(db)
    comment_dao = CommentDAO(db)

    # Створюємо користувача
    new_user = User(id=None, username="Oksana", email="oksana@example.com", password_hash="hashed_pwd_456")
    new_user = user_dao.add_user(new_user)
    print(f"User created: {new_user}")

    # Створюємо проект
    new_project = Project(id=None, title="New Project", description="Project description here", owner_id=new_user.id)
    new_project = project_dao.add_project(new_project)
    print(f"Project created: {new_project}")

    # Створюємо дошку для проекту
    new_board = Board(id=None, title="Main Board", project_id=new_project.id)
    new_board = board_dao.add_board(new_board)
    print(f"Board created: {new_board}")

    # Створюємо колонки на дошці
    todo_column = Column(id=None, title="To Do", board_id=new_board.id, order_num=1)
    inprogress_column = Column(id=None, title="In Progress", board_id=new_board.id, order_num=2)
    todo_column = column_dao.add_column(todo_column)
    inprogress_column = column_dao.add_column(inprogress_column)
    print(f"Columns created: {todo_column}, {inprogress_column}")

    # Створюємо задачу
    task = Task(
        id=None,
        title="Finish report",
        description="Complete the quarterly report",
        start_date=date(2025, 5, 20),
        end_date=date(2025, 5, 30),
        status="Open",
        project_id=new_project.id,
        assignee_id=new_user.id
    )
    task = task_dao.add_task(task)
    print(f"Task created: {task}")

    # Пов'язуємо задачу з колонкою
    task_column_link_dao.link_task_to_column(task.id, todo_column.id)
    print(f"Task {task.id} linked to column {todo_column.id}")

    # Додаємо коментар
    comment = Comment(
        id=None,
        task_id=task.id,
        author_id=new_user.id,
        content="Починаю роботу над звітом",
        timestamp=datetime.now()
    )
    comment = comment_dao.add_comment(comment)
    print(f"Comment added: {comment}")

    db.close()

if __name__ == "__main__":
    main()

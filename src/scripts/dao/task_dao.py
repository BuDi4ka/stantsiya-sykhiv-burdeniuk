from src.scripts.models import Task
from datetime import datetime

class TaskDAO:
    def __init__(self, db):
        self.db = db

    def add_task(self, task: Task) -> Task:
        sql = """
        INSERT INTO Task (title, description, start_date, end_date, status, project_id, assignee_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        self.db.execute(sql, (
            task.title,
            task.description,
            task.start_date,
            task.end_date,
            task.status,
            task.project_id,
            task.assignee_id
        ))
        task.id = self.db.cursor.lastrowid
        return task

    def get_tasks_by_project(self, project_id: int):
        sql = "SELECT * FROM Task WHERE project_id = %s"
        self.db.execute(sql, (project_id,))
        rows = self.db.fetchall()
        return [Task(**row) for row in rows]

    def get_task_by_id(self, task_id: int) -> Task | None:
        sql = "SELECT * FROM Task WHERE id = %s"
        self.db.execute(sql, (task_id,))
        row = self.db.fetchone()
        if row:
            return Task(**row)
        return None

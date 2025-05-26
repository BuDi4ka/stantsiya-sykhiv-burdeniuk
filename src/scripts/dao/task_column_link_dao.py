class TaskColumnLinkDAO:
    def __init__(self, db):
        self.db = db

    def link_task_to_column(self, task_id: int, column_id: int):
        sql = "INSERT INTO TaskColumnLink (task_id, column_id) VALUES (%s, %s)"
        self.db.execute(sql, (task_id, column_id))

    def get_columns_by_task(self, task_id: int):
        sql = "SELECT column_id FROM TaskColumnLink WHERE task_id = %s"
        self.db.execute(sql, (task_id,))
        rows = self.db.fetchall()
        return [row['column_id'] for row in rows]


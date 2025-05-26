from src.scripts.models import Comment

class CommentDAO:
    def __init__(self, db):
        self.db = db

    def add_comment(self, comment: Comment) -> Comment:
        sql = "INSERT INTO Comment (task_id, author_id, content, timestamp) VALUES (%s, %s, %s, %s)"
        self.db.execute(sql, (comment.task_id, comment.author_id, comment.content, comment.timestamp))
        comment.id = self.db.cursor.lastrowid
        return comment

    def get_comments_by_task(self, task_id: int):
        sql = "SELECT * FROM Comment WHERE task_id = %s ORDER BY timestamp"
        self.db.execute(sql, (task_id,))
        rows = self.db.fetchall()
        return [Comment(**row) for row in rows]

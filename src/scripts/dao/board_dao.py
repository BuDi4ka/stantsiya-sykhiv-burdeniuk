from src.scripts.models import Board

class BoardDAO:
    def __init__(self, db):
        self.db = db

    def add_board(self, board: Board) -> Board:
        sql = "INSERT INTO Board (title, project_id) VALUES (%s, %s)"
        self.db.execute(sql, (board.title, board.project_id))
        board.id = self.db.cursor.lastrowid
        return board

    def get_boards_by_project(self, project_id: int):
        sql = "SELECT * FROM Board WHERE project_id = %s"
        self.db.execute(sql, (project_id,))
        rows = self.db.fetchall()
        return [Board(**row) for row in rows]


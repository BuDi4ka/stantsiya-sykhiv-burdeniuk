from src.scripts.models import Column

class ColumnDAO:
    def __init__(self, db):
        self.db = db

    def add_column(self, column: Column) -> Column:
        sql = "INSERT INTO `Column` (title, board_id, `order_num`) VALUES (%s, %s, %s)"
        self.db.execute(sql, (column.title, column.board_id, column.order_num))
        column.id = self.db.cursor.lastrowid
        return column

    def get_columns_by_board(self, board_id: int):
        sql = "SELECT * FROM `Column` WHERE board_id = %s ORDER BY `order_num`"
        self.db.execute(sql, (board_id,))
        rows = self.db.fetchall()
        return [Column(**row) for row in rows]


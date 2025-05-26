from src.scripts.models import User

class UserDAO:
    def __init__(self, db):
        self.db = db

    def add_user(self, user: User) -> User:
        sql = "INSERT INTO User (username, email, passwordHash) VALUES (%s, %s, %s)"
        self.db.execute(sql, (user.username, user.email, user.password_hash))
        user.id = self.db.cursor.lastrowid
        return user

    def get_user_by_username(self, username: str) -> User | None:
        sql = "SELECT * FROM User WHERE username = %s"
        self.db.execute(sql, (username,))
        row = self.db.fetchone()
        if row:
            return User(**row)
        return None

    def list_users(self):
        sql = "SELECT * FROM User"
        self.db.execute(sql)
        rows = self.db.fetchall()
        return [User(**row) for row in rows]

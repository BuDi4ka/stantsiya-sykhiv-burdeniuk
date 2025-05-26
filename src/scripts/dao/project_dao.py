from src.scripts.models import Project

class ProjectDAO:
    def __init__(self, db):
        self.db = db

    def add_project(self, project: Project) -> Project:
        sql = "INSERT INTO Project (title, description, owner_id) VALUES (%s, %s, %s)"
        self.db.execute(sql, (project.title, project.description, project.owner_id))
        project.id = self.db.cursor.lastrowid
        return project

    def get_projects_by_owner(self, owner_id: int):
        sql = "SELECT * FROM Project WHERE owner_id = %s"
        self.db.execute(sql, (owner_id,))
        rows = self.db.fetchall()
        return [Project(**row) for row in rows]

from dataclasses import dataclass
from typing import Optional
from datetime import date, datetime

@dataclass
class User:
    id: Optional[int]
    username: str
    email: str
    password_hash: str

@dataclass
class Project:
    id: Optional[int]
    title: str
    description: Optional[str]
    owner_id: int

@dataclass
class Board:
    id: Optional[int]
    title: str
    project_id: int

@dataclass
class Column:
    id: Optional[int]
    title: str
    board_id: int
    order_num: int

@dataclass
class Task:
    id: Optional[int]
    title: str
    description: Optional[str]
    start_date: Optional[date]
    end_date: Optional[date]
    status: str
    project_id: int
    assignee_id: Optional[int]

@dataclass
class TaskColumnLink:
    task_id: int
    column_id: int

@dataclass
class Comment:
    id: Optional[int]
    task_id: int
    author_id: int
    content: str
    timestamp: datetime

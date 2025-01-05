from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class UserBase(db.Model, UserMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(50),unique=True, nullable=False)
    nickname: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120),unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(120), nullable=False)
    user_type: Mapped[str] = mapped_column(String(50), nullable=False, default="user")

    def __init__(self, username, nickname, email, password, user_type="user"):
        super().__init__()
        self.username = username
        self.nickname = nickname
        self.email = email
        self.password = generate_password_hash(password)
        self.user_type = user_type

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def has_access(self, permission):
        return self.user_type == permission


class Admin(UserBase):
    def __init__(self, username, nickname, email, password):
        super().__init__(username, nickname, email, password, user_type="admin")
    
    def has_access(self, permission):
        return True
    

class Student(db.Model):
    __tablename__ = "students"


    registration_number: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    series: Mapped[str] = mapped_column(String(15), nullable=False)

    def __init__(self, name, registration_number, series):
        self.name = name
        self.registration_number = registration_number
        self.series = series
from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from app.core.database import Base
from sqlalchemy.orm import relationship, Mapped,mapped_column

class User(Base):
    __tablename__ = "users"

    id : Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    password: Mapped[str]
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    role_id: Mapped[int] = mapped_column(Integer, ForeignKey("roles.id"))


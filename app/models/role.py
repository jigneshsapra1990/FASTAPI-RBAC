from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.core.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255), unique=True, index=True)


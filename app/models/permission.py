from sqlalchemy import create_engine, String
from app.core.database import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column

class Permission(Base):
    __tablename__ = "permissions"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    description: Mapped[str] = mapped_column(String(255))
    

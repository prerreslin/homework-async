from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, mapped_column, DeclarativeBase, Mapped

Engine = create_engine("sqlite:///users.db",echo=True)
Session = sessionmaker(Engine)

class Base(DeclarativeBase):
    id:Mapped[int] = mapped_column(primary_key = True)


class User(Base):
    __tablename__ = "users"
    
    name:Mapped[str]

Base.metadata.create_all(bind=Engine)
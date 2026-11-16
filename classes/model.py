import sqlalchemy as sql

from .base import Base


class Model(Base):
    __tablename__ = "models"

    id = sql.Column(sql.Integer, primary_key=True)
    model = sql.Column(sql.String(100), nullable=False)

    def __repr__(self) -> str:
        return f"<ID=(id={self.id}, model='{self.model}')>"

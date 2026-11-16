import sqlalchemy as sql

from .base import Base


class Color(Base):
    __tablename__ = "colors"

    id = sql.Column(sql.Integer, primary_key=True)
    color = sql.Column(sql.String(100), nullable=False)

    def __repr__(self) -> str:
        return f"<ID=(id={self.id}, color='{self.color}')>"
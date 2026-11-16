import sqlalchemy as sql

from .base import Base


class Body(Base):
    __tablename__ = "bodies"

    id = sql.Column(sql.Integer, primary_key=True)
    body = sql.Column(sql.String(100), nullable=False)

    def __repr__(self) -> str:
        return f"<ID=(id={self.id}, body='{self.body}')>"

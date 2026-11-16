import sqlalchemy as sql

from .base import Base


class Purpose(Base):
    __tablename__ = "purposes"

    id = sql.Column(sql.Integer, primary_key=True)
    purpose = sql.Column(sql.String(100), nullable=False)

    def __repr__(self) -> str:
        return f"<ID=(id={self.id}, purpose='{self.purpose}')>"
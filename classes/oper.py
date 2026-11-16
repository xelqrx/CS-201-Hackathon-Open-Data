import sqlalchemy as sql

from .base import Base


class Oper(Base):
    __tablename__ = "opers"

    id = sql.Column(sql.Integer, primary_key=True)
    oper_code = sql.Column(sql.Integer)
    oper_name = sql.Column(sql.String(100), nullable=False)

    def __repr__(self) -> str:
        return f"<ID=(id={self.id}, oper_name='{self.oper_name}', oper_code='{self.oper_code}' )>"
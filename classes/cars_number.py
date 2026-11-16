import sqlalchemy as sql

class Number:
    __tablename__ = "cars_numbers"

    id = sql.Column(sql.Integer, primary_key=True)
    number = sql.Column(sql.String(100), nullable=False)

    def __repr__(self) -> str:
        return f"<ID=(id={self.id}, number='{self.number}')>"
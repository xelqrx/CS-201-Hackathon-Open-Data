import sqlalchemy as sql

class Brand:
    __tablename__ = "brands"

    id = sql.Column(sql.Integer, primary_key=True)
    brand = sql.Column(sql.String(100), nullable=False)

    def __repr__(self) -> str:
        return f"<ID=(id={self.id}, brand='{self.brand}')>"
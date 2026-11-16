import sqlalchemy as sql

class Fuel:
    __tablename__ = "fuel"

    id = sql.Column(sql.Integer, primary_key=True)
    fuel = sql.Column(sql.String(100), nullable=False)

    def __repr__(self) -> str:
        return f"<ID=(id={self.id}, fuel='{self.fuel}')>"
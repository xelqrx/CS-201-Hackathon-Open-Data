import sqlalchemy as sql

class Kind:
    __tablename__ = "kinds"

    id = sql.Column(sql.Integer, primary_key=True)
    kind = sql.Column(sql.String(100), nullable=False)

    def __repr__(self) -> str:
        return f"<ID=(id={self.id}, kind='{self.kind}')>"
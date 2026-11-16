import sqlalchemy as sql

class Department:
    __tablename__ = "departments"

    id = sql.Column(sql.Integer, primary_key=True)
    dep_code = sql.Column(sql.Integer, primary_key=True)   
    dep = sql.Column(sql.String(100), nullable=False)

    def __repr__(self) -> str:
        return f"<ID=(id={self.id}, dep='{self.dep }', dep code='{self.dep_code}')>"
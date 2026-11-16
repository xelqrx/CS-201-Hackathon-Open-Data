import sqlalchemy as sql
from sqlalchemy.orm import relationship

from .base import Base
from .brand import Brand
from .body import Body
from .cars_number import Number
from .color import Color
from .department import Department
from .fuel import Fuel
from .kind import Kind
from .model import Model
from .oper import Oper
from .purpose import Purpose


class DataClean(Base):
    __tablename__ = "data_clean"

    id = sql.Column(sql.BigInteger, primary_key=True)
    person = sql.Column(sql.Text)
    oper_id = sql.Column(sql.Integer, sql.ForeignKey("opers.id"))
    d_reg = sql.Column(sql.Text)
    dep_id = sql.Column(sql.Integer, sql.ForeignKey("departments.id"))
    brand_id = sql.Column(sql.Integer, sql.ForeignKey("brands.id"))
    model_id = sql.Column(sql.Integer, sql.ForeignKey("models.id"))
    car_number_id = sql.Column(sql.Integer, sql.ForeignKey("cars_numbers.id"))
    vin = sql.Column(sql.Text)
    make_year = sql.Column(sql.Text)
    color_id = sql.Column(sql.Integer, sql.ForeignKey("colors.id"))
    kind_id = sql.Column(sql.Integer, sql.ForeignKey("kinds.id"))
    purpose_id = sql.Column(sql.Integer, sql.ForeignKey("purposes.id"))
    body_id = sql.Column(sql.Integer, sql.ForeignKey("bodies.id"))
    fuel_id = sql.Column(sql.Integer, sql.ForeignKey("fuel.id"))
    capacity = sql.Column(sql.Text)
    power_kwt = sql.Column(sql.Text)
    own_weight = sql.Column(sql.Text)
    total_weight = sql.Column(sql.Text)

    oper = relationship(Oper)
    department = relationship(Department)
    brand = relationship(Brand)
    model = relationship(Model)
    car_number = relationship(Number)
    color = relationship(Color)
    kind = relationship(Kind)
    purpose = relationship(Purpose)
    body = relationship(Body)
    fuel = relationship(Fuel)

import sqlalchemy

from db_session import SqlAlchemyBase


class Temp_hum_sens(SqlAlchemyBase):
    __tablename__ = 'temp_hum_sens'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    temp = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    hum = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    device_id = sqlalchemy.Column(sqlalchemy.Integer)
    time = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False)


class Hum_ground_sens(SqlAlchemyBase):
    __tablename__ = 'hum_ground_sens'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    hum = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    device_id = sqlalchemy.Column(sqlalchemy.Integer)
    time = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False)


class Statuses(SqlAlchemyBase):
    __tablename__ = 'statuses'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    status = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)


class Setttings(SqlAlchemyBase):
    __tablename__ = 'settings'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    value = sqlalchemy.Column(sqlalchemy.Float, nullable=False)


from sqlalchemy import Column, BigInteger, String, sql
from On_OFF_sensor_bot.utils.dp_api.dp_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users_bot'
    user_id = Column(BigInteger, primary_key=True)
    first_name = Column(String(200))
    last_name = Column(String(200))
    username = Column(String(50))
    status = Column(String(30))

    query: sql.select


from sqlalchemy import Column, Integer, Float, String
from app import db


"""
Tạo bảng trên mySQL 
"""
class ReadDataSensorTable(db.Model):
    id          = Column(Integer, primary_key= True, autoincrement= True, nullable= False)
    temp        = Column(Float, nullable= False)
    humi        = Column(Float, nullable= False)
    mq2         = Column(Float, nullable= False)
    createAt    = Column(String(50), nullable=False)
db.create_all()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: ChengXin
@contact:1921134176@qq.com
@version: 1.0.0
@license: Apache Licence
@file: models.py
@time: 2022/10/30 16:57
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import *
# import pymysql

app = Flask(__name__)
CORS(app, resources=r'/*', supports_credentials=True)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/test'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + "kgsql.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "jjjsks"

db = SQLAlchemy(app)  # 实例化的数据库


# 用户表
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)  # 主键
    username = db.Column(db.String(64), nullable=False)  # 用户名 nullable能否为空
    password = db.Column(db.String(20), nullable=False)  # 用户密码 可以为空


# 地球大数据科学工程平台数据表https://data.casearth.cn/
class Casearth(db.Model):
    __tablename__ = "casearth"
    id = db.Column(db.Integer, primary_key=True)  # 主键
    productSN = db.Column(db.String(20))  # 产品唯一标识，也可以用于查找icon
    title = db.Column(db.String(100), nullable=False)  # 产品名称
    iconPath = db.Column(db.String(100), nullable=False)  # 数据集图片路径https://data.casearth.cn + iconpath
    sdoId = db.Column(db.String(50), nullable=False)  # 跳转详情页数据接口https://data.casearth.cn/sdo/visitSdo?id= + sdoid + &userType=
    releaseDate = db.Column(db.String(10))  # 发布时间
    startTime = db.Column(db.String(10))  # 开始时间
    endTime = db.Column(db.String(10))  # 结束时间
    filesNumber = db.Column(db.Integer)  # 文件数量
    taxonomy = db.Column(db.String(30))  # 学科分类
    publishPhone = db.Column(db.String(20))  # 电话
    visitCount = db.Column(db.String(10))  # 访问量
    productType = db.Column(db.String(30))  # 产品类型
    publishDepartment = db.Column(db.String(30))  # 发布单位
    dataFormat = db.Column(db.String(20))  # 数据格式
    datatype = db.Column(db.String(20))  # 数据类型
    timeResolution = db.Column(db.String(10))  # 时间分辨率
    spatialResolution = db.Column(db.String(10))  # 空间分辨率
    keyword = db.Column(db.String(100))  # 关键词、标签
    tagStr = db.Column(db.String(100))  # 更广义的  关键词、标签
    publishEmail = db.Column(db.String(30))  # 邮箱
    publisher = db.Column(db.String(20))  # 数据作者
    downloadCount = db.Column(db.String(10))  # 下载数量
    desc = db.Column(db.String(1000))  # 描述
    # 必须进详情页才能获取的字段
    objectUrl = db.Column(db.String(100))  # 数据下载链接
    rangeDescription = db.Column(db.String(30))  # 数据范围
    mSize = db.Column(db.String(30))  # 数据大小
    shareMethod = db.Column(db.String(30))  # 共享方式

# 中国地名表

#
# # 学生表
# class Student(db.Model):
#     __tablename__ = "student"
#     id = db.Column(db.Integer, primary_key=True)  # 主键
#     name = db.Column(db.String(64), nullable=False)  # 学生姓名 nullable能否为空
#     gender = db.Column(db.Enum("男", "女"), nullable=False)  # 性别 Enum枚举 不能为空
#     phone = db.Column(db.String(11))  # 手机号 可以为空
#     grades = db.relationship("Grade", backref="student")  # 成绩关系关联
#     # courses = db.relationship("Course", secondary="student_to_course", backref="students")  # 关系关联
#
#
# # 中间表
# class StudenToCourse(db.Model):
#     __tablename__ = "student_to_course"
#     id = db.Column(db.Integer, primary_key=True)  # 主键
#     student_id = db.Column(db.Integer, db.ForeignKey("student.id"))  # 所属学生
#     course_id = db.Column(db.Integer, db.ForeignKey("course.id"))  # 所属课程
#
#
# # 课程表
# class Course(db.Model):
#     __tablename__ = "course"
#     id = db.Column(db.Integer, primary_key=True)  # 主键
#     name = db.Column(db.String(64), nullable=False)  # 课名
#     grades = db.relationship("Grade", backref="course")  # 成绩关系关联
#     teacher_id = db.Column(db.Integer, db.ForeignKey("teacher.id"))  # 所属教师
#     students = db.relationship("Student", secondary="student_to_course", backref="courses")  # 关系关联
#
#
# # 教师表
# class Teacher(db.Model):
#     __tablename__ = "teacher"
#     id = db.Column(db.Integer, primary_key=True)  # 主键
#     name = db.Column(db.String(64), nullable=False)  # 教师姓名 nullable能否为空
#     gender = db.Column(db.Enum("男", "女"), nullable=False)  # 性别 Enum枚举 不能为空
#     phone = db.Column(db.String(11))  # 手机号 可以为空
#     course = db.relationship("Course", backref="teacher")  # 课程关系关联
#
#
# # 成绩表
# class Grade(db.Model):
#     __tablename__ = "grade"
#     id = db.Column(db.Integer, primary_key=True)  # 主键
#     grade = db.Column(db.String(3), nullable=False)  # 成绩 nullable能否为空
#     student_id = db.Column(db.Integer, db.ForeignKey("student.id"))  # 所属学生
#     course_id = db.Column(db.Integer, db.ForeignKey("course.id"))  # 所属课程


if __name__ == '__main__':
    db.create_all()
    # db.drop_all()

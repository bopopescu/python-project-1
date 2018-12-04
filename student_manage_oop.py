import json

class Student(object):
    def __init__(self,name,age,wechat):
        self.__name = name
        self.__age = age
        self.__wechat = wechat


class StudentManager(object):
    __students = []
    def add_student(self,student):
        self.__students.append(student)

    def del_student(self,name):
        for item in self.__students :
            if item["name"] == name :
                self.__students.remove(item)

    def search_student(self,name):
        for item in self.__students :
            if item["name"] == name :
                return item






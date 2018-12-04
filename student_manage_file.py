import json

students = []

def load_students():
    with open("./data/student.json", "r") as f:
        student_json = f.read()

    global students
    students = json.loads(student_json)

def add_student():
    name = input("请输入学生姓名：")
    age = input("请输入学生年龄:")
    wechat = input("请输入学生微信:")
    student = {}
    student["name"] = name
    student["age"] = age
    student["wechat"] = wechat
    students.append(student)
    update_file_store()
    print_students()

def update_file_store() :
    # 写入文件
    student_json = json.dumps(students)
    with open("./data/student.json", "w") as f:
        f.write(student_json)

def del_student():
    name = input("请输入删除的姓名：")
    for student in students:
        if student["name"] == name :
            students.remove(student)
    update_file_store()
    print_students()

def search_student() :
    name = input("请输入查找的姓名：")
    for student in students :
        if student["name"] == name:
            print("\t"+student["name"]+"\t\t"+student["age"]+"\t\t"+student["wechat"])

def modify_student() :
    name = input("请输入要修改的学生姓名：")
    nname = input("请输入修改后的学生姓名：")
    nage = input("请输入修改后的学生年龄：")
    nwechat = input("请输入修改后的学生微信：")
    for student in students :
        if student["name"] == name :
            student["name"] = nname
            student["age"] = nage
            student["wechat"] = nwechat
    update_file_store()
    print_students()

def show_student() :
    print_students()


def show_opt():
    while True:
        print("\n")
        print("\t\t学生管理系统操作指令")
        print("~" * 50)
        print("\t1：添加|2：删除|3：查找|4：修改|5：显示|6：退出")
        print("~"*50)
        type = input("请输入指令：")
        if type == "1":
            add_student()
        elif type == "2":
            del_student()
        elif type == "3":
            search_student()
        elif type == "4":
            modify_student()
        elif type == "5":
            show_student()
        elif type == "6":
            break



def print_students():
    print("*"*50)
    print("\t姓名\t\t年龄\t\t微信")
    print("*" * 50)

    with open("./data/student.json", "r") as f:
        student_json = f.read()

    global students
    students = json.loads(student_json)
    for student in students :
        print("\t"+student["name"]+"\t\t"+student["age"]+"\t\t"+student["wechat"])
        print("*" * 50)

def main():
    load_students()
    show_opt()


main()

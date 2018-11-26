print("welcome to china")
'''模块用于定义一个学生类,此类用于
生成学生对象,来存储学生相关的信息'''
class Student:
    def __init__(self, n, a, s=0):
        self.name = n
        self.age = a
        self.score = s

    def get_info(self):
        '''此方法用来返回学生信息的元组'''
        return (self.name, self.age, self.score)

    def get_score(self):
        return self.score

    def get_age(self):
        return self.age

    def save(self, file):
        '''学生拿到文件后,自己来向文件里写东西'''
        file.write(self.name)
        file.write(',')
        file.write(str(self.age))
        file.write(',')
        file.write(str(self.score))
        file.write('\n')

def input_student():
    L = []  # 创建一个新的列表，用此列表准备保存学生信息
    # 录入学生信息
    while True:
        n = input("请输入姓名: ")
        if not n:
            break
        try:
            a = int(input("请输入年龄: "))
            s = int(input('请输入成绩: '))
        except:
            print("您的输入有错，请新输入...")
            continue
        L.append(Student(n, a, s))
    return L


def get_chinese_char_count(x):
    count = 0  # 先假设个数为0
    for ch in x:
        # 如果ch为中文字典,则count 做加一操作
        if ord(ch) > 127:
            count += 1
    return count


def output_student(L):
    print("+---------------+----------+----------+")
    print("|     name      |   age    |   score  |")
    print("+---------------+----------+----------+")
    for d in L:
        n, a, s = d.get_info()
        chinese_cnt = get_chinese_char_count(n)
        print('|%s|%s|%s|' % (n.center(15-chinese_cnt),
                              str(a).center(10),
                              str(s).center(10) ) )
    print("+---------------+----------+----------+")

def del_student(L):
    n = input('请输入要删除的学生的姓名: ')
    print("正在删除....", n)

def modify_student_score(L):
    print("正在修改学生成绩....")

def print_info_by_score_desc(L):
    def get_score(d):
        return d.get_score()
    L2 = sorted(L, key=get_score, reverse=True)
    output_student(L2)

def print_info_by_score_asc(L):
    def get_score(d):  # d是字典
        return d.get_score()
    L2 = sorted(L, key=get_score)
    output_student(L2)

def print_info_by_age_desc(L):
    L2 = sorted(L, key=lambda d: d.get_age(), reverse=True)
    output_student(L2)

def print_info_by_age_asc(L):
    L2 = sorted(L, key=lambda d: d.get_age())
    output_student(L2)

def save_to_file(L, filename='si.txt'):
    try:
        f = open(filename, 'w')
        for stu in L:
            # 第一,把学生的信息拿到当前来由'我'来往文件里写
            # f.write(stu.name)...
            stu.save(f)  # 第二,把文件 交给学生,由学来写
        f.close()
        print("保存成功")
    except OSError:
        print("写文件失败")

def read_from_file(filename='si.txt'):
    L = []
    try:
        f = open(filename)
        for line in f:
            n, a, s = line.strip().split(',')
            a = int(a)
            s = int(s)  # 转为整数
            L.append(Student(n, a, s))
        f.close()
    except OSError:
        print("读取文件失败")
    return L
# 此模块主要保存与菜单相关的函数
def show_menu():
    print("+---------------------------------+")
    print("| 1)  添加学生信息                |")
    print("| 2)  显示学生信息                |")
    print("| 3)  删除学生信息                |")
    print("| 4)  修改学生成绩                |")
    print("| 5)  按学生成绩高-低显示学生信息 |")
    print("| 6)  按学生成绩低-高显示学生信息 |")
    print("| 7)  按学生年龄高-低显示学生信息 |")
    print("| 8)  按学生年龄低-高显示学生信息 |")
    print("| 9)  保存信息到文件(si.txt)   |")
    print("| 10) 从文件中读取数据(si.txt) |")
    print("| q)  退出                        |")
    print("+---------------------------------+")
# 学生信息管理系统的主模块
def main():
    L = []
    while True:
        show_menu()
        s = input("请选择: ")
        if s == 'q':
            break
        elif s == '1':
            L += input_student()
        elif s == '2':
            output_student(L)
        elif s == '3':
            del_student(L)
        elif s == '4':
            modify_student_score(L)
        elif s == '5':
            print_info_by_score_desc(L)
        elif s == '6':
            print_info_by_score_asc(L)
        elif s == '7':
            print_info_by_age_desc(L)
        elif s == '8':
            print_info_by_age_asc(L)
        elif s == '9':
            save_to_file(L)
        elif s == '10':
            L = read_from_file()


if __name__ == '__main__':
    main()
# @Time: 2024/10/7 
# @Author: Qi Wang
# @File: 继承类练习_人力系统
# @Project: Python-leran-in-total
# @Quelle: https://www.bilibili.com/video/BV1ZW4y127Vp/?spm_id_from=333.999.0.0&vd_source=edaa7c180a2e4b42b2b256823b55fcbf


class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id


    def print_info(self):
        print(f"Employee name: {self.name}, Employee ID: {self.id}")


class FullTimeEmployee(Employee):
    def __init__(self, name, id, monthly_salary):
        # 这里用super表示父类
        super().__init__(name, id)
        # 全职员工的月薪属性
        self.monthly_salary = monthly_salary


    def calculate_monthly_pay(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, id, daily_salary, work_days):
        super().__init__(name, id)
        self.daily_salary = daily_salary
        self.work_days = work_days


    def calculate_monthly_pay(self):
        return self.daily_salary * self.work_days



Jack = FullTimeEmployee('Jack', 'FBI7368', 9000)
Rose = PartTimeEmployee('Rose', 'FBI8788', 200, 19)
Jack.print_info()
print(Jack.calculate_monthly_pay())

Rose.print_info()
print(Rose.calculate_monthly_pay())
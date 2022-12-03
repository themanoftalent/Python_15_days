#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#


from abc import ABCMeta, abstractmethod

class Employee(metaclass=ABCMeta):
    def __init__(self, name, salary=0.0):
        self.name = name
        self.salary = salary

    def give_raise(self, percent):
        self.salary = self.salary + (self.salary * percent)

    @abstractmethod
    def work(self):
        pass

    def __repr__(self):
        return f"<Employee: name={self.name}, salary={self.salary}>"

    def __str__(self):
        return f"Employee: name={self.name}, salary={self.salary}"

    def __eq__(self, other):
        return self.name == other.name and self.salary == other.salary


class Manager(Employee):
    def __init__(self, name, salary=0.0, project=None):
        super().__init__(name, salary)
        self.project = project

    def work(self):
        return f"{self.name} manages {self.project}"

    def __repr__(self):
        return f"<Manager: name={self.name}, salary={self.salary}, project={self.project}>"

    def __str__(self):
        return f"Manager: name={self.name}, salary={self.salary}, project={self.project}"

    def __eq__(self, other):
        return self.name == other.name and self.salary == other.salary and self.project == other.project


class Secretary(Employee):
    def work(self):
        return f"{self.name} takes dictations"

    def __repr__(self):
        return f"<Secretary: name={self.name}, salary={self.salary}>"

    def __str__(self):
        return f"Secretary: name={self.name}, salary={self.salary}"

    def __eq__(self, other):
        return self.name == other.name and self.salary == other.salary


class SalesPerson(Employee):
    def __init__(self, name, salary=0.0, quota=0):
        super().__init__(name, salary)
        self.quota = quota

    def work(self):
        return f"{self.name} expends {self.quota} hours on phone"

    def __repr__(self):
        return f"<SalesPerson: name={self.name}, salary={self.salary}, quota={self.quota}>"

    def __str__(self):
        return f"SalesPerson: name={self.name}, salary={self.salary}, quota={self.quota}"

    def __eq__(self, other):
        return self.name == other.name and self.salary == other.salary and self.quota == other.quota


class Factory:
    def create(self, kind, *args, **kwargs):
        return eval(kind)(*args, **kwargs)


if __name__ == "__main__":
    factory = Factory()
    employees = [
        factory.create("Manager", "Akif", 5000, "Project1"),
        factory.create("Secretary", "Hulya", 1500),
        factory.create("SalesPerson", "Cemil", 2000, 250),
    ]
    for employee in employees:
        print(employee.work())
        print(employee)
        print()



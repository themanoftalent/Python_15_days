#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

def main():
    student = {'name': 'Akif', 'age': 25, 'courses': ['Math', 'CompSci']}
    print(student)
    print(student['name'])
    print(student['courses'])
    print(student.get('name'))
    print(student.get('phone', 'Not Found'))
    student['phone'] = '555-5555'
    student['name'] = 'John'
    print(student.get('phone', 'Not Found'))
    print(student.get('name'))
    student.update({'name': 'Akif', 'age': 26, 'phone': '555-5555'})
    print(student)
    del student['age']
    age = student.pop('age')
    print(student)
    print(len(student))
    print(student.keys())
    print(student.values())
    print(student.items())


if __name__ == '__main__':
    main()

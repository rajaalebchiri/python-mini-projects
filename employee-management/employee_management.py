#!/usr/bin/env python

"""
Employee management system

- check employee {id} for checking if employee with id {id} exists
    cmd: ./employee_managment.py check_employee 85234

"""
import sys
import argparse

from sqlalchemy import create_engine, Column, Integer, String, select, update
from sqlalchemy.orm import sessionmaker, declarative_base

from tabulate import tabulate

engine = create_engine('sqlite:///employees.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Employee(Base):
    """Employee Table Class Based on sqlalchemy Base class"""
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    post = Column(String)
    salary = Column(Integer)

def display_employee(employee: Employee):
    print(f"Employee Name: {employee.name}, Post: {employee.post}, Salary: {employee.salary}")


class EmployeeConfig():
    """Employee Config Class"""
    def __init__(self, name, post, salary):
        self.name = name
        self.post = post
        self.salary = salary

    def update_name(self, name):
        self.name = name

    def update_post(self, post):
        self.post = post

    def update_salary(self, salary):
        self.salary = salary

Base.metadata.create_all(engine)
session = Session()

def check_employee(query: str) -> dict:
    """Check if employee exists By Name"""
    try:
        employee_exists = session.query(
            Employee).filter_by(name=query).exists()
        if session.query(employee_exists).scalar():
            print("Employee exists!")
        else:
            print("Employee doesn't exist!")
    except ValueError as value_error:
        raise ValueError("Something went wrong") from value_error

def display_employees(employees):
    """Display the list of employees in table format"""
    print(tabulate(employees, headers='firstrow', tablefmt='fancy_grid'))

def update_employee_name(id: int, name: str):
    employee = session.query(Employee).filter_by(id=id).one_or_none()
    if employee is None:
        return "Employee not found"
    else:
        employee.name = name
        session.commit()
        return(display_employee(employee))

def update_employee_post(id: int, post: str):
    employee = session.query(Employee).filter_by(id=id).one_or_none()
    if employee is None:
        return "Employee not found"
    else:
        employee.post = post
        session.commit()
        return(display_employee(employee))

def update_employee_salary(id: int, salary: int):
    employee = session.query(Employee).filter_by(id=id).one_or_none()
    if employee is None:
        return "Employee not found"
    else:
        employee.salary = salary
        session.commit()
        return(display_employee(employee))

def get_employees():
    """Get Employees"""
    formatted_employees = [["ID", "Full Name", "Post", "Salary"]]
    employees = session.query(Employee).all()
    for employee in employees:
        formatted_employees.append(
            [employee.id, employee.name, employee.post, employee.salary])
    return display_employees(formatted_employees)

def add_employee(employee: EmployeeConfig) -> dict:
    """Add new employee"""
    try:
        employee_query = (
            session.query(Employee)
            .filter_by(
                name=employee.name
            )
            .one_or_none()
        )
        if employee_query is not None:
            return f"Employee with name {employee.name} already exists"
        new_employee = Employee(
            name=employee.name, post=employee.post, salary=employee.salary)
        session.add(new_employee)
        session.commit()
        return print("Employee Added Successfully")
    except BaseException as base_exception:
        raise ValueError("Something went wrong") from base_exception

def update_employee(args: argparse.Namespace):
    if args.name is not None:
        update_employee_name(args.id, args.name)
    if args.post is not None:
        update_employee_post(args.id, args.post)
    if args.salary is not None:
        update_employee_salary(args.id, args.salary)

def delete_employee(id: int):
    employee = session.query(Employee).filter_by(id=id).one_or_none()
    if employee is None:
        return print("Employee Not Found")
    else:
        session.delete(employee)
        session.commit()
        return print("Employee Deleted successfully")

def process_args(args: argparse.Namespace):
    match args.subparser_name:
        case "add_employee":
            new_employee = EmployeeConfig(name=args.name, post=args.post, salary=args.salary)
            add_employee(employee=new_employee)
        case "display_employees":
            get_employees()
        case "check_employee":
            check_employee(query= args.name)
        case "edit_employee":
            update_employee(args)
        case "delete_employee":
            delete_employee(id= args.id)

if __name__ == "__main__":
    global_parser = argparse.ArgumentParser(
        prog="employee_management",
        description="Employee management system",
	    epilog=f"Thanks for using our system!",
    )
    subparsers = global_parser.add_subparsers(title="subcommands", help="Employee Management Actions", dest="subparser_name")
    
    # add new employee parser
    add_parser = subparsers.add_parser("add_employee", help="Add new employee")
    add_parser.add_argument("--name", type=str, help="name of the new employee")
    add_parser.add_argument("--post", type=str, help="post of the new employee")
    add_parser.add_argument("--salary", type=int, help="salary of the new employee")
    
    # list all employees parser
    display_parser = subparsers.add_parser("display_employees", help="Display all employees")
    
    # check if employee exists
    check_parser = subparsers.add_parser("check_employee", help="Check if employee exists")
    check_parser.add_argument("--name", type= str, help="name of the employee", required=True)
    
    # edit employee
    edit_parser = subparsers.add_parser("edit_employee", help="Edit employee")
    edit_parser.add_argument("--id", type=int, help="id of the employee", required=True)
    edit_parser.add_argument("--name", type=str, help="name of the employee")
    edit_parser.add_argument("--post", type=str, help="post of the employee")
    edit_parser.add_argument("--salary", type=str, help="salary of the employee")
    
    # delete employee
    delete_parser = subparsers.add_parser("delete_employee", help="Delete employee")
    delete_parser.add_argument("--id", type=int, help="id of the employee", required=True)
    
    # Parsing
    args = global_parser.parse_args(args=None if sys.argv[1:] else ['--help'])
    process_args(args)
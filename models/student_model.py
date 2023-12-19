from pydantic import BaseModel


class Student(BaseModel):
    id: int
    student_id_number: str
    first_name: str
    last_name: str


def create_samples():
    return [
        Student(id=1, student_id_number='11222', first_name='John', last_name='Doe'),
        Student(id=2, student_id_number='33444', first_name='Jane', last_name='Doe'),
        Student(id=3, student_id_number='55666', first_name='Jack', last_name='Doe'),
    ]
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str
    age: Optional[int] = None
    # email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default = 5, description="A decimal value representating the cgpa of the student")

# new_student = {"name": 32} ## wrong
new_student = {"name": "nitish", "age": "32", "cgpa": 5}

student =  Student(**new_student)

print(student)
print(type(student))
print(student.name)


student_dict = dict(student)
print(student_dict["age"])
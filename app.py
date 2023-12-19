from flask import render_template, request, redirect, url_for
from config import db, app

from models import Student


@app.route('/')
def index():    
    students = Student.query.all()
    return render_template('students_table.html', students=students)


@app.get('/create')
def student_create_form():
    return render_template('student_create_form.html')


@app.get('/update/<int:id>')
def student_update_form(id: int):
    student = Student.query.get(id)
    if student:
        return render_template('student_update_form.html', student=student)
    
    return 'Student not found', 404


@app.post('/create')
def create_student():
    student = Student(
        student_id_number=request.form['student_id_number'],
        first_name=request.form['first_name'],
        last_name=request.form['last_name'],
    )
    db.session.add(student)
    db.session.commit()
    return redirect(url_for('index'))


@app.post('/update/<int:id>')
def update_student(id: int):
    student = Student.query.get(id)
    if student:        
        student.student_id_number = request.form['student_id_number']
        student.first_name = request.form['first_name']
        student.last_name = request.form['last_name']
        db.session.merge(student)
        db.session.commit()
        return redirect(url_for('index'))      
      
    return 'Student not found', 404


@app.post('/delete/<int:id>')
def delete_student(id: int):
    student = Student.query.get(id)
    if student:
        db.session.delete(student)
        db.session.commit()
        return redirect(url_for('index'))
        
    return 'Student not found', 404
    

if __name__ == '__main__':
    app.run(debug=True)

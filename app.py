from flask import Flask, render_template, request, redirect, url_for
from models.student_model import Student, create_samples


app = Flask(__name__)

# sample data
students = create_samples()


@app.route('/')
def index():
    return render_template('students_table.html', students=students)


@app.get('/create')
def student_create_form():
    return render_template('student_create_form.html')


@app.get('/update/<int:id>')
def student_update_form(id: int):
    if student := next((s for s in students if s.id == id), None):        
        return render_template('student_update_form.html', student=student)
    
    return 'Student not found', 404


@app.post('/create')
def create_student():
    student = Student(
        id=len(students) + 1,
        student_id_number=request.form['student_id_number'],
        first_name=request.form['first_name'],
        last_name=request.form['last_name'],
    )
    students.append(student)
    return redirect(url_for('index'))


@app.post('/update/<int:id>')
def update_student(id: int):
    if student := next((s for s in students if s.id == id), None):        
        student.student_id_number = request.form['student_id_number']
        student.first_name = request.form['first_name']
        student.last_name = request.form['last_name']
        return redirect(url_for('index'))      
      
    return 'Student not found', 404


@app.post('/delete/<int:id>')
def delete_student(id: int):
    if student := next((s for s in students if s.id == id), None):
        students.remove(student)
        return redirect(url_for('index'))
        
    return 'Student not found', 404
    

if __name__ == '__main__':
    app.run(debug=True)

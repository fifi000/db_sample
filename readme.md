# Python Sample Web + DB App

## Technologies

  - **Flask** - web microframework 
  - **SQLAlchemy** - ORM (Object Relational Mapper)
  - **SQLite** - local database
  - **Jinja Template** - HTML template engine

## Database Schema

```sql
Student Table:
    id: INTEGER 
    student_id_number: VARCHAR
    first_name: VARCHAR
    last_name: VARCHAR
```
 
## Create and activate virtual env
 
```powershell
python -m venv ./.venv;
.\.venv\Scripts\Activate.ps1
```

## Requirements

```powershell
pip install -r ./requirements.txt
```

## Run

```powershell
flask run
```
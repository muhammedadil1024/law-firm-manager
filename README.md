# Law Firm Manager

![Django](https://img.shields.io/badge/Django-4.1-green) ![Python](https://img.shields.io/badge/Python-3.9-blue)

![Demo App](/static/demo-lawfirm.png)

## 🧐 About the Project

**Law Firm Manager** is a web-based application built with Python - Django, utilizing PostgreSQL for the database and a frontend developed with HTML, CSS, and JavaScript. It streamlines the management of client information, case tracking, etc.. for law firms.

---

## ✨ Features

- *Adding Clients*: User can Add or Create Clients and their detail on `Clients` Page. Options for Edit and Delete the User information when they want
- *Managing Lawyers Information List*: User can Add, Edit and Delete Lawyers Information on `Lawyers` Page.
- *Handling Case details and Status*: User can Add or Create a Case details with the details of Listed Clients and appropriate Lawyers on `Cases` Page and they can Edit or Update the Status of Case. Like others User can Delete data when they want.

---

## 🛠️ Tech Stack

- **Framework:** Django
- **Language:** Python
- **Database:** PostgreSQL
- **Frontend:** HTML/CSS/JAVASCRIPT

---

## ⚙️ Setup Instructions

### Prerequisites
- Python 3.9 or above
- Django 4.1.2
- PostgreSQL
- A virtual environment (recommended)

### Installation Steps

* Clone the repository
```bash
git clone https://github.com/muhammedadil1024/law-firm-manager.git
```

* Navigate to the project directory
```bash
cd law-firm-manager
```

* Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

* Install dependencies
```bash
pip install -r requirements.txt
```

* Set up the database -  PostgreSQL
  * Create new database fort the project
  * create .env file and add your secret key and database details
  
```bash
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_NAME=your_database_name
DATABASE_USER=your_username
DATABASE_PASSWORD=your_database_password
DATABASE_HOST=localhost
DATABASE_PORT=5432
``` 

* Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

* Run the development server
```bash
python manage.py runserver
```

## 📞 Contact

- **Email:** [muhammedadilpv292@gmail.com](mailto:muhammedadilpv292@gmail.com)
- **GitHub:** [Muhammed Adil](https://github.com/muhammedadil1024)
- **LinkedIn:** [Muhammed Adil](https://www.linkedin.com/in/mhd-adil292/)

Thank You!


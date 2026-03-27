# 🤑 Loan Manager (Django)

A simple and intuitive loan tracking web application built with Django.
It allows users to create loans, record repayments, and track progress visually.

---

## Features

* Create and manage loans between two people
* Track repayments over time
* Automatically calculate:

  * Total repaid
  * Remaining balance
* Prevent overpayment with validation
* Visual progress bar for repayment status
* Delete repayments and loans
* Clean and responsive UI (Bootstrap)

---

## Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, Bootstrap
* **Database:** SQLite
* **Version Control:** Git & GitHub

---

## 📸 Screenshots

### Home Page
![Home Page](screenshots/Screenshot%202026-03-27%20at%2021.00.16.png)

### Loan List

![Loan List](screenshots/Screenshot%202026-03-27%20at%2021.32.30.png)

### Loan Detail

![Loan Detail](screenshots/Screenshot%202026-03-27%20at%2021.33.06.png)

---

## ⚙️ Installation & Setup

1. Clone the repository:

```bash
git clone https://github.com/markmaritoi/loan-manager-django.git
cd loan-manager-django
```

2. Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Run the server:

```bash
python manage.py runserver
```

6. Open in browser:

```
http://127.0.0.1:8000/
```

---

## Key Learning Points

* Django models and relationships (ForeignKey)
* Form handling and validation
* Preventing invalid data (e.g. overpayments)
* Dynamic templates with Django Template Language
* CRUD operations (Create, Read, Update, Delete)

---

## Future Improvements

* User authentication (login/signup)
* Multi-user loan tracking
* Better UI styling (custom CSS)
* Charts for repayment analytics
* Deployment (Render / Railway)
# 🍰 Dessert Shop – Django Basics Final Project

A fully functional and visually polished web application built as part of the **Django Basics Course @ SoftUni**.  
The project demonstrates Django fundamentals including models, forms, views, templates, CRUD operations, PostgreSQL integration, and clean project structure.

---

## 📌 Project Overview

The **Dessert Shop** application allows users to browse desserts, categories, and orders.  
Administrators can manage desserts, categories, orders, and order items through full CRUD functionality.

The project follows Django best practices and includes:

- Modular architecture with 3 separate Django apps  
- PostgreSQL database  
- Dynamic templates with Bootstrap styling  
- Custom template filter  
- Custom 404 page  
- Form validation, custom error messages, and read‑only fields  
- Delete confirmation pages  
- Navigation across all pages  
- Clean, readable code  

---

## 🧩 Features

### ✔ Desserts
- List all desserts  
- View dessert details  
- Create, edit, delete desserts  
- Assign categories and ingredients  
- Upload dessert images  

### ✔ Categories
- List categories  
- View category details  
- Create, edit, delete categories  

### ✔ Orders
- Create customer orders  
- Add, edit, delete order items  
- Automatic total price calculation  
- Read‑only fields in forms  
- Validation and custom error messages  

### ✔ Additional Features
- Custom template filter (`euro`) for formatting prices  
- Custom 404 error page  
- Responsive design using Bootstrap  
- Template inheritance and reusable components  

---

## 🛠 Technologies Used

- **Python 3.9**
- **Django 4.2**
- **PostgreSQL**
- **Bootstrap 5**
- **HTML5 / CSS3**
- **Pillow** (for image uploads)

---

## 🗄 Database Setup (PostgreSQL)

Before running the project, create a PostgreSQL database:

```sql
CREATE DATABASE final_project_db;




🚀 Installation & Running the Project
1. Clone the repository
git clone <your-repo-url>
cd Django-Basics-Final-Project


2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


3. Install dependencies
pip install -r requirements.txt


4. Apply migrations
python manage.py migrate


5. Run the development server
python manage.py runserver


Open the app at:
http://127.0.0.1:8000/ (127.0.0.1 in Bing)

📁 Project Structure
Django-Basics-Final-Project/
│
├── core/               # Home page and shared logic
├── desserts/           # Desserts, categories, ingredients
├── orders/             # Orders and order items
│
├── templates/          # All HTML templates
│   ├── desserts/
│   ├── categories/
│   ├── orders/
│   ├── base.html
│   ├── home.html
│   └── 404.html
│
├── static/
│   └── css/styles.css  # Custom styling
│
├── requirements.txt
├── manage.py
└── README.md



🧪 Custom Template Filter
Located in desserts/templatetags/dessert_filters.py:
@register.filter
def euro(value):
    return f"{float(value):.2f} €"


Usage:
{{ dessert.price|euro }}



⚠ Notes for the Examiner
- Authentication is intentionally excluded as required by the assignment.
- The project uses PostgreSQL as specified.
- All CRUD operations include confirmation pages.
- Forms include custom validation, error messages, placeholders, and a read‑only field.
- The project contains more than 10 templates, with more than 7 dynamic pages.
- A custom 404 page is implemented.
- A custom template filter is implemented.
- Navigation is consistent across all pages.
- The project follows Django best practices and clean code principles.

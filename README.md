# Inventory Management System

**Student Name:** Aqeel Ahmed  
**Roll Number:** PWM-331198  
**Course:** Python Web Mastery (Saylani Welfare)  
**Project:** Inventory Management System with Django & REST API

## 🔗 GitHub Repository
[GitHub Link](https://github.com/AqeelAhmed1308/inventory-management-system)

## 📋 Project Summary
This is a Django-based Inventory Management System developed as a final project. It includes models and REST APIs for:
- Store
- Category
- Product
- Staff
- Manager

## 🧪 APIs (use in Postman)

Base URL: `http://127.0.0.1:8000/`

| Method | Endpoint               | Description           |
|--------|------------------------|-----------------------|
| GET    | `/stores/`             | List all stores       |
| POST   | `/stores/`             | Create new store      |
| GET    | `/stores/<id>/`        | Retrieve one store    |
| PUT    | `/stores/<id>/`        | Update a store        |
| DELETE | `/stores/<id>/`        | Delete a store        |
| ...    | Same for categories, products, staff, and managers |

## 🛠️ Setup Instructions
1. Open terminal and navigate to the project folder.
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate

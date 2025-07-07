# 🚨 Missing Resource Identifier – Disaster Relief Web App

This is a simple and powerful web application that allows users to **report and track missing essential resources** like food, water, medicine, and shelter during disaster situations. Built using **Python Flask** and **MySQL**, this app is designed to support relief teams like NGOs, government officials, and volunteers to collect real-time shortage data in affected areas.

---

### 🛠️ Features

- 📋 Submit missing resource details using a clean HTML form
- ✅ Validations using Flask flash messages
- 📊 View submitted resource records in a responsive Bootstrap table
- 🔍 Track info like category, quantity, location, date, and contact
- 🧠 Organized folder structure using Jinja2 templates and modular files

---

### 🧰 Technologies Used

- **Frontend**: HTML5, Bootstrap 5, Jinja2
- **Backend**: Python Flask
- **Database**: MySQL

---

### 📁 Project Structure

```
project/
├── app.py
├── db_config/
│   └── db_connect.py
├── templates/
│   ├── base.html
│   ├── index.html
│   └── resources.html
```

---

### ⚙️ How to Run This Project Locally

1. Clone this repository:
   ```
   git clone https://github.com/tanujasharma000/Missing-Resource-Identifier.git
   ```

2. Navigate into the project folder:
   ```
   cd Missing-Resource-Identifier
   ```

3. Install required libraries:
   ```
   pip install Flask mysql-connector-python
   ```

4. Make sure your MySQL server is running and a database named `disaster_resources` is created.  
   You also need a table named `resources` with appropriate columns (like name, category, quantity, location, date, etc.)

5. Update the credentials in `db_config/db_connect.py` file if needed.

6. Run the Flask app:
   ```
   python app.py
   ```

7. Open your browser and go to:
   ```
   http://localhost:5000
   ```

---


### 📦 Requirements

This app uses the following Python libraries:

- Flask
- mysql-connector-python

You can install them using:

```
pip install Flask mysql-connector-python
```

---

### 📝 Developer Note

This is a student-level backend + database project built with a focus on functionality and real-world disaster support scenarios. It can be extended to include login systems, report downloads, map integration, and analytics in the future.

---

### Developed by Tanuja Sharma

> *“Because even a missing packet of food can make a difference in a disaster zone.”*

---

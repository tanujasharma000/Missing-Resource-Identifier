from flask import Flask, render_template, request, redirect, url_for , flash
from datetime import datetime
from db_config.db_connect import get_connection


app= Flask(__name__)
import os
from dotenv import load_dotenv
load_dotenv()

app.secret_key = os.getenv("SECRET_KEY")

@app.route('/',methods=["GET" , "POST"])
def index():
    if request.method=="POST":
        name=request.form.get("name","").strip()
        quantity = request.form.get("quantity", "").strip()
        unit = request.form.get("unit", "").strip()
        location = request.form.get("location", "").strip()
        category = request.form.get("category", "").strip()
        date = request.form.get("date", "").strip() or datetime.now().strftime("%Y-%m-%d")
        submission_time = datetime.now()
        reported_by = request.form.get("reported_by", "").strip()
        contact = request.form.get("contact", "").strip()
        notes = request.form.get("notes", "").strip()
        if not name or not quantity or not location or not category or not contact:
            flash("Name, Category, Contact, Location, and Quantity are required!","danger")
            return render_template("index.html")
        try:
            quantity=int(quantity)
            if quantity<=0:
                flash("Quantity must be a positive number!","danger")
                return render_template("index.html")
        except ValueError:
            flash("Quantity must be a number!","danger")
            return render_template("index.html")
        try:
            conn=get_connection()
            cursor=conn.cursor()

            insert_query = """
                INSERT INTO resources 
                (name, category, quantity, unit, location, date, submission_time, reported_by, contact, notes) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values= (name, category, quantity, unit, location, date, submission_time, reported_by, contact, notes)
            cursor.execute(insert_query,values)
            conn.commit()
            cursor.close()
            conn.close()

            flash("Form submitted successfully!", "success")
            return redirect(url_for("show_resources"))
        except Exception as e:
            print("Error while saving:", e)
            flash("Something went wrong while submitting the form.", "danger")
            

    return render_template('index.html')

@app.route("/resources")
def show_resources():
    
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM resources ORDER BY submission_time DESC")
        data=cursor.fetchall()
        print("Fetched Data:", data)
        cursor.close()
        conn.close()
        return render_template("resources.html",data=data)
    except Exception as e:
        print("Error fetching resources:", e)
        flash("Could not fetch resources", "danger")
        data = []

    return render_template("resources.html", data=data)


if __name__=='__main__':
    app.run(debug=True)

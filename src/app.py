from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3

# Initialize the Flask app
app = Flask(__name__, template_folder='../templates', static_folder='../static')

def connect_db():
    """Connect to SQLite database."""
    #change the File path accordingly 
    db_path = r"C:\Users\Acer\PycharmProjects\incident_response_system\user_performance.db"
    return sqlite3.connect(db_path)

# Initialize the database table
def initialize_database():
    conn = connect_db()
    cursor = conn.cursor()
    # Create the table if it does not exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_performance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname TEXT,
        age INTEGER,
        gender TEXT,
        time_A REAL,
        time_B REAL,
        errors_A INTEGER,
        errors_B INTEGER
    );
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def startup():
    """Redirect to the startup page as the default landing page."""
    return render_template('startup.html')

@app.route('/task', methods=['GET', 'POST'])
def task():
    if request.method == 'POST':
        try:
            fullname = request.form.get('fullname')
            age = request.form.get('age')
            gender = request.form.get('gender')

            print(f"Fullname: {fullname}, Age: {age}, Gender: {gender}")

            # Save user details to the database
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO user_performance (fullname, age, gender) VALUES (?, ?, ?)',
                (fullname, age, gender)
            )
            conn.commit()
            conn.close()

            print("User details saved successfully.")
            return redirect('/task')

        except Exception as e:
            print(f"Error details: {e}")
            return "An error occurred while saving user details.", 500

    return render_template('task.html')

@app.route('/prototype-a', methods=['GET', 'POST'])
def prototype_a():
    if request.method == 'POST':
        try:
            time_A = request.form.get('time_A')
            errors_A = request.form.get('errors_A')

            # Save the data to the database
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE user_performance
                SET time_A = ?, errors_A = ?
                WHERE id = (SELECT MAX(id) FROM user_performance)
            ''', (time_A, errors_A))
            conn.commit()
            conn.close()

            print(f"Prototype A Data Saved: Time - {time_A}, Errors - {errors_A}")
            return redirect('/task')

        except Exception as e:
            print(f"Error in Prototype A POST request: {e}")
            return "An error occurred while processing Prototype A.", 500

    return render_template('prototype_a.html')

@app.route('/prototype-b', methods=['GET', 'POST'])
def prototype_b():
    if request.method == 'GET':
        return render_template('prototype_b.html')

    if request.method == 'POST':
        try:
            # Collect the data from the POST request
            data = request.get_json()
            time_B = float(data.get('time_B', 0))
            errors_B = int(data.get('errors_B', 0))

            # Save the data to the database
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE user_performance
                SET time_B = ?, errors_B = ?
                WHERE id = (SELECT MAX(id) FROM user_performance)
            ''', (time_B, errors_B))
            conn.commit()
            conn.close()

            print(f"Prototype B Data Saved: Time - {time_B}, Errors - {errors_B}")
            return jsonify({"message": "Data saved successfully!"}), 200

        except Exception as e:
            print(f"Error: {e}")
            return jsonify({"message": "An error occurred while saving data."}), 500

@app.route('/questionnaire')
def questionnaire():
    """
    Render the questionnaire instructions page.
    Redirects to the question.html file.
    """
    return render_template('question.html')

if __name__ == '__main__':
    print("Starting Flask app...")
    initialize_database()  # Ensure the database is initialized before starting
    app.run(debug=True)

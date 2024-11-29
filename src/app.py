from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Root URL
@app.route('/')
def home():
    # Redirect to Prototype A as the default page
    return redirect(url_for('prototype_a'))

# Route for Prototype A
@app.route('/prototype-a', methods=['GET', 'POST'])
def prototype_a():
    if request.method == 'POST':
        try:
            # Collect form data from Prototype A
            data = {
                'incident_type': request.form.get('incident-type'),
                'name': request.form.get('name'),
                'email': request.form.get('email'),
                'department': request.form.get('department'),
                'evidence': request.files.get('evidence'),  # For file uploads
                'device_type': request.form.get('device-type'),
                'suspected_source': request.form.get('suspected-source'),
                'severity': request.form.get('severity'),
                'incident_time': request.form.get('incident-time'),
                'additional_notes': request.form.get('additional-notes'),
            }

            # Debugging: Log form data
            print("Prototype A - Form Data Received:", data)

            # Redirect to the success page after form submission
            return redirect(url_for('success'))
        except Exception as e:
            print("Error in Prototype A:", e)
            return "An error occurred while processing Prototype A.", 500

    # Render the Prototype A template
    return render_template('prototype_a.html')

# Route for Success Page
@app.route('/success')
def success():
    try:
        # Debugging: Log success page access
        print("Success page accessed.")
        return render_template('success.html')  # Display success message and button
    except Exception as e:
        print("Error in Success Page:", e)
        return "An error occurred while rendering the success page.", 500

# Route for Prototype B
@app.route('/prototype-b', methods=['GET', 'POST'])
def prototype_b():
    if request.method == 'POST':
        try:
            # Collect JSON data from Prototype B
            data = request.json
            # Debugging: Log form data
            print("Prototype B - Data Received:", data)
            return jsonify({"message": "Responses submitted successfully!"}), 200
        except Exception as e:
            print("Error in Prototype B POST request:", e)
            return jsonify({"message": "An error occurred while processing Prototype B."}), 500

    try:
        # Render the Prototype B template
        print("Rendering Prototype B widget.")
        return render_template('prototype_b.html')
    except Exception as e:
        print("Error in Prototype B GET request:", e)
        return "An error occurred while rendering Prototype B.", 500

# API route for Prototype B responses
@app.route('/submit_responses', methods=['POST'])
def submit_responses():
    try:
        # Collect JSON data from Prototype B
        data = request.get_json()
        # Debugging: Log responses
        print("Prototype B - Responses Received:", data)
        # Simulate saving the responses (e.g., to a database)
        return jsonify({"message": "Responses submitted successfully!"}), 200
    except Exception as e:
        print("Error in /submit_responses API:", e)
        return jsonify({"message": "An error occurred while submitting responses."}), 500

# Main Entry Point
if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(debug=True)

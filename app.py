from flask import Flask, request, jsonify
from dbconn import create_connection
from datetime import datetime
from flask_cors import CORS
import uuid


app = Flask(__name__)

# Enable CORS for all routes
CORS(app, origins="http://localhost:8033")

@app.route('/')
def hello_world():
    return 'Hello, World!'

from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/insert_test_result', methods=['GET'])  # Change the method to GET
def insert_test_result():
    print("Received data")

    # Get the data from the GET request query parameters
    test_id = str(uuid.uuid4())
    test_case = request.args.get('test_case')
    path = request.args.get('path')
    test_suite = request.args.get('test_suite')
    profile = request.args.get('profile')
    os = request.args.get('os')
    os_version = request.args.get('os_version')
    browser = request.args.get('browser')
    browser_version = request.args.get('browser_version')
    status = request.args.get('status')
    error_message = request.args.get('error_message')
    duration = request.args.get('duration')

    start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Create a database connection
    print("Connecting to DB")
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            insert_query = """
            INSERT INTO TestResults (TestResultId, TestCase, Path, TestSuite, Profile, OS, OSVersion, Browser, BrowserVersion, Status, ErrorMessage, StartTime, EndTime, Duration)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            # Prepare the data tuple
            test_data = (test_id, test_case, path, test_suite, profile, os, os_version, browser, browser_version, status, error_message, start_time, end_time, duration)
            print("Saving to DB")
            cursor.execute(insert_query, test_data)
            connection.commit()
            print("Successful")
            return jsonify({"status": "success", "message": "Test result inserted successfully"}), 200
        except Exception as e:
            print("Error: " + str(e))
            return jsonify({"status": "error", "message": str(e)}), 500
        finally:
            cursor.close()
            connection.close()
    else:
        print("Database connection failed")
        return jsonify({"status": "error", "message": "Database connection failed"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

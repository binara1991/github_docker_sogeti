import Flask, jsonify
import pymysql

app = Flask(__name__)

# Database configuration
db = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='github_binara'
)

@app.route('/data')
def get_data():
    try:
        # Create a cursor
        cursor = db.cursor()

        # Execute SQL query
        cursor.execute("SELECT * FROM github_year")

        # Fetch data
        results = cursor.fetchall()

        # Close cursor
        cursor.close()

        # Return JSON response
        return jsonify(results)

    except pymysql.Error as e:
        # Handle database error
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    # Run Flask application on port 5000
    app.run(host='172.17.0.2', port=3306, debug=True)
from flask import Flask, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# Required MySQL configurations
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "github_binara"
app.config["MYSQL_PORT"] = 3306

# Corrected MySQL host configuration
app.config["MYSQL_HOST"] = "github_mysql"  # Use the correct IP address of the MySQL container

# Initialize MySQL extension
mysql = MySQL(app)

@app.route("/GET/github_language")
def github_language():
    try:
        # Get a cursor for MySQL connection
        cur = mysql.connection.cursor()

        # Execute the SQL query
        cur.execute("SELECT * FROM github_language")

        # Fetch all the results
        rv = cur.fetchall()

        # Close cursor
        cur.close()

        # Return JSON response
        return jsonify(rv)
    except Exception as e:
        # Handle exceptions
        return jsonify({"error": str(e)})
    
@app.route("/GET/github_year")
def github_year():
    try:
        # Get a cursor for MySQL connection
        cur = mysql.connection.cursor()

        # Execute the SQL query
        cur.execute("SELECT * FROM github_year")

        # Fetch all the results
        rv = cur.fetchall()

        # Close cursor
        cur.close()

        # Return JSON response
        return jsonify(rv)
    except Exception as e:
        # Handle exceptions
        return jsonify({"error": str(e)})
    
if __name__ == "__main__":
    # Run the Flask application
    app.run(host="0.0.0.0", port=5000, debug=True)

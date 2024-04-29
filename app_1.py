from flask import Flask
from flaskext.mysql import MySQL


app = Flask(__name__)
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'github_binara'
mysql = MySQL()
mysql.init_app(app)
    # Database configuration
#db = flask-mysql.connect(
 #   host='localhost',
 #   user='root',
 #   password='root',
   # database='github_binara'
#)
#cursor = mysql.get_db().cursor()

@app.route('/data')
def get_data():
    
        # Create a cursor
        cursor = mysql.get_db().cursor()

        # Execute SQL query
        cursor.execute("SELECT * FROM github_year")

        # Fetch data
        results = cursor.fetchall()

        # Close cursor
        cursor.close()

        # Return JSON response
        return jsonify(results)
 
    
if __name__ == "__main__":
    app.run(debug=True)
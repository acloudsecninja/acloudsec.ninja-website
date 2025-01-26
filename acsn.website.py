from flask import Flask, render_template

# Create a Flask app with the correct static folder path
app = Flask(__name__, static_folder='images', template_folder='templates')

# Define the homepage route
@app.route('/index.html')
def home():
    return render_template('index.html')

# Define the services page route
@app.route('/services.html')
def services():
    return render_template('services.html')

# Define the courses page route
@app.route('/courses.html')
def courses():
    return render_template('courses.html')

# Define the contactus page route
@app.route('/contactus.html')
def contactus():
    return render_template('contactus.html')


# Run the app
if __name__ == '__main__':
    app.run(debug=True)

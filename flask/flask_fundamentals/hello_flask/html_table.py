# This will be the "server" file where we will set up all of our routes to handle requests

from flask import Flask, render_template  # Import Flask class to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/table')
def htmltable():
    user_info = [
        {'first_name':'Michael', 'last_name':'Choi'},
        {'first_name':'John', 'last_name':'Supsupin'},
        {'first_name':'Mark', 'last_name':'Guillen'},
        {'first_name':'KB', 'last_name':'Tonel'}
    ]
    return render_template('table.html', users=user_info)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
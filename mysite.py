from flask import Flask, render_template, request, url_for, flash, session, send_from_directory, redirect
from werkzeug import secure_filename
import os
import sys


# Initialize the Flask application
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

reload(sys)  
# Define a route for the default URL, which loads the form
@app.route('/')
def form():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Get the name of the uploaded file
    file = request.files['file']

    filename = secure_filename(file.filename)

    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    flash('file uploaded')
    return render_template('index.html')
'''
    return redirect(url_for('uploaded_file',
                            filename=filename))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
'''
if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(debug=True)

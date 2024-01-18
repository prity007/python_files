from flask  import Flask, render_template
app = Flask(__name__)
app.config['ALLOWED_EXTENSIONS'] ={'csv'}

@app.route('/')
def index():
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
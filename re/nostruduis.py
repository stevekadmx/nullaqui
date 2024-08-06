from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    occupation = request.form.get('occupation')
    age = request.form.get('age')

    detail_desc = ''
    if name:
        detail_desc += f"Name: {name}<br>"
    if occupation:
        detail_desc += f"Occupation: {occupation}<br>"
    if age:
        detail_desc += f"Age: {age}<br>"

    return render_template_string("<html><body>{{ detail_desc }}</body></html>", detail_desc=detail_desc)

if __name__ == '__main__':
    app.run()

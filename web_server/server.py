from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)
print(__name__)

# decorator
@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong, try again.'


# =========================================================

# Refactored and discarded code

# @app.route('/about.html')
# def about():
#     return render_template('about.html')


# @app.route('/components.html')
# def components():
#     return render_template('components.html')


# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

# @app.route('/work.html')
# def work():
#     return render_template('work.html')


# @app.route('/works.html')
# def works():
#     return render_template('works.html')







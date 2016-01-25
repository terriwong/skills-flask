from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = 'HappyDoingHomeworkOnASunnySunday'


@app.route('/')
def index_page():
    """Show an index page."""

    # return "<html><body><button>Click here to start application</button></body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    return render_template("index.html")


@app.route('/application-form')
def show_application_form():
    """Show application form."""

    return render_template("application-form.html")


@app.route('/application', methods=['POST'])
def submit_application():
    """Handle submission of an application form."""

    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    salary = int(request.form.get("salary_requirement"))
    job_title = request.form.get("job")

    return render_template('application-response.html',
                            first_name=first_name,
                            last_name=last_name,
                            salary=salary,
                            job_title=job_title)


if __name__ == "__main__":
    app.run(debug=True)

"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright
#this is using hackbright.py, not a library!

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    html = render_template("student_info.html",
                            first=first,
                            last=last,
                            github=github)

    return html

@app.route('/student-search') #go here first otherwise nothing will be saved and run in '/student'
def get_student_form():
    """Show form for searching for a student"""

    return render_template("student_search.html")

@app.route('/student-display-form')
def student_form():
     """this is front desk that displays the blank add a new student form """
     return render_template("student_add.html")


@app.route('/student-add', methods=["POST"])
def student_add():
    """Add a student"""

    github = request.form.get('github')
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    #print(request.form)

    #new_student = request.form['github']
    #alternative

    hackbright.make_new_student(fname, lname, github)

    html = render_template("student_confirmation.html",
                            fname=fname,
                            lname=lname,
                            github=github)

    return (html)


@app.route('/new-student-display')
def student_display():

    #return render_template(some_page.htmls)
    return render_template('student_confirmation.html')



if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")

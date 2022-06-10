from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secrets,secrets,secret'

@app.route('/')
def counts():
    if "visits" not in session:
        session["visits"] = 1
    else:
        session["visits"] += 1
    return render_template("index.html")


@app.route('/destroy_session')
def reset_count():
    session.clear()
    # redirect is not only used for POST methods and session is not only used when there is a form.
    return redirect('/')

@app.route('/add_two')
def add_two():
    session["visits"] += 1
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
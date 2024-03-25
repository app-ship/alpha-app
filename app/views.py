from flask import Blueprint, request, render_template, redirect, url_for, send_file


# Placeholder function for processing, replace as necessary
def langchain_process(answers):
    return "Your customized app is ready. Please run the app on the SF Org.", "path/to/yourfile.zip"


app_views = Blueprint('app_views', __name__)

questions = [
    "What is the name and primary goal of your SalesForce App?",
    "Explain how the UI will look like?",
    "What do you want to show on UI and from where the data will come",
    "Explain the SalesForce objects and triggers you want to use?",
    "Explain the user flow in detail"
]


@app_views.route('/')
def questionnaire():
    return render_template("questions.html", questions=questions)


@app_views.route('/process', methods=['POST'])
def process_answers():
    answers = [request.form[f'answer{i + 1}'] for i in range(len(questions))]
    print(answers)  # Replace with actual processing
    return redirect(url_for('.progress'))


@app_views.route('/progress')
def progress():
    return render_template("progress.html")


@app_views.route('/results')
def results():
    results, _ = langchain_process([])
    return render_template("results.html", results=results)


@app_views.route('/download')
def download():
    file_path = 'path/to/yourfile.zip'  # Update this path
    return send_file(file_path, as_attachment=True)

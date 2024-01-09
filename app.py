from flask import Flask, render_template, url_for

app= Flask(__name__)

jobs = [
    {"id": 1,
     "title": "Data Analyst",
     "level":"Entry Level",
     "Location": "Dar es Salaam, Tanzania",
     "Salary": "1,500,000",
     "Mode":["Full-time","Hybrid"]
     },
    {"id": 2,
     "title": "Frontend Developer",
     "level":"Entry Level",
     "Location": "Tabora, Tanzania",
     "Mode":["Full-time","Office"]
     },
    {"id": 3,
     "title": "UI/UX designer",
     "level":"Entry Level",
     "Location": "Arusha, Tanzania",
     "Salary": "1,400,000",
     "Mode":["Full-time","Remote"]
     },
    {"id": 4,
     "title": "Backend Engineer",
     "level":"Entry Level",
     "Location": "Arusha, Tanzania",
     "Salary": "1,400,000",
     "Mode":["Full-time","Hybrid"]
     },
    ]

@app.route('/')
def index():
    return render_template('home.html', jobs=jobs)

@app.route('/job/<int:job_id>')
def job_details(job_id):
    for job in jobs:
        if job["id"] == job_id:
           return render_template('job_detail.html', job=job)
    return render_template('job_detail.html', {'message': 'Job not found'})



if __name__ == '__main__':
    app.run(debug=True)
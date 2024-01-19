from flask import Flask, render_template
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

app = Flask(__name__)

# Configure MongoDB connection
app.config['MONGO_URI'] = os.environ.get("MONGO_URI", "mongodb://localhost:27017/myportfolio")
mongo = PyMongo(app)

# Your routes and helper functions...

# Route for the home page
@app.route('/')
def home():
    # Fetch data from MongoDB
    basic_info_data = mongo.db.basic_info.find_one()

    app.logger.info(basic_info_data)

    # Map MongoDB data to the format used in the template
    mapped_info = {
        'name': basic_info_data.get('Name', ''),
        'designation': basic_info_data.get('Designation', ''),
        'description': basic_info_data.get('Description', ''),
        'photo': basic_info_data.get('Photo', ''),
        'github': basic_info_data.get('Github Profile Link', ''),
        'linkedin': basic_info_data.get('Linkedin Profile Link', ''),
        'instagram': basic_info_data.get('Instagram Profile Link', ''),
        'email': basic_info_data.get('Email Id', '')
    }

    return render_template('home.html', **mapped_info)


# Route for the education page
@app.route('/education')
def education():
    # Fetch education data from MongoDB
    education_data = list(mongo.db.education.find())

    # Check if any documents were found
    if education_data:
        # Map MongoDB data to the format used in the template
        mapped_education = []
        for record in education_data:
            mapped_education.append({
                'institute': record.get('Institute', ''),
                'degree': record.get('Degree', ''),
                'date': record.get('Date', ''),
                'extra info': record.get('Extra Info', ''),  # Corrected field name
                'image': record.get('Image', '')
            })

        return render_template('education.html', educationinfo=mapped_education, name="Jyotsna kadam")
    else:
        # Handle the case when no education data is found
        return render_template('error.html', message='No education data found')
    

    # Route for the skills page
@app.route('/skills')
def skills():
    # Fetch skill data from MongoDB
    skill_data = list(mongo.db.skills.find())

    # Check if any documents were found
    if skill_data:
        # Map MongoDB data to the format used in the template
        mapped_skills = []
        for record in skill_data:
            mapped_skills.append({
                'skill': record.get('Skill', ''),
                'image': record.get('Image', '')
            })

        return render_template('skills.html', skillsinfo=mapped_skills, name="Jyotsna kadam")
    else:
        # Handle the case when no skill data is found
        return render_template('error.html', message='No skill data found')


# Route for the projects page
@app.route('/projects')
def projects():
    # Fetch project data from MongoDB
    project_data = list(mongo.db.project.find())

    # Check if any documents were found
    if project_data:
        # Map MongoDB data to the format used in the template
        mapped_projects = []
        for record in project_data:
            mapped_projects.append({
                'project_name': record.get('Project Name', ''),
                'date': record.get('Date', ''),
                'image': record.get('Image', ''),
                'description': record.get('Description', '')
            })

        return render_template('projects.html', projectinfo=mapped_projects, name="Jyotsna kadam")  # Change here to projectinfo
    else:
        # Handle the case when no project data is found
        return render_template('error.html', message='No project data found')


# Route for the experience page
@app.route('/experience')
def experience():
    # Fetch experience data from MongoDB
    experience_data = list(mongo.db.experience.find())

    # Check if any documents were found
    if experience_data:
        # Map MongoDB data to the format used in the template
        mapped_experience = []
        for record in experience_data:
            mapped_experience.append({
                'company': record.get('Company', ''),
                'designation': record.get('Designation', ''),
                'image': record.get('Image', ''),
                'date': record.get('Date', ''),
                'info': record.get('Info', ''),
                'name': record.get('Name', '')
            })

        return render_template('experience.html', experienceinfo=mapped_experience, name="Jyotsna kadam")
    else:
        # Handle the case when no experience data is found
        return render_template('error.html', message='No experience data found')



# Your existing routes...

# Route for the resume page
@app.route('/resume')
def resume():
    resume_link = "https://drive.google.com/file/d/1eXVo4-ViEcxTA728oJ1vOQa9RCvMiZte/view"
    
    return render_template('resume.html', resumelink=resume_link, name="Jyotsna kadam")

# Similar routes and helper functions for other pages...

if __name__ == '__main__':
    # Use dynamic port binding, default to 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)

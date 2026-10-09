# AI Resume–Job Description Matcher

A Python and Streamlit application that compares a resume with a job description using NLP-based text similarity and predefined skill matching.

The application provides a custom resume–job description matching score to help identify relevant skills, missing skills, and areas where a resume can be improved for a target role.

## Features

- Compare resume text with a job description
- Calculate TF-IDF cosine similarity
- Detect technical and soft skills using a predefined skill list
- Calculate skill coverage based on detected job-relevant skills
- Generate an overall resume–JD matching score
- Display matching skills
- Identify missing job-relevant skills
- Show resume strengths
- Highlight areas for improvement
- Load sample resume and job description for quick testing
- Clear the input fields and enter custom resume/JD text
- Runs locally without sending resume data to an external AI API

## Technologies

- Python
- Streamlit
- Scikit-learn
- TF-IDF
- Cosine Similarity
- Regular Expressions

## How the Application Works

The application analyzes two text inputs:

1. Resume
2. Job Description

### 1. Text Similarity

The resume and job description are converted into TF-IDF vectors.

Cosine similarity is then used to measure the similarity between the two texts.

### 2. Skill Matching

The application checks both texts against a predefined list of technical and soft skills.

It identifies:

- Skills present in both the resume and job description
- Skills detected in the job description
- Skills missing from the resume

### 3. Overall Match

The application calculates a custom matching score using:

**Overall Match = 60% Content Similarity + 40% Skill Match**

This weighting is implemented for this project to combine text similarity with skill coverage.


## Project Structure

```text
resume-analyzer/
├── app.py
├── matcher.py
├── requirements.txt
├── sample_resume.txt
├── sample_job_description.txt
├── README.md
└── .gitignore
```

## How to Run on Windows

### 1. Open the project

Open the project folder in VS Code and open the integrated terminal.

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

For PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt:

```cmd
venv\Scripts\activate
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the application

```bash
python -m streamlit run app.py
```

The application will open in the browser at the local Streamlit address.

## Example Analysis

The application provides:

- **Overall Match** – combined custom matching score
- **Content Similarity** – similarity between resume and job description text
- **Skill Match** – percentage of detected job skills also found in the resume
- **Matching Skills** – skills detected in both texts
- **Missing Skills** – job-relevant skills not detected in the resume
- **Resume Strengths** – relevant skills already present
- **Areas to Improve** – skills that could be highlighted or developed

## Author

**Vaishnavi Rajure**

Computer Engineering Graduate | Python | Java | SQL | Machine Learning

GitHub: [VaishnaviRajure88](https://github.com/VaishnaviRajure88)

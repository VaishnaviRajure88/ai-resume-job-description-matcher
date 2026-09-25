# Resume–Job Description Matcher

A beginner-friendly Python and Streamlit project that compares resume text with a job description.

## Features

- Calculates a TF-IDF cosine-similarity score.
- Detects technical and soft skills from a predefined skill list.
- Shows matching skills.
- Shows skills found in the job description but missing from the resume.
- Runs locally without a paid AI API.

## Technologies

- Python
- Streamlit
- Scikit-learn
- TF-IDF
- Cosine Similarity

## Project Structure

```text
resume-job-matcher/
├── app.py
├── matcher.py
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Run on Windows

### 1. Open the project folder in VS Code

Open the terminal in VS Code.

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate it

PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, Command Prompt can be used:

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

The browser should open the Streamlit application.

## How It Works

The application takes two text inputs:

1. Resume text
2. Job description

Both texts are converted into TF-IDF vectors. Cosine similarity is then used to calculate how similar the two documents are.

The application also checks both texts against a predefined list of skills and displays:

- Skills present in both texts
- Skills required by the job description but not detected in the resume

## Important Limitation

The match percentage is a text-similarity score. It is not an ATS score, hiring probability, or guarantee of getting an interview.

The skill detector uses a predefined list in `matcher.py`. Add more skills to that list as needed.

## Future Improvements

- Support PDF and DOCX resume uploads.
- Extract text automatically from uploaded files.
- Add job-specific skill recommendations.
- Add charts for skill coverage.
- Store previous analyses in SQLite.
- Add an exportable report.

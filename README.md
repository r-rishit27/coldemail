# 🚀 Cold Email Generator

## 📘 Project Overview

This project automates the process of generating personalized cold emails for job applications. By simply pasting the URL of a job posting, the tool crafts a targeted email addressing the hiring manager and showcasing how the candidate's skills, experience, and portfolio align perfectly with the role.
![Alt text](https://github.com/r-rishit27/coldemail/blob/main/Screenshot%202024-08-31%20020645.png)
## 🛠️ Features

- **Job Posting URL Input**: Analyze job posting content directly from the URL.
- **Personalized Emails**: Tailors the email based on the candidate’s skills and experience relevant to the job.
- **Portfolio Highlight**: Automatically integrates relevant projects and achievements from the candidate's portfolio.
- **Hiring Manager Targeting**: The email is addressed specifically to the hiring manager.
  
## 🧠 Technologies Used

- **LangChain**: For precise and robust NLP-based text processing.
- **ChromaDB**: Used for lightning-fast semantic search, enabling rapid job description analysis.
- **Groq**: High-performance cloud computing for fast and scalable processing.
- **LLaMA 3.1**: Base Large Language Model (LLM) used for language generation and understanding.

## 📈 Workflow

1. **Job Posting URL**: User provides the URL of the job posting.
2. **NLP Text Processing**: The system processes the job description using LangChain.
3. **Semantic Search**: ChromaDB searches the most relevant parts of the candidate's profile to match the job.
4. **Personalized Email Generation**: LLaMA 3.1 generates a tailored email, addressing the hiring manager and outlining the candidate's fit for the role.

## 🚀 How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/cold-email-generator.git
   cd cold-email-generator
   
2.Install the dependencies:
 ```bash
pip install -r requirements.txt

3.Run the application:
 ```bash
python app.py

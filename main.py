import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.1-70b-versatile")

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}
            {link_list}
           
            ### INSTRUCTION:

Resepected Sir/Ma'am,

I hope this email finds you well.

My name is Rishit, and I am currently a pre-final year B.Tech student specializing in Smart Manufacturing at IIIT Chennai. I am reaching out to express my interest in exploring data science opportunities at [Company Name]. With a solid foundation in Python, Machine Learning, Deep Learning, Generative AI, DBMS, SQL, and Tableau, I believe I could bring valuable skills and insights to your team.

I recently completed a Data Science Internship at TnQ Technologies, where I contributed to optimizing their workflow by [briefly describe your contribution—e.g., developing a predictive model, automating a process, etc.]. This experience not only enhanced my technical skills but also deepened my understanding of how data-driven solutions can significantly improve business operations.

In addition to my internship experience, I have worked on several  projects in data science domain, including [mention one or two key projects briefly, e.g., "a machine learning model to predict customer churn" or "a deep learning model for image classification"]. These projects have helped me sharpen my problem-solving abilities and reinforced my passion for data science.

I am also proud to have won the Altair Data Science Hackathon, where my team and I developed [briefly describe the project—e.g., "an innovative solution for anomaly detection in manufacturing processes"]. This achievement, along with my role as the AI Club Head at IIIT Chennai, has equipped me with leadership and teamwork skills that I believe are crucial for a successful career in data science.

I am eager to bring my expertise and enthusiasm to [Company Name] and contribute to the innovative work your team is doing. I would be grateful for the opportunity to discuss how I could be a valuable addition to your data science team.

Thank you for considering my application. I look forward to the possibility of contributing to your organization.

Please find my resume attached below for your refrence.

Best regards,
Rishit
+91-9305654811
https://github.com/r-rishit27
https://drive.google.com/file/d/1VL7J-dUh6e4z6AXFGnbQWGq5IL8kkELO/view?usp=sharing

            Your job is to write a cold email to the hiring  managers regarding the job mentioned above describing your skillset and how you can contribute for companies growth
            in fulfilling their needs.
            Also add the most relevant ones from the following links to showcase your portfolio: {link_list}
            Remember you are Job Applicant
Do not provide a preamble.
### EMAIL (NO PREAMBLE):



            """
        )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content

if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))
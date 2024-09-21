import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from main import Chain
from portfolio import Portfolio
from utills import clean_text

tuneai_api_key: str = st.sidebar.text_input("TuneAI API Key", type="password")

def create_streamlit_app(llm, portfolio, clean_text):
    # Set the background and title styling
    st.markdown(
        """
        <style>
        .title {
            font-size: 3em;
            color: #0073e6;
            text-align: center;
        }
        .description {
            font-size: 1.2em;
            color: white;
            margin-bottom: 30px;
            text-align: center;
        }
        .submit-button {
            background-color: green;
            color: white;
            font-size: 1em;
            padding: 5px 10px;
            border-radius: 10 px;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .submit-button:hover {
            background-color: #005f00;
        }
        </style>
        """, unsafe_allow_html=True
    )

    # Title and description
    st.markdown("<div class='title'>📧 Cold Mail Generator</div>", unsafe_allow_html=True)
    st.markdown("<div class='description'>Generate personalized cold emails based on job postings!</div>", unsafe_allow_html=True)

    # Input field and button
    url_input = st.text_input("Enter Job Posting URL:", value="https://jobs.nike.com/job/R-33460", help="Paste the job posting URL here")
    submit_button = st.markdown('<button class="submit-button">Submit</button>' ,unsafe_allow_html=True)
    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)
            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)
                email = llm.write_mail(job, links)
                st.code(email, language='markdown')
        except Exception as e:
            st.error(f"An Error Occurred: {e}")

    # Footer
    st.markdown(
        """
        <div style='text-align: center; margin-top: 50px;'>
            <p>Powered by AI | Contact: <a href='mailto:support@coldmailgen.com'>support@coldmailgen.com</a></p>
        </div>
        """, unsafe_allow_html=True
    )

if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain, portfolio, clean_text)

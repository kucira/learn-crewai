import os
from dotenv import load_dotenv
load_dotenv()

from crew import SoftwareEngineerCrew

def run():
    inputs = {
        'document_file': './prd-document.docx',
    }
    SoftwareEngineerCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()    
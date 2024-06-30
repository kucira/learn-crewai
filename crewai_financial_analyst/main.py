import os
from dotenv import load_dotenv
load_dotenv()

from crew import FinancialAnalystCrew

def run():
    inputs = {
        'company_name': 'Astra International',
    }
    FinancialAnalystCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()    
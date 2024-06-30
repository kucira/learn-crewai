from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_google_genai import ChatGoogleGenerativeAI
from tools.document_reader import DocumentReader
from langchain.tools import StructuredTool

@CrewBase
class SoftwareEngineerCrew():
	"""SoftwareEngineer crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	def __init__(self) -> None:
		self.gemini_llm = ChatGoogleGenerativeAI(temperature=0, model="gemini-pro")

	@agent
	def document_reader_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['document_reader_agent'],
			llm=self.gemini_llm,
   			tools=DocumentReader.tools()
		)
     
	@agent
	def system_analyst_researcher(self) -> Agent:
		return Agent(
			config = self.agents_config['system_analyst_researcher'],
			llm = self.gemini_llm
		)

	@agent
	def software_engineer_analyst(self) -> Agent:
		return Agent(
			config = self.agents_config['software_engineer_analyst'],
			llm = self.gemini_llm
		)
  	
	@task
	def document_reader_task(self) -> Task:
		return Task(
			config=self.tasks_config['document_reader_task'],
			agent=self.document_reader_agent()
		)   
   
	@task
	def system_analyst_researcher_task(self) -> Task:
		return Task(
			config = self.tasks_config['system_analyst_researcher_task'],
			agent = self.system_analyst_researcher()
		)

	@task
	def software_engineer_analyst_task(self) -> Task:
		return Task(
			config = self.tasks_config['software_engineer_analyst_task'],
			agent = self.software_engineer_analyst()
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the SoftwareEngineer crew"""
		return Crew(
			agents =  self.agents,
			tasks = self.tasks,
			process = Process.sequential,
			verbose = 2
		)
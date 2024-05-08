from textwrap import dedent
from crewai import Task

class ResearchTask():
    def research_task(self, agent, website):
        return Task(
            description=dedent(f"""\
                               Researching {website}
                               """),
        )
from typing import List
from crewai import Agent, Crew, Task, Process
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent

from publishing_house.crews.copy_to_a_document.custom_tool.custom_tool import DocxWriterTool

@CrewBase
class copyToDocument:
    """Book Writing Crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"
    
    @agent
    def DocumentWriterAgent(self) -> Agent:
        return Agent(
            config=self.agents_config['DocumentWriterAgent'],
            verbose=True,
        )

    @task
    def format_text_to_document(self) -> Task:
        return Task(
            config=self.tasks_config['formatBookDocument'],
            agent=self.DocumentWriterAgent(),
            tools=[DocxWriterTool()],
            expected_output="A DOCX file saved at output/book.docx containing the formatted manuscript.",
      
        )
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
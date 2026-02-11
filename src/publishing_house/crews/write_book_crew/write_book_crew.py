from typing import List
from crewai import Agent, Crew, Task, Process
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from crewai.agents.agent_builder.base_agent import BaseAgent

from publishing_house.types import ChapterContent

@CrewBase
class WriteBookCrew:
    """Book Writing Crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"
    
    @agent
    def writer(self) -> Agent:
        return Agent(
            config=self.agents_config['writer'], # type: ignore[index]
            verbose=True,
            tools=[]
        )
    
    @task
    def write_book(self) -> Task:
        return Task(
            config=self.tasks_config['write_book'], # type: ignore[index]
            agent=self.writer(), # type: ignore[index]
            output_pydantic=ChapterContent
        )
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
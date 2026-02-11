from typing import List
from crewai import Agent, Crew, Task, Process
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from crewai.agents.agent_builder.base_agent import BaseAgent

from publishing_house.types import BookOutline

@CrewBase
class OutlineBookCrew:
    """Book Outline Crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"
    
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'], # type: ignore[index]
            verbose=True,
            tools=[SerperDevTool(), ScrapeWebsiteTool()]
        )
    
    @agent
    def outliner(self) -> Agent:
        return Agent(
            config=self.agents_config['outliner'], # type: ignore[index]
            verbose=True
        )
    
    @task
    def research_topic(self) -> Task:
        return Task(
            config=self.tasks_config['research_topic'], # type: ignore[index]
            agent=self.researcher()
        )
    
    @task
    def generate_outline(self) -> Task:
        return Task(
            config=self.tasks_config['generate_outline'], # type: ignore[index]
            agent=self.outliner(),
            output_pydantic=BookOutline
        )
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
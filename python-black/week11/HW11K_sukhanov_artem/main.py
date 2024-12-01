import asyncio
import os
from collections.abc import AsyncIterable

import aiofiles
from aiocsv import AsyncDictWriter, AsyncDictReader


class CSVReader:
    def __init__(self, file_path: str, chunk_size: int = 1024):
        self.file_path = file_path
        self.chunk_size = chunk_size
        self.headers = None

    async def read_in_chunks(self) -> AsyncIterable[list[dict[str, str]]]:
        async with aiofiles.open(self.file_path, mode='r') as file:
            reader = AsyncDictReader(file)
            self.headers = reader.fieldnames
            chunk = []
            async for row in reader:
                chunk.append(row)
                if len(chunk) >= self.chunk_size:
                    yield chunk
                    chunk = []
            if chunk:
                yield chunk

    @staticmethod
    def clean_review(review: dict[str, str]) -> dict[str, str]:
        return {key: value.strip() for key, value in review.items()}


class ProjectDataProcessor:
    def __init__(self):
        self.projects = []
        self.tasks = []

    async def load_projects(self, file_path: str):
        async with aiofiles.open(file_path, mode='r') as file:
            reader = AsyncDictReader(file)
            async for row in reader:
                self.projects.append(row)

    async def load_tasks(self, file_path: str):
        async with aiofiles.open(file_path, mode='r') as file:
            reader = AsyncDictReader(file)
            async for row in reader:
                self.tasks.append(row)

    def get_projects_in_progress(self):
        return [project for project in self.projects if project['Статус'] == 'В процессе']

    def get_tasks_for_project(self, project_id: str):
        return [task for task in self.tasks if task['ID проекта'] == project_id]


class ProjectFileWriter:
    def __init__(self, output_dir: str):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    async def save_project_data(self, file_name: str, data: list[dict[str, str]]):
        file_path = os.path.join(self.output_dir, file_name)
        fieldnames: list[str] = list(data[0].keys())

        async with aiofiles.open(file_path, mode='w', newline='') as file:
            writer = AsyncDictWriter(file, fieldnames=fieldnames)
            await writer.writeheader()
            for row in data:
                await writer.writerow(row)


class ProjectManager:
    def __init__(self, projects_path: str, tasks_path: str, output_dir: str):
        self.projects_path = projects_path
        self.tasks_path = tasks_path
        self.output_dir = output_dir
        self.data_processor = ProjectDataProcessor()
        self.file_writer = ProjectFileWriter(output_dir)

    async def load_data(self):
        await asyncio.gather(
            self.data_processor.load_projects(self.projects_path),
            self.data_processor.load_tasks(self.tasks_path)
        )

    async def analyze_data(self):
        projects_in_progress = self.data_processor.get_projects_in_progress()
        result = []
        for project in projects_in_progress:
            tasks = self.data_processor.get_tasks_for_project(project['ID'])
            result.append({
                'project': project,
                'tasks': tasks
            })
        return result

    async def add_new_task(self, task: dict[str, str]):
        # Check if project exists and task ID is unique
        project_ids = {project['ID'] for project in self.data_processor.projects}
        if task['ID проекта'] not in project_ids:
            raise ValueError("Project not found")
        task_ids = {task['ID'] for task in self.data_processor.tasks}
        if task['ID'] in task_ids:
            raise ValueError("Task ID must be unique")

        self.data_processor.tasks.append(task)
        await self.file_writer.save_project_data('tasks.csv', self.data_processor.tasks)

    async def update_project_statuses(self):
        for project in self.data_processor.projects:
            project_id = project['ID']
            tasks = self.data_processor.get_tasks_for_project(project_id)
            if all(task['Статус'] == 'Завершена' for task in tasks):
                project['Статус'] = 'Завершён'
        await self.file_writer.save_project_data('projects.csv', self.data_processor.projects)


async def main():
    project_manager = ProjectManager('projects.csv', 'tasks.csv', 'output_data')
    await project_manager.load_data()

    # Analyze data
    analysis_result = await project_manager.analyze_data()
    for item in analysis_result:
        print(f"Project: {item['project']['Название']}")
        for task in item['tasks']:
            print(f"  Task: {task['Название задачи']} - {task['Статус']}")

    # Add a new task
    new_task = {
        'ID': '99999',
        'Название задачи': 'Оптимизация API',
        'Статус': 'Не начата',
        'ID проекта': '1'
    }
    await project_manager.add_new_task(new_task)

    # Update project statuses
    await project_manager.update_project_statuses()


if __name__ == '__main__':
    asyncio.run(main())

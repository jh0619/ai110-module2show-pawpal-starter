from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Pet:
    name: str
    species: str
    age: int
    notes: str
    tasks: list[Task] = field(default_factory=list)

    def get_profile(self) -> str:
        """Return a formatted profile of the pet."""
        profile = "Pet Profile:\n"
        profile += f"  Name: {self.name}\n"
        profile += f"  Species: {self.species}\n"
        profile += f"  Age: {self.age} years\n"
        profile += f"  Notes: {self.notes}\n"
        profile += f"  Active Tasks: {len([t for t in self.tasks if not t.is_completed])}/{len(self.tasks)}\n"
        return profile

    def update_info(
        self,
        name: str,
        species: str,
        age: int,
        notes: str,
    ) -> None:
        """Update the pet's information."""
        self.name = name
        self.species = species
        self.age = age
        self.notes = notes


@dataclass
class Owner:
    name: str
    available_time: int
    preferences: list[str]
    pets: list[Pet] = field(default_factory=list)

    def update_availability(self, available_time: int) -> None:
        """Update the owner's available time."""
        self.available_time = available_time

    def set_preferences(self, preferences: list[str]) -> None:
        """Set the owner's preferences for pet care."""
        self.preferences = preferences

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the owner's collection."""
        self.pets.append(pet)

    def remove_pet(self, pet: Pet) -> None:
        """Remove a pet from the owner's collection."""
        if pet in self.pets:
            self.pets.remove(pet)

    def get_all_tasks(self) -> list[Task]:
        """Retrieve all tasks from all pets."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.tasks)
        return all_tasks


@dataclass
class Task:
    title: str
    duration: int
    priority: str
    category: str
    description: str = ""
    time: str = ""
    frequency: str = ""
    is_completed: bool = False

    def mark_completed(self) -> None:
        """Mark the task as completed."""
        self.is_completed = True

    def update_task(
        self,
        title: str,
        duration: int,
        priority: str,
        category: str,
        description: str = "",
        time: str = "",
        frequency: str = "",
    ) -> None:
        """Update all task details."""
        self.title = title
        self.duration = duration
        self.priority = priority
        self.category = category
        self.description = description
        self.time = time
        self.frequency = frequency

    def get_task_info(self) -> str:
        """Return a formatted string with all task information."""
        info = f"Task: {self.title}\n"
        info += f"Description: {self.description}\n"
        info += f"Duration: {self.duration} minutes\n"
        info += f"Priority: {self.priority}\n"
        info += f"Category: {self.category}\n"
        info += f"Time: {self.time}\n"
        info += f"Frequency: {self.frequency}\n"
        info += f"Status: {'Completed' if self.is_completed else 'Pending'}\n"
        return info


@dataclass
class Scheduler:
    tasks: list[Task] = field(default_factory=list)
    available_time: int = 0
    generated_plan: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to the scheduler."""
        self.tasks.append(task)

    def remove_task(self, task: Task) -> None:
        """Remove a task from the scheduler."""
        if task in self.tasks:
            self.tasks.remove(task)

    def generate_plan(
        self,
        available_time: int,
        preferences: list[str],
    ) -> list[Task]:
        """Generate an optimized plan based on available time and preferences.

        Tasks are prioritized by priority level, then sorted by duration.
        Tasks are added to the plan if they fit within available time.
        """
        self.available_time = available_time

        # Filter incomplete tasks
        incomplete_tasks = [t for t in self.tasks if not t.is_completed]

        # Sort by priority and duration
        priority_order = {"high": 1, "medium": 2, "low": 3}
        sorted_tasks = sorted(
            incomplete_tasks,
            key=lambda t: (priority_order.get(t.priority, 4), t.duration)
        )

        # Fit tasks into available time
        self.generated_plan = []
        total_time = 0
        for task in sorted_tasks:
            if total_time + task.duration <= available_time:
                self.generated_plan.append(task)
                total_time += task.duration

        return self.generated_plan

    def explain_plan(self) -> str:
        """Return a formatted explanation of the generated plan."""
        if not self.generated_plan:
            return "No plan generated yet."

        explanation = "Generated Plan:\n"
        explanation += "=" * 40 + "\n"
        total_duration = 0
        for i, task in enumerate(self.generated_plan, 1):
            explanation += f"{i}. {task.title} ({task.duration} min)\n"
            explanation += f"   Priority: {task.priority}\n"
            total_duration += task.duration

        explanation += "=" * 40 + "\n"
        explanation += f"Total Duration: {total_duration}/{self.available_time} minutes\n"
        return explanation

    def get_plan(self) -> list[Task]:
        """Return the currently generated plan."""
        return self.generated_plan

    def get_plan_by_time(self) -> list[Task]:
        """Return the generated plan sorted chronologically by time."""
        def time_to_minutes(time_str: str) -> int:
            """Convert time string (e.g., '8:00 AM') to minutes since midnight."""
            if not time_str:
                return 0
            try:
                parts = time_str.split()
                time_parts = parts[0].split(':')
                hour = int(time_parts[0])
                minute = int(time_parts[1])
                period = parts[1].upper() if len(parts) > 1 else "AM"

                if period == "PM" and hour != 12:
                    hour += 12
                elif period == "AM" and hour == 12:
                    hour = 0

                return hour * 60 + minute
            except (ValueError, IndexError):
                return 0

        return sorted(self.generated_plan, key=lambda t: time_to_minutes(t.time))

from pawpal_system import Pet, Owner, Task, Scheduler


def main():
    """Demo script for PawPal pet care scheduling system."""

    # Create Owner
    owner = Owner(
        name="Sarah",
        available_time=120,  # 2 hours available
        preferences=["morning routine", "exercise", "grooming"]
    )

    # Create Pets
    dog = Pet(
        name="Max",
        species="Golden Retriever",
        age=3,
        notes="Energetic and loves outdoor activities"
    )

    cat = Pet(
        name="Whiskers",
        species="Persian Cat",
        age=5,
        notes="Indoor cat, enjoys grooming and play"
    )

    # Add pets to owner
    owner.add_pet(dog)
    owner.add_pet(cat)

    # Create Tasks for Max (Dog)
    task1 = Task(
        title="Morning Walk",
        duration=30,
        priority="high",
        category="exercise",
        description="Take Max for a morning jog in the park",
        time="8:00 AM",
        frequency="daily"
    )

    task2 = Task(
        title="Feed Max",
        duration=10,
        priority="high",
        category="feeding",
        description="Prepare and serve breakfast",
        time="8:30 AM",
        frequency="twice daily"
    )

    task3 = Task(
        title="Bath Time",
        duration=20,
        priority="medium",
        category="grooming",
        description="Give Max a bath and brush",
        time="5:00 PM",
        frequency="weekly"
    )

    # Create Tasks for Whiskers (Cat)
    task4 = Task(
        title="Feed Whiskers",
        duration=5,
        priority="high",
        category="feeding",
        description="Prepare wet food and refill water bowl",
        time="7:00 AM",
        frequency="twice daily"
    )

    task5 = Task(
        title="Brush Whiskers",
        duration=15,
        priority="medium",
        category="grooming",
        description="Gentle brushing to prevent matting",
        time="6:00 PM",
        frequency="daily"
    )

    # Add tasks to pets
    dog.tasks.extend([task1, task2, task3])
    cat.tasks.extend([task4, task5])

    # Create scheduler and add all tasks
    scheduler = Scheduler()
    for task in owner.get_all_tasks():
        scheduler.add_task(task)

    # Generate today's schedule
    scheduler.generate_plan(
        available_time=owner.available_time,
        preferences=owner.preferences
    )

    # Print Today's Schedule
    print("\n" + "=" * 60)
    print("🐾 PAWPAL - TODAY'S PET CARE SCHEDULE 🐾")
    print("=" * 60)

    print(f"\nOwner: {owner.name}")
    print(f"Available Time: {owner.available_time} minutes")
    print(f"Preferences: {', '.join(owner.preferences)}")

    print("\n📋 PETS IN CARE:")
    print("-" * 60)
    for pet in owner.pets:
        print(pet.get_profile())

    print("\n📅 TODAY'S OPTIMIZED SCHEDULE:")
    print("-" * 60)
    print(scheduler.explain_plan())

    print("📝 DETAILED TASK LIST:")
    print("-" * 60)
    for i, task in enumerate(scheduler.get_plan_by_time(), 1):
        print(f"\n{i}. {task.get_task_info()}")

    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()

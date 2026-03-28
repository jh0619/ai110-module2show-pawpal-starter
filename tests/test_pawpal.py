from pawpal_system import Task, Pet, Scheduler, Owner
import sys
sys.path.insert(0, '/Users/jiahou/Desktop/AI110/ai110-module2show-pawpal-starter')


def test_mark_complete():
    """Test that calling mark_complete() changes the task's status."""
    task = Task("Feed the dog", 10, "high", "feeding")
    assert task.is_completed == False, "Task should start as incomplete"

    task.mark_complete()
    assert task.is_completed == True, "Task status should be True after calling mark_complete()"


def test_mark_complete_creates_next_for_daily_task():
    """Daily tasks should generate a new pending occurrence when completed."""
    task = Task("Feed", 10, "high", "feeding", frequency="daily")

    next_task = task.mark_complete()

    assert task.is_completed == True
    assert next_task is not None
    assert next_task.title == task.title
    assert next_task.frequency == "daily"
    assert next_task.is_completed == False


def test_mark_complete_creates_next_for_weekly_task():
    """Weekly tasks should generate a new pending occurrence when completed."""
    task = Task("Groom", 30, "medium", "care", frequency="weekly")

    next_task = task.mark_complete()

    assert task.is_completed == True
    assert next_task is not None
    assert next_task.frequency == "weekly"
    assert next_task.is_completed == False


def test_mark_complete_non_recurring_returns_none():
    """Non-recurring tasks should not generate new occurrences."""
    task = Task("Play", 15, "low", "exercise", frequency="once")

    next_task = task.mark_complete()

    assert task.is_completed == True
    assert next_task is None


def test_scheduler_mark_task_complete_appends_next_occurrence():
    """Scheduler completion should auto-add the next recurring task."""
    scheduler = Scheduler()
    task = Task("Feed", 10, "high", "feeding", frequency="daily")
    scheduler.add_task(task)

    next_task = scheduler.mark_task_complete(task)

    assert next_task is not None
    assert len(scheduler.tasks) == 2
    assert scheduler.tasks[0].is_completed == True
    assert scheduler.tasks[1].is_completed == False


def test_detect_time_conflicts_same_pet_warning():
    """Scheduler should warn on same-time tasks for the same pet."""
    owner = Owner("Sam", 120, [])
    pet = Pet("Buddy", "Dog", 3, "friendly")
    owner.add_pet(pet)

    task1 = Task("Feed", 10, "high", "feeding", time="8:00 AM")
    task2 = Task("Walk", 20, "medium", "exercise", time="8:00 AM")
    pet.tasks.extend([task1, task2])

    scheduler = Scheduler(tasks=[task1, task2])
    warnings = scheduler.detect_time_conflicts(
        task_pet_map=owner.get_task_pet_map()
    )

    assert len(warnings) == 1
    assert "same pet" in warnings[0]


def test_detect_time_conflicts_different_pets_warning():
    """Scheduler should warn on same-time tasks for different pets."""
    owner = Owner("Sam", 120, [])
    dog = Pet("Buddy", "Dog", 3, "friendly")
    cat = Pet("Luna", "Cat", 2, "calm")
    owner.add_pet(dog)
    owner.add_pet(cat)

    dog_task = Task("Feed Buddy", 10, "high", "feeding", time="8:00 AM")
    cat_task = Task("Feed Luna", 10, "high", "feeding", time="8:00 AM")
    dog.tasks.append(dog_task)
    cat.tasks.append(cat_task)

    scheduler = Scheduler(tasks=[dog_task, cat_task])
    warnings = scheduler.detect_time_conflicts(
        task_pet_map=owner.get_task_pet_map()
    )

    assert len(warnings) == 1
    assert "different pets" in warnings[0]


def test_detect_time_conflicts_invalid_time_returns_warning():
    """Invalid task time should return warning and not crash."""
    scheduler = Scheduler(
        tasks=[Task("Feed", 10, "high", "feeding", time="not-a-time")]
    )

    warnings = scheduler.detect_time_conflicts()

    assert len(warnings) == 1
    assert "Skipped invalid task time" in warnings[0]


def test_add_task_to_pet():
    """Test that adding a task to a Pet increases that pet's task count."""
    pet = Pet("Buddy", "Dog", 3, "friendly")
    assert len(pet.tasks) == 0, "Pet should start with 0 tasks"

    task1 = Task("Feed", 10, "high", "feeding")
    pet.tasks.append(task1)
    assert len(pet.tasks) == 1, "Pet should have 1 task after adding"

    task2 = Task("Walk", 20, "medium", "exercise")
    pet.tasks.append(task2)
    assert len(pet.tasks) == 2, "Pet should have 2 tasks after adding another task"

from pawpal_system import Task, Pet
import sys
sys.path.insert(0, '/Users/jiahou/Desktop/AI110/ai110-module2show-pawpal-starter')


def test_mark_complete():
    """Test that calling mark_complete() changes the task's status."""
    task = Task("Feed the dog", 10, "high", "feeding")
    assert task.is_completed == False, "Task should start as incomplete"

    task.mark_complete()
    assert task.is_completed == True, "Task status should be True after calling mark_complete()"


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

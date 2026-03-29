# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

Based on the PawPal+ scenario, I identified three core actions that a user should be able to perform:

1.Add and manage pet information
The user should be able to input basic information about their pet (such as name, type, and basic needs). This allows the system to personalize care tasks.
2.Create and manage care tasks
The user should be able to add, edit, and delete pet care tasks (e.g., walks, feeding, medication). Each task should include attributes like duration and priority so the system can make scheduling decisions.
3.Generate and view a daily care plan
The user should be able to generate a daily schedule based on their available time and task priorities, and view the planned tasks clearly, ideally with explanations of why tasks were selected.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

Yes, my design changed during implementation in a few important ways.

First, I converted all four classes (`Pet`, `Owner`, `Task`, and `Scheduler`) into Python dataclasses. I originally only planned this for object-heavy classes, but using dataclasses across the board made the model definitions cleaner, more consistent, and easier to read while still keeping method stubs empty for this stage.

Second, I added explicit relationship fields to better match the UML: `Owner` now has a `pet` reference, and `Pet` now has a `tasks` list. This made the class relationships visible directly in code instead of being implied by comments or future logic.

Overall, these changes improved alignment between UML and code structure and set up a safer foundation before implementing scheduling behavior.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

My scheduler currently considers three main inputs: **available time**, **task priority**, and **task completion status** (it only schedules incomplete tasks). It sorts tasks by priority (`high` → `medium` → `low`), then by shorter duration, and adds tasks only if they fit within the owner’s available minutes.

I decided these constraints mattered most because they directly affect whether a schedule is practical for daily use. Time is the hard limit, so it is enforced first through fit checks. Priority comes next so essential care tasks are selected before optional ones. Preferences are included in the method signature and UI flow, but in this version they are a secondary design placeholder rather than a strict decision rule; I prioritized building a reliable baseline scheduler first.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

One tradeoff my scheduler makes is using a simple greedy strategy: it sorts tasks by priority and duration, then picks tasks in that order until time runs out. This is fast and easy to explain, but it does not always produce the mathematically optimal combination of tasks.

I think this is reasonable for the PawPal+ scenario because the app is meant for practical daily planning, not perfect optimization. A caregiver usually needs a clear, predictable plan they can trust quickly. The greedy approach gives stable results, keeps runtime low, and makes the scheduling behavior transparent to users. In future iterations, I could add a more advanced optimizer if the project needs stronger optimization guarantees.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

I used AI as a development assistant for several stages of the project: generating early UI structure, suggesting class and method scaffolds, and helping refine scheduler-related logic. The most useful prompts were specific, task-focused requests such as “add form inputs for pet profile fields,” “show how to structure task CRUD in Streamlit,” and “propose test cases for scheduling conflicts and recurrence.”

AI was especially helpful for accelerating boilerplate and giving me alternative implementation ideas, but it worked best when I gave clear constraints and expected behaviors. Generic prompts produced generic UI output, while detailed prompts with explicit requirements led to more practical suggestions.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

One clear moment was the original AI-generated UI draft. I did not accept it as-is because it missed core functionality: there was no working flow to add a new pet, no complete path to add a new task, and tasks with time conflicts could still be added to the task list without proper prevention or warning.

I evaluated the AI output by running the app manually through real user flows (create pet, create task, edit task, generate plan) and checking behavior against the project requirements. I then revised the implementation to include the missing add-pet and add-task interactions and strengthened conflict handling logic. I also used tests and repeated manual checks to confirm that the final behavior matched expected scheduling rules.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

I tested the scheduler behaviors that most directly affect correctness and daily usability: chronological sorting of planned tasks, recurring task creation (daily/weekly), time-conflict detection, and edge-case handling for invalid or unusual time inputs (including noon/midnight style ordering). I also checked that non-recurring tasks do not create extra occurrences and that filtering by completion/pet works as expected.

These tests were important because they cover both core logic and failure-prone boundaries. In a planning app, ordering and recurrence errors can make a schedule unreliable, and weak conflict checks can create impossible plans. By validating these areas, I reduced the chance of high-impact scheduling mistakes in normal use.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

I am highly confident in the current scheduler behavior for the implemented scope (about 5/5 confidence for core features), supported by passing automated tests and repeated manual app walkthroughs.

If I had more time, I would add tests for more complex combinations: multiple pets with dense overlapping schedules, very large task lists, mixed recurring + one-time tasks on the same timestamp, timezone/date-boundary transitions, and stricter UI-level validation to block conflict-creating inputs before submission.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

I am most satisfied with the backend design and the clarity of the class structure. The UML-to-code mapping was clean, and the responsibilities of `Pet`, `Owner`, `Task`, and `Scheduler` stayed understandable throughout implementation. Having a clear class diagram early made later coding and testing much easier.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

If I had another iteration, I would improve the UI significantly. The current interface works, but it still looks very basic and could be more user-friendly and polished. I would redesign the layout and interaction flow so key actions (adding pets, managing tasks, resolving conflicts) feel more intuitive.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

My biggest takeaway is: test, test, test. Running the app with different user inputs quickly reveals what was truly implemented and what was missing. I initially assumed the AI-generated frontend was fully connected to backend logic, but real testing showed the first version was weak and missing core features. This taught me that AI output should be treated as a draft and always verified with both manual flows and automated tests.

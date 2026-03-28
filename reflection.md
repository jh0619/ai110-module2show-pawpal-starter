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

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

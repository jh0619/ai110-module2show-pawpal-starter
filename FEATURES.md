# Features

Implemented algorithms and scheduling behaviors:

- **Priority + duration scheduling:** Sorts incomplete tasks by priority (`high` → `medium` → `low`) and then by shorter duration first.
- **Available-time bounded planning:** Greedily adds tasks only while total planned duration stays within the owner’s available minutes.
- **Chronological sorting:** Returns generated plans in time order using AM/PM-aware parsing.
- **Time conflict warnings:** Detects same-time task conflicts and generates human-readable warnings.
- **Cross-pet conflict scope:** Labels conflicts as `same pet` or `different pets` when task-to-pet mapping is available.
- **Invalid-time resilience:** Skips malformed time values safely and reports warnings instead of failing.
- **Daily/weekly recurrence:** Completing `daily` or `weekly` tasks automatically creates the next pending occurrence.
- **Date-aware recurrence shifting:** If a task time includes a date, recurrence moves forward by +1 day (daily) or +7 days (weekly).
- **Task filtering:** Supports filtering tasks by completion status and by pet name.

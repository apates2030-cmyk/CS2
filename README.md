# General Task Organizer
---
## Overview/Description
A task organizer that helps students track their homework or assignments for the day.


## Features

The project can:
✔ Add tasks
✔ View tasks
✔ Mark tasks as completed

## Methodology
Tasks are stored in an already made array. To add tasks, `append()` is used.
	<ins>ex.</ins>
>     tasks.append({
        "task": task,
        "priority": priority,
        "due": due
    })
To complete them, it removes tasks using `pop()`.
	<ins>ex.</ins>
> def complete_task():
    try:
        number = int(input("Task number you want to mark as complete: ")) - 1

        if 0 <= number < len(tasks):
            removed = tasks.pop(number)
To view, it uses `enumerate().` 
<ins>ex.</ins>
> for i, t in enumerate(tasks, 1):

A `while True` loop keeps the organizer working.

## Technologies Used
We used Python, so that it could easily be read and understood by a wide range of our audience. We also used it for its simplicity.

## Ethical Considerations
It follows principles from the Association for Computing Machinery and its ACM Code of Ethics and Professional Conduct regarding privacy and honesty in programming since it doesn't steal any data. Our organizer does not use any external libraries.

## How to Run the Program
1. Have Python installed.
2. Download the file `task_org.py`.
3. Open a command prompt.
4. Run the program by clicking `Run..`
5. Follow the on-screen instruction to enter tasks.
---

## Example Output
(Start Program)

(Empty Task Sheet)

Decision

1. Add Task

2. Mark Task as Complete

3. View

4. End

Input number: 1

Input Task: `Computer Science Quarter Project`

Print: `Computer Science Quarter Project added!`

--------    
## Contributor
- Student 1: Pates (readme, code)
- Student 2: Maribao ()
- Student 3: Rosal ()

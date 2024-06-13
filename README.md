# Phase 3 CLI Project fittrack
# FitTrack CLI

**FitTrack** is a command-line interface (CLI) application designed to help users track fitness metrics, activities, nutrition, goals, and reminders.

## Features

- Track fitness metrics such as weight and calories.
- Log and view physical activities.
- Log and view nutrition details.
- Set and track fitness goals.
- Set and view reminders.
- Analyze collected data.



```console
fittrack/
├── __pycache__
├── __init__.py
├── cli.py
├── database.py
├── db/
│   ├── __init__.py
│   └── models.py
├── goal.py
├── metrics.py
├── nutrition.py
├── reminder.py
├── util/
    ├── __init__.py
    ├── analysis.py
    ├── validators.py
 ## example:

Log Nutrition:
fittrack log-nutrition [food] [calories]

Example:
fittrack log-nutrition apple 95

View Nutrition:
fittrack view-nutrition



Contributing
Contributions are welcome! Please open an issue or submit a pull request on GitHub.

License
This project is licensed under the MIT License. See the LICENSE file for more information.

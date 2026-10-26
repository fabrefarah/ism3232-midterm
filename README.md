# ISM3232 Midterm: Catering Event Program

- **Name:** Farah Fabre
- **Version:** 1.0
- **Date:** October 25, 2026

## What This Program Does

This program helps calculate the costs for catering events based on the number of guests and the event type. It also calculates discounts and fees and checks if an event needs approval or an extra chef.

## Business Rules

1. Events with fewer than 25 guests do not get a discount.
2. Events with 25 to 99 guests get a 5% discount.
3. Events with 100 or more guests get a 12% discount if they are nonprofit events, or a 5% discount for regular events.
4. A $75 service fee is added when the discounted food cost is $500 or less.
5. Events costing more than $2,500 need sign-off.
6. Events with more than 80 guests or a total cost of $3,000 or more need a second chef.

## How to Run

Open the terminal in the project folder and run these commands to set up the project and start the program.

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 main.py
```

## How to Test

Use these commands to check the code and run the tests.

```bash
ruff check .
pytest -v
```

I wrote 20 tests to check that the calculations and business rules work correctly.

## Files in This Repository

- `business_rules.py` — Has the functions for calculating event costs and checking the rules.
- `main.py` — Runs the program and prints the event results.
- `commands.md` — Shows the terminal commands I used for the project.
- `README.md` — Explains what the program does and how to run it.
- `requirements.txt` — Lists the packages needed to run the project.
- `.gitignore` — Keeps unnecessary files, like the virtual environment and cache files, out of GitHub.
- `tests/__init__.py` — Helps Python recognize the tests folder as a package.
- `tests/test_business_rules.py` — Contains the 20 tests for the program.

## AI Use Statement

I did not use AI to help me with this project.
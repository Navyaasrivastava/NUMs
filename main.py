from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

# Home route
@app.get("/")
def home():
    return {"message": "Welcome to NUMs API! Use /mulank endpoint with your DOB."}

# Mulank calculation route
@app.get("/mulank")
def mulank(dob: str):
    """
    Pass dob in YYYY-MM-DD format.
    Example: /mulank?dob=2005-08-15
    """
    try:
        date_obj = datetime.strptime(dob, "%Y-%m-%d")
    except ValueError:
        return {"error": "Invalid date format. Use YYYY-MM-DD."}

    # Calculate mulank (sum of digits of day)
    day = date_obj.day
    mulank = sum(int(d) for d in str(day))

    # Reduce to single digit
    while mulank > 9:
        mulank = sum(int(d) for d in str(mulank))

    # Lucky number = mulank + 7 (example logic)
    lucky_number = mulank + 7

    return {"dob": dob, "mulank": mulank, "lucky_number": lucky_number}


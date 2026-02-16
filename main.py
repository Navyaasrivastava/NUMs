from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

# Home route to avoid 404
@app.get("/")
def home():
    return {"message": "Welcome to NUMs API! Use /mulank endpoint with your DOB in YYYY-MM-DD format."}

# Mulank calculation route
@app.get("/mulank")
def mulank(dob: str):
    """
    Example: /mulank?dob=2005-08-15
    """
    try:
        date_obj = datetime.strptime(dob, "%Y-%m-%d")
    except ValueError:
        return {"error": "Invalid date format. Use YYYY-MM-DD."}

    # Mulank = sum of digits of day
    day = date_obj.day
    mulank = sum(int(d) for d in str(day))
    while mulank > 9:
        mulank = sum(int(d) for d in str(mulank))

    # Example lucky number formula
    lucky_number = mulank + 7

    return {"dob": dob, "mulank": mulank, "lucky_number": lucky_number}


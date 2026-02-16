# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

# Initialize FastAPI app
app = FastAPI()

# Enable CORS for all origins (so frontend can access the API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # "*" means all domains; in production, replace with your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root route to avoid 404
@app.get("/")
def home():
    return {"message": "Welcome to NUMs API! Use /mulank endpoint with your DOB in YYYY-MM-DD format."}

# Mulank endpoint
@app.get("/mulank")
def mulank(dob: str):
    """
    Example usage: /mulank?dob=2005-08-15
    """
    try:
        date_obj = datetime.strptime(dob, "%Y-%m-%d")
    except ValueError:
        return {"error": "Invalid date format. Use YYYY-MM-DD."}

    # Calculate Mulank: sum of digits of day until single digit
    day = date_obj.day
    mulank = sum(int(d) for d in str(day))
    while mulank > 9:
        mulank = sum(int(d) for d in str(mulank))

    # Example lucky number formula
    lucky_number = mulank + 7

    return {"dob": dob, "mulank": mulank, "lucky_number": lucky_number}

from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# Input model for date of birth
class DOB(BaseModel):
    dob: str  # format: YYYY-MM-DD

# Home route (for testing)
@app.get("/")
def home():
    return {"message": "Welcome to NUMs API! Use /mulank endpoint with your DOB."}

# Mulank route
@app.post("/mulank")
def get_mulank(data: DOB):
    try:
        dob = datetime.strptime(data.dob, "%Y-%m-%d")
        # Mulank = sum of digits of date until 1-9
        total = dob.day
        while total > 9:
            total = sum(int(d) for d in str(total))
        mulank = total

        # Example: lucky numbers for each mulank
        lucky_numbers = {
            1: [1, 10, 19, 28],
            2: [2, 11, 20, 29],
            3: [3, 12, 21, 30],
            4: [4, 13, 22],
            5: [5, 14, 23, 32],
            6: [6, 15, 24],
            7: [7, 16, 25],
            8: [8, 17, 26],
            9: [9, 18, 27]
        }

        return {
            "mulank": mulank,
            "lucky_numbers": lucky_numbers.get(mulank, [])
        }

    except Exception as e:
        return {"error": str(e)}


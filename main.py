from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# -------- Request Model --------
class DOBRequest(BaseModel):
    dob: str   # format DD-MM-YYYY

# -------- Numerology Logic --------
def calculate_mulank(day):
    while day > 9:
        day = sum(int(d) for d in str(day))
    return day

def get_lucky_numbers(mulank):
    lucky_map = {
        1: [1, 10, 19, 28, 37, 46],
        2: [2, 11, 20, 29, 38, 47],
        3: [3, 12, 21, 30, 39, 48],
        4: [4, 13, 22, 31, 40, 49],
        5: [5, 14, 23, 32, 41, 50],
        6: [6, 15, 24, 33, 42, 51],
        7: [7, 16, 25, 34, 43, 52],
        8: [8, 17, 26, 35, 44, 53],
        9: [9, 18, 27, 36, 45, 54],
    }
    return lucky_map[mulank]

# -------- API Route --------
@app.post("/lucky-number")
def lucky_number(request: DOBRequest):
    try:
        day = int(request.dob.split("-")[0])
        mulank = calculate_mulank(day)
        lucky_numbers = get_lucky_numbers(mulank)

        return {
            "dob": request.dob,
            "mulank": mulank,
            "lucky_numbers": lucky_numbers
        }

    except:
        return {"error": "Invalid DOB format. Use DD-MM-YYYY"}

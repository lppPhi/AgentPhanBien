from fastapi import FastAPI
from pydantic import BaseModel
from agents import debater_a, debater_b, judge
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DebateTopic(BaseModel):
    topic: str

@app.post("/debate")
def run_debate(data: DebateTopic):
    a1 = debater_a(data.topic)
    b1 = debater_b(data.topic, rebuttal=a1)
    a2 = debater_a(data.topic, rebuttal=b1)
    b2 = debater_b(data.topic, rebuttal=a2)

    full_debate = f"""
Debater A: {a1}

Debater B: {b1}

Debater A (Round 2): {a2}

Debater B (Round 2): {b2}
    """

    result = judge(full_debate)

    return {
        "a1": a1,
        "b1": b1,
        "a2": a2,
        "b2": b2,
        "result": result
    }

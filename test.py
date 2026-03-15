from dotenv import load_dotenv
from crew import stock_crew
import os

os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"

load_dotenv()

def run(stock: str):
    result = stock_crew.kickoff(inputs={"stock": stock})
    print(result.raw)

if __name__ == "__main__":
    run("APPLE")
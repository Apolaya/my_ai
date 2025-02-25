import os
import pprint 
from openai import OpenAI
import telemetry_reader
from dotenv import load_dotenv
import gui 
from ir_telemetry import ir_telemetry



simpleGui = gui.SimpleGui()
load_dotenv()
api_key = os.getenv("API_KEY_AI")
client = OpenAI(api_key=api_key)

simpleGui = gui.SimpleGui()
running: bool = True

def runApp(running):
    simpleGui = gui.SimpleGui()
    while running:
        # Any event handling logic should go here
        # Replace with actual event handling logic
        student_prompts = makeStudent()
        base_prompts = makeBase()
        print("delete check ")

        # GET AND PRINT THE TEXT FILES GIVEN TO CHAT GPT
        #stream = callGPT(makeStudent, makeBase())
        #show_GPT_results(stream)

        break
        

    # Needs a break clause becasue this is a infinite loop. 



# 1st racer
# Uses another class to read the file to retur a string form so i can send to the OPEN AI , messages.
def make_ibt_base():
    ibt_base = ir_telemetry.my_ir('/Users/apolaya/Library/Mobile Documents/com~apple~CloudDocs/Telemetry /raygr22_rudskogen 2024-10-21 00-20-59.ibt')

    base_stream = ibt_base.get_speed_array()
    ibt_base.close_ibt()
    return base_stream
def make_ibt_student():
    ibt_student = ir_telemetry.my_ir("/Users/apolaya/Library/Mobile Documents/com~apple~CloudDocs/Telemetry /raygr22_rudskogen 2024-10-21 00-26-58.ibt")

    student_stream = ibt_student.get_speed_array()
    ibt_student.close_ibt()
    return student_stream
    
def makeStudent()-> str:
    tr = telemetry_reader.telemetry_reader(
        "/Users/apolaya/Documents/my_ai/telemetry_data/Garage 61 - GR Buttkicker Cup - Fixed - Race - Export - 2024-09-13-18-29-30.xlsx"
    )
    prompts = tr.extract()
    return prompts

# second racer
def makeBase() -> str:
    tr_2 = telemetry_reader.telemetry_reader(
        "/Users/apolaya/Documents/my_ai/telemetry_data/Opponent_times.xlsx"
    )
    prompts_2 = tr_2.extract()
    return prompts_2


# this is senting the laptimes for each driver adn comparing which is faster
def callGPT(prompts, prompts_2):
    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a Sim racing coach focusing on i-racing. You must taken the lap times of Base Racer and compare it to student This is meant to improve the student. ",
            },
            {"role": "system", "name": "Student", "content": prompts},
            {"role": "system", "name": "BaseRacer", "content": prompts_2},
        ],
        stream=True,
    )
    return stream

def show_GPT_results(stream):
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")



def main():
    student_stream = make_ibt_student() 
    base_stream = make_ibt_base()
    

    stream_results = callGPT(student_stream, base_stream)
    show_GPT_results(stream_results)
    
    
    # Get telemetry data
    

if __name__ == "__main__":
    main()

import os
from pathlib import Path 
from dotenv import load_dotenv
from pydantic import BaseModel
from groq import Groq
import json

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key not found")

client= Groq(api_key=my_api_key)

model = "openai/gpt-oss-120b"
role="user"

class JobDescription(BaseModel):
    Role:str
    Required_skills:list[str]
    Prefferd_skills:list[str]
    Min_experience:int | None
    Education:str
    responsibility:str
class Experience(BaseModel):
    Company:str | None=None
    Role:str | None=None
    Duration:str | None=None
    Description:str | None=None
    Skills:list[str] = []

class Resume(BaseModel):
    Name:str | None=None
    Email:str | None=None
    Phone:int | None=None
    Total_experience_Year:float | None=None
    Skills:list[str] = []
    Experience=list[Experience] = []
    Projects:list[str] = []
    Certifications:list[str] = []

JobDescription_schema = JobDescription.model_json_schema()
Experience_schema =Experience.model_json_schema()
Resume_schema = Resume.model_json_schema()

Job_Description_str='''Amazon is looking for a Software Development Engineer I (SDE I) responsible for designing, developing, testing, 
debugging, deploying, and maintaining scalable software applications and services. Required skills include proficiency in
at least one programming language such as Java, Python, or C++, strong knowledge of data structures and algorithms, object-oriented programming, 
problem-solving, and computer science fundamentals. Preferred skills include experience with SQL or NoSQL databases, REST APIs, AWS cloud services,
Git, automated testing, and distributed systems. Educational requirements typically include a Bachelor's degree in Computer Science, Information Technology,
Computer Engineering, or a related field, or equivalent qualifications where accepted. Minimum experience varies by job posting; entry-level and 
university-hiring roles may accept fresh graduates, while some SDE I openings require one or more years of professional software development experience. Candidates should demonstrate
analytical thinking, communication, teamwork, ownership, attention to code quality, and a willingness to learn
and follow Amazon's Leadership Principles.'''
system_prompt=f'''
You are an expert HR assistant.
Your job is to analyze job descriptions and extract
structured information from them.
Return ONLY valid JSON matching this schema:
{JobDescription_schema}
IMPORTANT:
Do NOT return the schema itself.
Do NOT return fields like "properties", "title" or "type".
Fill the schema with actual information extracted from the job description.

If minimum experience is not mentioned, return null.
If information for a list is missing, return an empty list.
Do not invent information.
'''

user_prompt = f"""
Analyze the following job description:
{Job_Description_str}
"""

message_system = {
    "role": "system",
    "content": system_prompt
}

message_user = {
    "role": "user",
    "content": user_prompt
}

response_format = {
    "type": "json_object"
}

messages = [message_system, message_user]
response = client.chat.completions.create(model=model,messages=messages,response_format=response_format)
answer = response.choices[0].message.content
raw_json = answer
jobdata = json.loads(raw_json)
Job_D = JobDescription(**jobdata)




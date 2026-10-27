import os
from pathlib import Path 
from dotenv import load_dotenv
from pydantic import BaseModel
from groq import Groq

class JobDescription(BaseModel):
    Role:str
    Required_skills:list[str]
    Prefferd_skills:list[str]
    Min_experience:int
    Education:str
    responsibility:str
class Experience(BaseModel):
    Company:str
    Role:str
    Duration:str
    Description:str
    Skills:list[str]

class Resume(BaseModel):
    Name:str
    Email:str
    Phone:int
    Total_experience_Year:int
    Skills:list[str]
    Experience=list[Experience]
    Projects:list[str]
    Certifications:list[str]

JobDescription_schema = JobDescription.model_json_schema()
Experience_schema =Experience.model_json_schema()
Resume_schema = Resume.model_json_schema()

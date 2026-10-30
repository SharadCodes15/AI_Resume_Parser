from pydantic import BaseModel

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
    Experiences:list[Experience] = []
    Projects:list[str] = []
    Certifications:list[str] = []

class MatchResult(BaseModel):
    score:float
    details:dict
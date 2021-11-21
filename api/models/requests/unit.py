from typing import Optional

from pydantic.main import BaseModel


class Unit(BaseModel):
    lesonIdCompleted: Optional[str] = None
    examCompleted: Optional[bool] = None
    unitCompleted: Optional[bool] = None
    allExercisesExam: Optional[bool] = None
    allExercisesLesson: Optional[bool] = None
    time: Optional[int] = None
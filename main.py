from dataclasses import Field

from pydantic import  BaseModel, fields
from typing import  Optional ,List

class NewsArticle(BaseModel):
    title:str = Field(name='Article Title', description='Title of the article')
    url: str = Field(name='Article URL', description='link to Article')
    summary: Optional[str]= Field(name='Article Summary',description='summary of th Article if available')

class SearchResults(BaseModel):
    article:List[NewsArticle]


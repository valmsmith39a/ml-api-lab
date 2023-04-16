from typing import List
from pydantic import BaseModel 

class UserConversationRequest(BaseModel):
	model: str
	messages: List[Message]

class Message(BaseModel):
	role: str
	content: str 
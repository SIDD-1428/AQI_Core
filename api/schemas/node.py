from pydantic import BaseModel

class NodeListResponse(BaseModel):
    nodes:list[str]
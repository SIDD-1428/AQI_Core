from fastapi import APIRouter
router=APIRouter()

@router.get("/node/list")
def node_list():
    return {
        "message":"Node API is working"
    }
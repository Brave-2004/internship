from fastapi import APIRouter, Depends
from dependencies import get_current_user
from schemas.schema import NotificationCreate
from services import notification_service

router = APIRouter(
    prefix="/notification",
    tags=["notification"],
)


@router.post("/create")
async def notificationCreate(
    data: NotificationCreate,
    current_user: dict = Depends(get_current_user)
):
    return notification_service.notificationCreate(data)


@router.get("/list/{user_id}")
async def notificationList(
    user_id: int,
    current_user: dict = Depends(get_current_user)
):
    return notification_service.notificationList(user_id)


@router.put("/markRead/{notification_id}")
async def notificationMarkRead(
    notification_id: str,
    current_user: dict = Depends(get_current_user)
):
    return notification_service.notificationMarkRead(notification_id)


@router.delete("/delete/{notification_id}")
async def notificationDelete(
    notification_id: str,
    current_user: dict = Depends(get_current_user)
):
    return notification_service.notificationDelete(notification_id)

from typing import List

from fastapi import APIRouter, HTTPException
from schemas import (
    StandardOutput,
    UserCreatePayload,
    ErrorOutput,
    UserListOutput,
    AlterUserPayload,
)
from services import UserService

user_router = APIRouter(prefix="/user", responses={400: {"model": ErrorOutput}})


@user_router.post(
    "/create",
    description="Create user route",
    response_model=StandardOutput,
)
async def user_create(user_input: UserCreatePayload):
    try:
        await UserService.create_user(
            name=user_input.name,
            phone_number=user_input.phone_number,
            email=user_input.email,
            cpf=user_input.cpf,
        )
        return StandardOutput(message="Created")
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@user_router.delete(
    "/delete/{user_id}",
    description="Delete user route",
    response_model=StandardOutput,
)
async def user_delete(user_id: int):
    try:
        await UserService.delete_user(user_id)
        return StandardOutput(message="Deleted")
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@user_router.get(
    "/list",
    description="List users route",
    response_model=List[UserListOutput],
)
async def user_list():
    try:
        return await UserService.list_user()
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@user_router.get(
    "/get_by_id/{user_id}",
    description="Get user by id route",
    response_model=UserListOutput,
)
async def user_get_by_id(user_id: int):
    try:
        return await UserService.get_by_id(user_id)
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@user_router.put(
    "/alter_user/{user_id}",
    description="Alter user route",
    response_model=StandardOutput,
)
async def alter_user(user_id: int, user_input: AlterUserPayload):
    try:
        await UserService.alter_user(
            user_id=user_id,
            name=user_input.name,
            phone_number=user_input.phone_number,
            email=user_input.email,
            cpf=user_input.cpf,
        )
        return StandardOutput(message="Done")
    except Exception as error:
        raise HTTPException(400, detail=str(error))

from models import User


async def Create(user_id: int, first_name: str, last_name: str = "") -> User:
    user = User(id=user_id, first_name=first_name, last_name=last_name)
    await user.insert()
    return user


async def Get(user_id: int) -> User | None:
    return await User.find_one({"_id": user_id})


async def Update(user_id: int, **kwargs) -> User | None:
    user = await Get(user_id)
    if user:
        for key, value in kwargs.items():
            setattr(user, key, value)
        await user.save()
    return user


async def Delete(user_id: int) -> User | None:
    user = await Get(user_id)
    if user:
        await user.delete()
    return user

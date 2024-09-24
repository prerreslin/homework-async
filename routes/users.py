from .. import app
from ..db import User,Session
from sqlalchemy import select


@app.get("/get_users")
async def get_users():
    with Session.begin() as session:
        users = session.scalars(select(User)).all()
        if not users:
            return {"Error": "No users in database"}
        
        user_list = [{"id": user.id, "name": user.name} for user in users]
        # не хочу морочится с model_validate
        return user_list
    
@app.post("/add_user")
async def add_user(name:str):
    with Session.begin() as session:
        user = session.scalar(select(User).where(User.name == name))
        if user:
            return {"Error: ":"The user already exists"}
        new_user = User(name=name)
        session.add(new_user)
        session.commit()
        return {"Output: ":"User successfully created"}
    
@app.delete("/delete_user")
async def delete_user(name:str):
    with Session.begin() as session:
        user = session.scalar(select(User).where(User.name == name))
        if not user:
            return {"Error: ":"User not found"}
        session.delete(user)
        return {"Output: ":"User successfully deleted"}

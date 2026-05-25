from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.user import User
from app.services.auth_service import verify_password
from app.api.deps import get_db
from app.schemas.auth import RegisterSchema



router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register")
async def register(user: RegisterSchema, db: AsyncSession = Depends(get_db)):
    # Check if the email already exists
    result = await db.execute(select(User).where(User.email == user.email))
    existing_user = result.scalars().first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    # Create a new user
    new_user = User(
        name=user.name,
        email=user.email,
        password=user.password  # In a real application, make sure to hash the password
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return {"message": "User registered successfully", "user_id": new_user.id}

@router.post("/login")
async def login(user: RegisterSchema, db: AsyncSession = Depends(get_db)):
    # Check if the user exists
    result = await db.execute(select(User).where(User.email == user.email))
    existing_user = result.scalars().first()
    if not existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid email or password")

    # Verify the password
    if not verify_password(user.password, existing_user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid email or password")

    return {"message": "Login successful", "user_id": existing_user.id}

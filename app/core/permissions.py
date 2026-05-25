from fastapi import Depends, HTTPException
from app.api.deps import get_current_user

def permission_required(permission: str):

    def checker(current_user=Depends(get_current_user)):

        user_permissions = [
            "user_create",
            "user_update"
        ]

        if permission not in user_permissions:
            raise HTTPException(
                status_code=403,
                detail="Permission denied"
            )

        return current_user

    return checker
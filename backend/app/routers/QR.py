from typing import List
from urllib import response
from fastapi import APIRouter, Depends, HTTPException, status, Header
from jose.exceptions import JWTError
from sqlalchemy.orm import Session

from app import schemas
from app.database import get_session
from app.errors import (
    INVALID_CREDENTIALS,
    QR_NOT_FOUND_ERROR,
    TOKEN_AUTHENTICATION_FAILED,
    InvalidAuthenticationTokenError,
    InvalidCredentialsError,
    MissingAuthenticationTokenError,
    QRNotFoundError,
)

from app.services import QR
from app.token import get_user_id

router = APIRouter(tags=["QR"], prefix="/QR")


@router.post("", status_code=status.HTTP_201_CREATED, response_model=schemas.QRCreateOut)
def create_QR(
    request: schemas.QRCreateIn,
    token: str = Header(None),
    session: Session = Depends(get_session),
):
    """Creates and stores a new user in a database

    :param request: The request body for users to input their new account credentials
    :type: schemas.UserIn
    :param session: The database that user's credentials are uploaded to
    :type session: Session
    :returns: The user's username
    :rtype: schemas.UserOut
    :raises HTTPException: If username validation fails
    """
    try:
        user_id = get_user_id(token)
    except MissingAuthenticationTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": MissingAuthenticationTokenError},
        )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": TOKEN_AUTHENTICATION_FAILED},
        )
    except InvalidAuthenticationTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": TOKEN_AUTHENTICATION_FAILED},
        )

    return QR.create_QR(user_id, request, session)


@router.get("", status_code=status.HTTP_200_OK, response_model=List[schemas.QRCreateOut])
def get_all_QRs(token: str = Header(None), session: Session = Depends(get_session)):
    """Creates and stores a new user in a database

    :param request: The request body for users to input their new account credentials
    :type: schemas.UserIn
    :param session: The database that user's credentials are uploaded to
    :type session: Session
    :returns: The user's username
    :rtype: schemas.UserOut
    :raises HTTPException: If username validation fails
    """
    try:
        user_id = get_user_id(token)
    except MissingAuthenticationTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": MissingAuthenticationTokenError},
        )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": TOKEN_AUTHENTICATION_FAILED},
        )
    except InvalidAuthenticationTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": TOKEN_AUTHENTICATION_FAILED},
        )

    try:
        return QR.get_all_QRs(user_id, session)
    except QRNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error": QR_NOT_FOUND_ERROR},
        )


@router.get(
    "/{QR_id}", status_code=status.HTTP_200_OK, response_model=schemas.QRCreateOut
)
def get_QR(
    QR_id: int, token: str = Header(None), session: Session = Depends(get_session)
):
    """Creates and stores a new user in a database

    :param request: The request body for users to input their new account credentials
    :type: schemas.UserIn
    :param session: The database that user's credentials are uploaded to
    :type session: Session
    :returns: The user's username
    :rtype: schemas.UserOut
    :raises HTTPException: If username validation fails
    """
    try:
        user_id = get_user_id(token)
    except MissingAuthenticationTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": MissingAuthenticationTokenError},
        )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": TOKEN_AUTHENTICATION_FAILED},
        )
    except InvalidAuthenticationTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": TOKEN_AUTHENTICATION_FAILED},
        )

    try:
        return QR.get_QR(session, user_id, QR_id)
    except QRNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error": QR_NOT_FOUND_ERROR},
        )
    except InvalidCredentialsError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": INVALID_CREDENTIALS},
        )


@router.delete("", status_code=status.HTTP_200_OK, response_model=None)
def delete_QR(
    request: schemas.QRDeleteIn,
    token: str = Header(None),
    session: Session = Depends(get_session),
):
    """Creates and stores a new user in a database

    :param request: The request body for users to input their new account credentials
    :type: schemas.UserIn
    :param session: The database that user's credentials are uploaded to
    :type session: Session
    :returns: The user's username
    :rtype: schemas.UserOut
    :raises HTTPException: If username validation fails
    """
    try:
        user_id = get_user_id(token)
    except MissingAuthenticationTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": MissingAuthenticationTokenError},
        )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": TOKEN_AUTHENTICATION_FAILED},
        )
    except InvalidAuthenticationTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": TOKEN_AUTHENTICATION_FAILED},
        )

    try:
        return QR.delete_QR(request.QR_id, user_id, session)
    except QRNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error": QRNotFoundError},
        )
    except InvalidCredentialsError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": INVALID_CREDENTIALS},
        )

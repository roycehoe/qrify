from os import link
from time import time

from sqlalchemy.orm.session import Session
from app import models, schemas
from app.errors import InvalidCredentialsError, QRNotFoundError
from app.repository.QR import QRRepository


def create_QR(
    user_id: int, request: schemas.QRCreateIn, session: Session
) -> models.QR:
    new_QR = models.QR(
        user_id=user_id,
        created_at=time(),
        title=request.title,
        link=request.link,
    )
    try:
        QRRepository(session).save(new_QR)
    except Exception:
        raise Exception
    return new_QR


def __is_QR_owner(QR_id: int, user_id: int, session: Session) -> bool:
    user_QRs = QRRepository(session).get_all(user_id)
    return QR_id in [user_QR.id for user_QR in user_QRs]


def get_QR(session: Session, user_id: int, QR_id: int) -> list[models.QR]:
    """Creates and stores a new user in a database

    :param request: The request body for users to input their new account credentials
    :type: schemas.UserIn
    :param session: The database that user's credentials are uploaded to
    :type session: Session
    :returns: Full details of the created user
    :rtype: models.User
    raises UsernameNotUniqueError: if username in request.username is already taken
    in the session database
    """

    if not __is_QR_owner(QR_id, user_id, session):
        raise InvalidCredentialsError
    try:
        QR = QRRepository(session).get(QR_id)
        return QR
    except QRNotFoundError:
        raise QRNotFoundError


def get_all_QRs(user_id: int, session: Session) -> list[models.QR]:
    """Creates and stores a new user in a database

    :param request: The request body for users to input their new account credentials
    :type: schemas.UserIn
    :param session: The database that user's credentials are uploaded to
    :type session: Session
    :returns: Full details of the created user
    :rtype: models.User
    raises UsernameNotUniqueError: if username in request.username is already taken
    in the session database
    """

    try:
        QR = QRRepository(session).get_all(user_id)
        return QR
    except QRNotFoundError:
        raise QRNotFoundError


def delete_QR(QR_id: int, user_id: int, session: Session) -> None:
    if not __is_QR_owner(QR_id, user_id, session):
        raise InvalidCredentialsError

    try:
        return QRRepository(session).delete(QR_id)
    except QRNotFoundError:
        raise QRNotFoundError

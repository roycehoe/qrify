from sqlalchemy.exc import IntegrityError, InvalidRequestError
from sqlalchemy.orm.session import Session

from app import models
# from app.errors import TimerNotFoundError


class QRRepository:
    def __init__(self, session: Session):
        self.session = session

    def save(self, QR: models.QR) -> models.QR:
        try:
            self.session.add(QR)
            self.session.commit()
            return QR

        except IntegrityError:
            pass

    def get(self, QR_id: int) -> models.QR:
        if QR := (
            self.session.query(models.QR).filter(models.QR.id== QR_id).first()
        ):
            return QR_id
        # raise TimerNotFoundError

    def get_all(self, user_id: str) -> list[models.QR]:
        if QR := (
            self.session.query(models.QR).filter(models.QR.user_id == user_id)
        ).all():
            return QR
        # raise TimerNotFoundError

    def delete(self, QR_id: int) -> None:
        if QR := self.session.query(models.QR).filter(
            models.QR.id == QR_id
        ):
            QR.delete()
            self.session.commit()
            return
        # raise TimerNotFoundError
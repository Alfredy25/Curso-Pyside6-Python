from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import sessionmaker, Session

from course.alfredo.pyside.kardex.app.entity.operation import Operation
from course.alfredo.pyside.kardex.app.repository.operation_repository import (
    OperationRepository,
)


class OperationRepositoryImpl(OperationRepository):

    def __init__(self, session_factory: sessionmaker[Session]):
        self._session_factory = session_factory

    def find_by_id(self, operation_id: int) -> Optional[Operation]:
        with self._session_factory() as session:
            return session.get(Operation, operation_id)

    def find_all(self, offset: int = 0, limit: int = 100) -> list[Operation]:
        with self._session_factory() as session:

            statement = (
                select(Operation)
                .order_by(Operation.id)
                .offset(offset)
                .limit(limit)
            )
            result = session.execute(statement)

            return list(result.scalars().all())

    def save(self, operation: Operation) -> Operation:
        with self._session_factory() as session:
            try:
                # Insert si no se tiene un id en el objeto Operation pasado a guardar es decir es nuevo
                if not getattr(operation, 'id', None):
                    session.add(operation)
                    session.commit()
                    session.refresh(operation)
                    return operation
                # UPDATE si existe id entonces la condicion anterior es falsa y pasa a una actualizacion
                managed_operation = session.merge(operation)
                session.commit()
                session.refresh(managed_operation)
                return managed_operation

            except Exception:
                session.rollback()
                raise

    def delete(self, operation_id: int) -> bool:
        with self._session_factory() as session:
            try:
                operation = session.get(Operation, operation_id)

                if operation is None:
                    return False

                session.delete(operation)
                session.commit()

                return True

            except Exception:
                session.rollback()
                raise
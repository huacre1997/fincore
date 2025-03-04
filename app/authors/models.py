from app.books.models import Book
from app.commons.database import Base, TimestampMixin
from sqlalchemy.orm import Mapped, relationship


class Author(TimestampMixin, Base):
    name: str
    last_name: str
    books: Mapped[list["Book"]] = relationship(
        back_populates="author",
        cascade="all, delete",
        passive_deletes=True,
    )

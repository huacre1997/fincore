from sqlalchemy import ForeignKey
from app.authors.models import Author
from app.commons.database import Base, TimestampMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Book(TimestampMixin, Base):
    title: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("author.id", ondelete="CASCADE"))
    author: Mapped[Author] = relationship("Author", back_populates="books")

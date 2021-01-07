from .db import db


class Type(db.Model):
    __tablename__ = "types"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False, unique=True)

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
        }

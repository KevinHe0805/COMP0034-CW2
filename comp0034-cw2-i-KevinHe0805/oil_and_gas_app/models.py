from oil_and_gas_app import db
from flask_login import UserMixin
from oil_and_gas_app import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class Source(db.Model):
    """Source class"""

    __tablename__ = "oil_and_gas"
    rowid = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Text, nullable=False)
    Date = db.Column(db.Integer, nullable=False)
    Price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        """

        :returns str
        """
        clsname = self.__class__.__name__
        return f"{clsname}: <{self.type}, {self.Date}, {self.Price}>"


class User(db.Model, UserMixin):

    __tablename__ = "user"

    def get_id(self):
        return self.id

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)

    def __repr__(self):
        """
        Returns the attributes of a User as a string, except for the password
        :returns str
        """
        clsname = self.__class__.__name__
        return f"{clsname}: <{self.id}, {self.email}>"

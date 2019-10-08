from flask_login import UserMixin
from app import login

# At this point, the database should be implemented, but for the hackathon
# purposes I thought is too much, and it might cause additional errors,
# in the future work. There was a need for only one user to be working on.


class User(UserMixin):
    username = "Admin"
    password = "123"
    id = 0

# There is only one user "Admin". In the bigger scale implementation,
# function load_user should query the database for the user's
# information by the given id value.
# Use "return Use User.query.get(int(id))" instead of "return User()"


@login.user_loader
def load_user(id):
    return User()

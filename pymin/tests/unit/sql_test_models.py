import unittest
from datetime import datetime

from pymin import app, db
from pymin.models import User, Post


# TODO: create proper test config for alchemy testing
class TestParticipant(unittest.TestCase):
    def setUp(self):
        app.config.from_object('pymin.config.DevConfig')
        db.session.close()
        db.drop_all()
        db.create_all()

    def test_lookup(self):
        user = User('test', 'test@test.com')
        db.session.add(user)
        post = Post('body', 1, datetime.utcnow())
        db.session.add(post)
        db.session.commit()
        users = User.query.all()
        posts = Post.query.all()
        assert user in users
        assert post in posts

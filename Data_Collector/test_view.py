
import os
import unittest

from Data_Collector import app, db

basedir = os.path.abspath(os.path.dirname(__file__))


class BasicTests(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.db')
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        pass

    def test_home(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_otp(self):
        response = self.app.get('/otp', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_data(self):
        response = self.app.get('/data', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_search(self):
        response = self.app.get('/search', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_main(self):
        return self.app.post('/result', data=dict(username="tester", password="secretonly",
                                                  email="test@test.com", phone="0123456789", gender="M"))


if __name__ == "__main__":
    unittest.main()

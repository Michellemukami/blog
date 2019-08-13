import unittest
from app.models import Blog, User
from app import db

class BlogTest(unittest.TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_Blog = Blog("This is a new pitch")


    def test_check_instance_variables(self):
        self.assertEquals(self.new_Blog.comments,"This is a new pitch")
      
    def test_save_pitch(self):
        """
        To tests on whether pitches are being saved
        """
        self.new_blog.save_blog()
        self.assertTrue(len(Blog.query.all())>0)
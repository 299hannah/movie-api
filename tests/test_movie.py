import unittest
from app.models import Movie
from app.models import movie
Movie = movie.Movie

class MovieTest(unittest.TestCase):
    '''

    Test Class to test the behavior of the movie class
    '''
    def setUp(self):
        '''
        set up method that will run before every test
        '''
        self.new_movie = Movie(1234,'Python must be very crazy','A thrilling series','https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie,Movie))

if __name__ == '__main__':
    unittest.main()

from django.test import TestCase, Client

# Create your tests here.
from films.models import Movie


class TestMovieViewSet(TestCase):
    def setUp(self) -> None:
        self.movie = Movie.objects.create(name='Test name', year='2002-01-02', imdb=6, genre='action')
        self.movie = Movie.objects.create(name='Test name 2', year='2002-01-02', imdb=10, genre='drama')
        self.client = Client()

    def test_get_movies(self):
        response = self.client.get("/movies/")
        data = response.data

        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data), 1)
        self.assertIsNotNone(data[0]['id'])
        self.assertEquals(data[0]['name'], 'Test name')
        self.assertEquals(data[0]['year'], '2002-01-02')
        self.assertEquals(data[0]['imdb'], 8)
        self.assertEquals(data[0]['genre'], 'action')

    def test_search(self):
        response = self.client.get('/movies/?search=Test')
        data = response.data

        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data), 1)
        self.assertEquals(data[0]['name'], 'Test name')

    def test_ordering(self):
        response = self.client.get('/movies/?ordering=-imdb')
        data = response.data

        self.assertEquals(data[0]['name'], 'Test name 2')

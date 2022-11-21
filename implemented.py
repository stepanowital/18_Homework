from dao.movie import MovieDAO
from dao.director import DirectorDAO
from dao.genre import GenreDAO
from setup_db import db
from service.movie import MovieService
from service.director import DirectorService
from service.genre import GenreService

movie_dao = MovieDAO(session=db.session)
movie_service = MovieService(dao=movie_dao)

director_dao = DirectorDAO(session=db.session)
director_service = DirectorService(dao=director_dao)

genre_dao = GenreDAO(session=db.session)
genre_service = GenreService(dao=genre_dao)

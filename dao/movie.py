from dao.model.movie import Movie


class MovieDAO:
	def __init__(self, session):
		self.session = session

	def get_one(self, uid):
		return self.session.query(Movie).get(uid)

	def get_all(self):
		return self.session.query(Movie).all()

	def get_by_director_id(self, did):
		return self.session.query(Movie).filter(Movie.director.id == did).all()

	def get_by_genre_id(self, gid):
		return self.session.query(Movie).filter(Movie.genre.id == gid).all()

	def get_by_year(self, year):
		return self.session.query(Movie).filter(Movie.year == year).all()

	def create(self, data):
		new_movie = Movie(**data)
		self.session.add(new_movie)
		self.session.commit()

		return new_movie

	def update(self, movie):
		self.session.add(movie)
		self.session.commit()

		return movie

	def delete(self, uid):
		movie = self.get_one(uid)

		self.session.delete(movie)
		self.session.commit()

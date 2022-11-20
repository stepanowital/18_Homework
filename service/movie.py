from dao.movie import MovieDAO


class MovieService:
	def __init__(self, dao: MovieDAO):
		self.dao = dao

	def get_one(self, uid):
		return self.dao.get_one(uid)

	def get_all(self):
		return self.dao.get_all()

	def get_by_director_id(self, uid):
		return self.dao.get_by_director_id(uid)

	def get_by_genre_id(self, uid):
		return self.dao.get_by_genre_id(uid)

	def get_by_year(self, year):
		return self.dao.get_by_year(year)

	def create(self, data):
		return self.dao.create(data)

	def update(self, data):
		movie = self.get_one(data.get("id"))

		movie.title = data.get("title")
		movie.description = data.get("description")
		movie.trailer = data.get("trailer")
		movie.year = data.get("year")
		movie.rating = data.get("rating")
		movie.genre_id = data.get("genre_id")
		movie.director_id = data.get("director_id")

		self.dao.update(movie)

	def delete(self, uid):
		self.dao.delete(uid)

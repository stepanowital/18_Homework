from dao.genre import GenreDAO


class GenreService:
	def __init__(self, dao: GenreDAO):
		self.dao = dao

	def get_one(self, uid):
		return self.dao.get_one(uid)

	def get_all(self):
		return self.dao.get_all()

	def create(self, data):
		return self.dao.create(data)

	def update(self, data):
		genre = self.get_one(data.get("id"))

		genre.name = data.get("name")

		self.dao.update(genre)

	def delete(self, uid):
		self.dao.delete(uid)

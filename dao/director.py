from dao.model.director import Director


class DirectorDAO:
	def __init__(self, session):
		self.session = session

	def get_one(self, uid):
		return self.session.query(Director).get(uid)

	def get_all(self):
		return self.session.query(Director).all()

	def create(self, data):
		new_director = Director(**data)
		self.session.add(new_director)
		self.session.commit()

		return new_director

	def update(self, director):
		self.session.add(director)
		self.session.commit()

		return director

	def delete(self, uid):
		director = self.get_one(uid)

		self.session.delete(director)
		self.session.commit()

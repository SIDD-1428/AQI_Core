from configuration.standard_repository import StandardRepository

class StandardManager:
    def __init__(self, session):
        self.repository = StandardRepository(session)

    def save_standard(self, standard):
        self.repository.save(standard)

    def get_active_standard(self):
        return self.repository.get_active()

    def get_all_standards(self):
        return self.repository.get_all()
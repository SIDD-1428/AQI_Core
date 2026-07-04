from configuration.standard_models import AQIStandard

class StandardRepository:

    def __init__(self, session):
        self.session = session

    def save(self, standard):
        self.session.add(standard)
        self.session.commit()

    def get_active(self):
        return (
            self.session
            .query(AQIStandard)
            .filter_by(active=True)
            .first()
        )

    def get_all(self):
        return (
            self.session
            .query(AQIStandard)
            .all()
        )
from configuration.models import SystemSetting

class ConfigurationRepository:
    def __init__(self, session):
        self.session=session
    
    def get(self, key):
        return(
            self.session.query(SystemSetting).filter_by(key=key).first()
        )

    def save(self,setting):
        self.session.add(setting)
        self.session.commit()
    
    def get_all(self):
        return self.session.query(SystemSetting).all()
    
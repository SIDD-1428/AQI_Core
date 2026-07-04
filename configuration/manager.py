from configuration.repository import ConfigurationRepository
class ConfigurationManager:
    def __init__(self,session):
        self.repository=ConfigurationRepository(session)
    
    def get_setting(self,key):
        return self.repository.get(key)
    
    def get_all_setting(self):
        return self.repository.get_all()
    
    def save_setting(self,setting):
        self.repository.save(setting)
from database.aqi_result_models import AQIResultModel
class AQIResultRepository:
    def __init__(self,session):
        self.session=session
    
    def save(self,result):
        self.session.add(result)
        self.session.commit()
        self.session.refresh(result)
        return result
    
    def latest(self):
        return(
            self.session.query(AQIResultModel)
            .order_by(AQIResultModel.id.desc())
            .first()
        )

    def get_all(self,limit):
        return(
             self.session.query(AQIResultModel)
             .order_by(AQIResultModel.id.desc())
             .limit(limit)
             .all()
        )
    
    def get_latest_by_node(self,node):
        return(
            self.session.query(AQIResultModel)
            .filter(AQIResultModel.node==node)
            .order_by(AQIResultModel.id.desc())
            .first()
        )
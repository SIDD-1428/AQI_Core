from parser.entry_point.context import ProcessingContext

class PacketQualityAnalyzer:
    "Stage 6 - sumary"
    @staticmethod 
    def get_grade(score:int):
        if score>=95:
            return "A+","excellent"
        
        if score>=90:
            return "A","Very Good"
        
        if score>=80:
            return "B","Good"
        
        if score>=70:
            return "C","Fair"
        
        if score>=60:
            return "D","Poor"
        
        return "F","Critical"
    

    def process(self,context:ProcessingContext) ->ProcessingContext:
        score=max(0,min(100,context.quality_score))
        grade, status=self.get_grade(score)
        context.metadata["quality"]={
            "score":score,
            "grade":grade,
            "status":status,
            "warnings":len(context.warnings),
            "errors":len(context.errors)
        }

        return context
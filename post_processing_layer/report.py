from dataclasses import dataclass, field

@dataclass
class ReportEntry:
    stage:str
    status:str
    message:str


@dataclass
class PostProcessingReport:
    entries: list[ReportEntry]=field(default_factory=list)

    def add(self,stage:str,status:str,message: str):
        self.entries.append(
            ReportEntry(
                stage=stage,
                status=status,
                message=message
            )
        )
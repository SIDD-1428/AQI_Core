import time
from parser.entry_point.context import ProcessingContext
from parser.report import ProcessingReport
from parser.entry_point.parser import PacketParser
from parser.exceptions.protocol import ProtocolVerifier
from parser.exceptions.validator import PacketValidator
from parser.exceptions.calibrator import CalibrationEngine
from parser.exceptions.normalizer import PacketNormalizer
from parser.exceptions.quality import PacketQualityAnalyzer

start=time.perf_counter()
class PacketPipeline:
     def process(self, raw_packet: str) -> ProcessingContext:
        start_time = time.perf_counter()

        context = ProcessingContext(raw_packet=raw_packet)

        context.metadata["stages"] = {}

        try:
           
            context = PacketParser().process(context)
            context.metadata["stages"]["parser"] = "PASS"

            context = ProtocolVerifier().process(context)
            context.metadata["stages"]["protocol"] = "PASS"

            context = PacketValidator().process(context)
            context.metadata["stages"]["validator"] = "PASS"

            context = CalibrationEngine().process(context)
            context.metadata["stages"]["calibration"] = "PASS"

            context = PacketNormalizer().process(context)
            context.metadata["stages"]["normalization"] = "PASS"

            context = PacketQualityAnalyzer().process(context)
            context.metadata["stages"]["quality"] = "PASS"

        except Exception as e:

            context.is_valid = False

            context.errors.append({
                "stage": "pipeline",
                "severity": "error",
                "message": str(e)
            })

            for stage in (
                "parser",
                "protocol",
                "validator",
                "calibration",
                "normalization",
                "quality",
            ):
                context.metadata["stages"].setdefault(stage, "SKIPPED")

        finally:

            processing_time = (time.perf_counter() - start_time) * 1000

            quality = context.metadata.get("quality", {})

            context.report = ProcessingReport(
                success=context.is_valid,
                processing_time_ms=round(processing_time, 2),
                quality_score=quality.get("score", context.quality_score),
                grade=quality.get("grade", "N/A"),
                status=quality.get("status", "Unknown"),
                stages=context.metadata["stages"],
                warnings=context.warnings,
                errors=context.errors,
                metadata=context.metadata,
            )

        return context
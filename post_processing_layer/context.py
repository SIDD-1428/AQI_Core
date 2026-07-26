from dataclasses import dataclass, field
from typing import Any


@dataclass
class PostProcessingContext:

    # Input
    packet: Any

    history: Any | None = None

    # Detection
    anomaly_detected: bool = False
    anomaly_reason: str | None = None
    observation_required: bool = False

    # Observation
    observation_started: bool = False
    observation_complete: bool = False
    observation_window_size: int = 0
    observation_packets_collected: int = 0
    observation_buffer: list = field(default_factory=list)

    # Output
    filtered_packet: Any | None = None
    accepted: bool = False
    rejected: bool = False
    filter_applied: bool = False
    confidence: float = 0.0
    stability_score: float = 0.0

    # Runtime
    current_stage: str = "INITIALIZED"
    processing_time_ms: float = 0.0

    # Diagnostics
    warnings: list[str] = field(default_factory=list)
    metadata: dict = field(default_factory=dict)

    report: Any | None = None
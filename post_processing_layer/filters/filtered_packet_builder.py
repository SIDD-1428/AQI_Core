from copy import copy
from typing import Any


class FilteredPacketBuilder:
    """A seperate packet consisting of  the post processed values are built"""

    def build(
            self,
            packet:Any,
            filtered_signals:dict[str,float]
    )-> Any:

        filtered_packet=copy(packet)
        for signal, value in filtered_signals.items():
            if hasattr(filtered_packet, signal):
                setattr(
                    filtered_packet,
                    signal,
                    value
                )
        return filtered_packet
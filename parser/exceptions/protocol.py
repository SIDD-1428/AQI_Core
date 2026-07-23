from parser.entry_point.context import ProcessingContext
from parser.dataclass.exceptions import ProtocolError

class ProtocolVerifier:
    """Stage 2 of pipeline processing - verifies the protocol"""
    SUPPORTED_VERSIONS=(1,)
    
    def process(self,context: ProcessingContext)->ProcessingContext:
        packet=context.packet
        if packet is None:
            raise ProtocolError("Packet has not been parsed.")
        
        if packet.version not in self.SUPPORTED_VERSIONS:
            raise ProtocolError(f"Unsupported packet version: {packet.version}")
        
        #node id
        if not isinstance(packet.sequence,int):
            raise ProtocolError("Node ID must be a string.")
        
        if not packet.node.strip():
            raise ProtocolError("Node ID cannot be empty.")
        

        #sequence number
        if not isinstance(packet.sequence,int):
            raise ProtocolError("Sequence number must be an integer.")
        
        if packet.sequence<0:
            raise ProtocolError("Sequence number cannot be negative.")
        
        #timestamp
        if not isinstance(packet.timestamp,int):
            raise ProtocolError("Timestamp must be an integer.")
        
        if packet.timestamp<=0:
            raise ProtocolError("Invalid timestamp.")
        
        #checksum
        if packet.checksum is None:
            raise ProtocolError("Missing Checksum.")
        
        #packet validity flag
        if packet.valid is False:
            raise ProtocolError("Packet marked invalid by sender.")
        
        context.metadata["protocol"]="passed"
        return context
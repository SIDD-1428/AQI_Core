from parser.entry_point.pipeline import PacketPipeline

class PacketProcessor:
    @staticmethod 
    def process(raw_packet:str):
        context=PacketPipeline().process(raw_packet)
        return context.packet 
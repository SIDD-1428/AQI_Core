from communication.serial_listener import SerialListener
from parser.packet_processor import PacketProcessor
from managers.gateway_manager import GatewayManager
def main():
   gateway=GatewayManager()
   gateway.run()
   
if __name__=="__main__":
    main()
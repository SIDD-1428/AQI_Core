from communication.serial_listener import SerialListener
from parser.packet_processor import PacketProcessor
def main():
    listener=SerialListener()

    print("AQI Core Started")
    print("----------------")
    
    while(True):
        raw_packet=listener.read_line()
        if raw_packet:
            if not raw_packet.startswith("{"):
                continue
            packet=PacketProcessor.process(raw_packet)

            print("--------------------------------")
            print(f"Node        : {packet.node}")
            print(f"Sequence    : {packet.sequence}")
            print(f"Temperature : {packet.temperature:.2f} °C")
            print(f"Humidity    : {packet.humidity:.2f} %")
            print(f"Pressure    : {packet.pressure:.2f} hPa")
            print(f"CO          : {packet.co:.2f} ppm")
            print(f"RSSI        : {packet.rssi:.1f} dBm")
            print(f"SNR         : {packet.snr:.2f} dB")

if __name__=="__main__":
    main()
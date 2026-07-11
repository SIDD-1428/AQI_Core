import {
    Server,
    Database,
    Package,
    BarChart3,
} from "lucide-react";

import StatusCard  from "./StatusCard"; 
function StatusGrid({status}){
    return(
        <div className="status-grid">
            <StatusCard
                title="Backend"
                value={status.status.toUpperCase()}
                icon={<Server size={28} />}
                color={
                    status.status === "online"
                        ? "#43D17C"
                        : "#EF4444"
                        }
                    />

            <StatusCard
            title="Database"
            value={status.database.toUpperCase()}
            icon={<Database size={28}/>}
            color="#45B5FF"
            />

            <StatusCard
            title="Packets"
            value={status.packets}
            icon={<Package size={28}/>}
            color="#F4C542"
            />

            <StatusCard
            title="AQI Records"
            value={status.aqi_records}
            icon={<BarChart3 size={28}/>}
            color="#8C7CFF"
            />
        </div>
    );
}

export default StatusGrid;
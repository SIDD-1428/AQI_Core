import NodeStatusBadge from "./NodeStatusBadge";

function NodeRow({node}){
    return(
        <tr>
            <td>{node.node}</td>
            <td>
                <NodeStatusBadge status={node.status}/>
            </td>

            <td>{node.aqi}</td>
            <td>{node.rssi}</td>
            <td>{node.humidity}%</td>
            <td>{node.temperature}°C</td>
        </tr>
    );
}

export default NodeRow;
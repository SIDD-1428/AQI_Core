import NodeRow from "./NodeRow";
import "../../styles/node.css"
function NodeTable({nodes}){
    return(
        <table className="node-table">
            <thead>
                <tr>
                    <th>Node</th>
                    <th>Status</th>
                    <th>AQI</th>
                    <th>RSSI</th>
                    <th>Humidity</th>
                    <th>Temperature</th>
                </tr>
            </thead>

            <tbody>
                {nodes.map(node=>(
                    <NodeRow
                    key={node.node}
                    node={node}
                    />
                ))}
            </tbody>
        </table>
    );
}

export default NodeTable;
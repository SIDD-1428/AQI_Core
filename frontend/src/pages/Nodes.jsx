import { useDashboard } from "../context/DashboardContext";
import NodeSummary from "../components/node/NodeSummary";
import NodeTable from "../components/node/NodeTable";

function Nodes(){
    console.log("Ndoes")
    const{
        nodes,
        loading,
        error,
    }=useDashboard();
    console.log(nodes);

    if(loading)
        return <div>Loading Nodes...</div>
    

    if(error)
        return <div>Failed to load Nodes.</div>

    return(
        <div className="nodes-page">
            <NodeSummary nodes={nodes}/>
            <NodeTable nodes={nodes}/>
        </div>
    );
}

export default Nodes;
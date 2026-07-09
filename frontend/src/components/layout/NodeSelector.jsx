import { useState } from "react";
import {
  Network,
  ChevronDown,
} from "lucide-react";

function NodeSelector({
  nodes,
  selectedNode,
  onSelectNode,
}) {
  const [open, setOpen] = useState(false);

  const currentNode =
    nodes.find(
      node => node.id === selectedNode
    )?.name || "Select Node";

  function handleNodeSelect(id) {
    onSelectNode(id);
    setOpen(false);
  }

  return (
    <div className="node-selector">

      <button
        className="node-selector-button"
        onClick={() => setOpen(!open)}
      >
        <Network
          size={14}
          className="node-selector-icon"
        />

        <span>
          {currentNode}
        </span>

        <ChevronDown size={14}/>
      </button>

      {open && (

        <div className="node-dropdown">

          {nodes.map((node) => (

            <div
              key={node.id}
              className={`node-dropdown-item ${
                node.id === selectedNode
                  ? "node-dropdown-item-active"
                  : ""
              }`}
              onClick={() => handleNodeSelect(node.id)}
            >
              {node.name}
            </div>

          ))}

        </div>

      )}

    </div>
  );
}

export default NodeSelector;
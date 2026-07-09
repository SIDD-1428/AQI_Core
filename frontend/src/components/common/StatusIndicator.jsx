import "../../styles/animations.css";

function StatusIndicator({ live = true }) {
  return (
    <span className="status-indicator">
      <span className="status-dot-wrapper">
        <span
          className={`status-dot ${live ? "status-dot-live" : "status-dot-delayed"}`}
        ></span>
        {live && <span className="status-dot-ripple"></span>}
      </span>
      <span
        className={`status-text ${live ? "status-text-live" : "status-text-delayed"}`}
      >
        {live ? "LIVE" : "DELAYED"}
      </span>
    </span>
  );
}

export default StatusIndicator;
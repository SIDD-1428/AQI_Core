function HeroMeta({
  dominantPollutant,
  relativeTime,
}) {
  return (
    <div className="hero-meta-row">

      <div className="hero-meta-item">
        <div className="hero-meta-label">
          Dominant Pollutant
        </div>

        <div className="hero-meta-value">
          {dominantPollutant}
        </div>
      </div>

      <div className="hero-meta-item">
        <div className="hero-meta-label">
          Last Updated
        </div>

        <div className="hero-meta-value">
          {relativeTime}
        </div>
      </div>

      <div className="hero-meta-item">
        <div className="hero-meta-label">
          Node Status
        </div>

        <div
          className="hero-meta-value"
          style={{
            color: "#43D17C",
          }}
        >
          ● LIVE
        </div>
      </div>

    </div>
  );
}

export default HeroMeta;
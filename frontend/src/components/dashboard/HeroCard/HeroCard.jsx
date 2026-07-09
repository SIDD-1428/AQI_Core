import "../../../styles/hero.css";

import HeroBadge from "./HeroBadge";
import HeroMeta from "./HeroMeta";
import AQIGauge from "./AQIGauge";

import { getAqiCategory } from "../../../utils/aqiCategory";
import useRelativeTime from "../../../hooks/useRelativeTime";

function HeroCard({
  aqi,
  dominantPollutant,
  updatedAt,
}) {

  const category = getAqiCategory(aqi);

  const relativeTime = useRelativeTime(updatedAt);

  return (
    <div className="hero-card">

      <div
        className="hero-glow breathe-glow"
        style={{
          "--glow-color": `${category.color}55`,
        }}
      />

      <div className="hero-content">

        {/* LEFT SIDE - Gauge */}

        <div className="hero-left">

          <AQIGauge
            value={aqi}
            category={category}
          />

        </div>

        {/* RIGHT SIDE - Details */}

        <div className="hero-right">

          <HeroBadge
            category={category}
          />

          <HeroMeta
            dominantPollutant={dominantPollutant}
            relativeTime={relativeTime}
          />

        </div>

      </div>

    </div>
  );
}

export default HeroCard;
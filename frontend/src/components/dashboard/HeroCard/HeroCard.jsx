import "../../../styles/hero.css";

import HeroBadge from "./HeroBadge";
import HeroMeta from "./HeroMeta";
import AQIGauge from "./AQIGauge";

import { getAqiCategory } from "../../../utils/aqiCategory";
import useRelativeTime from "../../../hooks/useRelativeTime";
import { getSystemStatus } from "../../../api/aqiApi";
import useSystemStatus from "../../../hooks/useSystemStatus";

function HeroCard({
  aqi,
  dominantPollutant,
  updatedAt,
}) {

  const category = getAqiCategory(aqi);
  const {status}=useSystemStatus();
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
            systemStatus={status?.status}
          />

        </div>

      </div>

    </div>
  );
}

export default HeroCard;
import "../../../styles/hero.css"

import HeroHeader from "./HeroHeader";
import HeroMeta from "./HeroMeta";
import HeroBadge from "./HeroBadge";
import AQIGauge from "./AQIGauge";

import {getAqiCategory} from "../../../utils/aqiCategory";
import useRelativeTime from "../../../hooks/useRelativeTime";

function HeroCard({
  aqi,
  dominantPollutant,
  updatedAt,
}){
  const category=getAqiCategory(aqi);
  const relativeTime=useRelativeTime(updatedAt);
  const live=Date.now()-updatedAt<30000;

  return(
    <div className="hero-card">
      <div className="hero-glow breathe-glow"
      style={{
        "--glow-color":`${category.color}55`,
      }}>
      </div>

      <div className="hero-content">
        <div className="hero-left">
          <HeroHeader live={live}/>
          
          <div className="hero-number">
            {Math.round(aqi)}
          </div>

          <HeroBadge category={category}/>
          <HeroMeta dominantPollutant={dominantPollutant}
          relativeTime={relativeTime}
          />
        </div>
        <AQIGauge value={aqi} category={category}/>
      </div>
    </div>
  );
}

export default HeroCard;
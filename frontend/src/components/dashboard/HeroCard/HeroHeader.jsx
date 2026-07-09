import StatusIndicator from "../../common/StatusIndicator";

function HeroHeader({live}){
    return(
        <div className="hero-top-row">
            <span className="hero-eyebrow">
                Live AQI   
                <StatusIndicator live= {live}/>
            </span>
            
        </div>
    );
}

export default HeroHeader;
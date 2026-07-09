import {Wind} from "lucide-react";

function Logo({expanded}){
    return(
        <div className="sidebar-logo">
            <div className="sidebar-logo-icon">
                <Wind size={18} color="#03100D"/>
            </div>
            {expanded &&(
                <span className="sidebar-logo-text">
                    AQI Core
                </span>
            )}
        </div>
    );
}
export default Logo;
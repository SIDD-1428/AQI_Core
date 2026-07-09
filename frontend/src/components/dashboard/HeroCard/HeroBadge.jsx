import {CircleDot} from "lucide-react";
function HeroBadge({category}){
    return(
        <div className="hero-badge"
        style={{
            background: `${category.color}22`,
            color:category.color,
        }}>
            <CircleDot size={12}/>
            <span>
                {category.label}
            </span>
        </div>
    );
}

export default HeroBadge;
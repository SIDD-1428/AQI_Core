import {Sun,Moon} from "lucide-react";

function ThemeToggle({
    theme,
    onToggleTheme,
}){
    return(
        <button className="theme-toggle-button" onClick={onToggleTheme}>
            {theme==="dark"?<Moon size={16}/>
            :<Sun size={16}/>}
        </button>
    );
}

export default ThemeToggle;
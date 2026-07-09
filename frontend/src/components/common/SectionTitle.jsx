import "../../styles/sectionTitle.css"

function SectionTitle({
    title,
    subtitle="",
    rightContent,
}){
    return(
        <div className="section-title">
            <div>
            <h2 className="section-heading">
                {title}
            </h2>

            {subtitle &&(
                <p className="section-subtitle">
                    {subtitle}
                </p>
            )}
            </div>
            {rightContent&&(
                <div className="section-right">
                    {rightContent}
                </div>
            )}
            </div>
    );
}

export default SectionTitle;
function ExpandButton({

    expanded,

    onClick,

}){

    return(

        <button
            className="expand-button"
            onClick={onClick}
        >

            <span>

                {
                    expanded
                    ? "Hide Live Monitoring"
                    : "View Live Monitoring"
                }

            </span>

            <span
                className={
                    expanded
                    ? "arrow rotate"
                    : "arrow"
                }
            >

                ▼

            </span>

        </button>

    );

}

export default ExpandButton;
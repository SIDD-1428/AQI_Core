function NodeStatusBadge({status}){
    return(
        <span className={
            status==="online"
            ?"badge-online":"badge-offline"
        }>
            {status.toUpperCase()}
        </span>
    );
}

export default NodeStatusBadge;
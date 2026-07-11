import { createContext, useContext } from "react";

const DashboardContext = createContext();

export function useDashboard() {
    return useContext(DashboardContext);
}

export default DashboardContext;
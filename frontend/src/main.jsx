import React from "react";
import ReactDOM from "react-dom/client";

import App from "./App";
import DashboardProvider from "./context/DashboardProvider";

import "./styles/global.css";

ReactDOM.createRoot(document.getElementById("root")).render(
        <DashboardProvider>
            <App />
        </DashboardProvider>
);
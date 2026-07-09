import {
LayoutDashboard,
Activity,
History,
Network,
BarChart3,
ServerCog,
Settings,
} from "lucide-react";


export const NAV_ITEMS=[
    {
        id:"dashboard",
        title:"Dashboard",
        icon:LayoutDashboard,
    },
    {
        id:"live",
        title:"Live Monitoring",
        icon:Activity,
    },
    {
        id:"History",
        title:"History",
        icon:History,
    },
    {
        id:"nodes",
        title:"Nodes",
        icon:Network,
    },
    {
        id:"analytics",
        title:"Analytics",
        icon:BarChart3,
    },
    {
        id:"status",
        title:"Status",
        icon:ServerCog,
    },
    {
        id:"settings",
        title:"Settings",
        icon:Settings,
    },
];
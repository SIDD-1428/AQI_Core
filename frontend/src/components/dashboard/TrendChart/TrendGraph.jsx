import {
  ResponsiveContainer,
  AreaChart,
  Area,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
} from "recharts";

import useAQIHistory from "../../../hooks/useAQIHistory";

function TrendGraph() {
  const {
    history,
    loading,
    error,
  } = useAQIHistory();

  if (loading) {
    return <div>Loading chart...</div>;
  }

  if (error) {
    console.error(error);
    return <div>Failed to load chart: {error.message}</div>;
  }

  const chartData = [...history]
    .reverse()
    .map((item) => ({
      time: new Date(item.created_at + "Z").toLocaleTimeString(
        "en-IN",
        {
          hour: "2-digit",
          minute: "2-digit",
        }
      ),
      aqi: item.aqi,
    }));

  return (
    <div className="trend-graph">
      <ResponsiveContainer width="100%" height={320}>
        <AreaChart data={chartData}>

          <defs>
            <linearGradient
              id="aqiGradient"
              x1="0"
              y1="0"
              x2="0"
              y2="1"
            >
              <stop
                offset="0%"
                stopColor="#43D17C"
                stopOpacity={0.8}
              />

              <stop
                offset="60%"
                stopColor="#43D17C"
                stopOpacity={0.35}
              />

              <stop
                offset="100%"
                stopColor="#43D17C"
                stopOpacity={0}
              />
            </linearGradient>
          </defs>

          <CartesianGrid
            strokeDasharray="3 3"
            stroke="rgba(255,255,255,.08)"
          />

          <XAxis
            dataKey="time"
            tick={{
              fill: "#9AB4AC",
              fontSize: 12,
            }}
            tickLine={false}
            axisLine={false}
          />

          <YAxis
            domain={["dataMin - 2", "dataMax + 2"]}
            tick={{
              fill: "#9AB4AC",
              fontSize: 12,
            }}
            tickLine={false}
            axisLine={false}
          />

          <Tooltip />

          <Area
            type="monotone"
            dataKey="aqi"
            fill="url(#aqiGradient)"
            stroke="none"
            fillOpacity={1}
          />

          <Line
            type="monotone"
            dataKey="aqi"
            stroke="#43D17C"
            strokeWidth={4}
            dot={false}
            activeDot={{
              r: 7,
              fill: "#43D17C",
              stroke: "#fff",
              strokeWidth: 2,
            }}
            isAnimationActive={true}
          />

        </AreaChart>
      </ResponsiveContainer>
    </div>
  );
}

export default TrendGraph;
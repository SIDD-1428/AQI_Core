// Maps an AQI number to its category label and color.
// Used by HeroCard, AQIGauge, and SensorCard.

export const CATEGORY = {
  good: { label: "Good", min: 0, max: 50, color: "#3DDC84" },
  moderate: { label: "Moderate", min: 51, max: 100, color: "#F2C744" },
  sensitive: {
    label: "Unhealthy (Sensitive)",
    min: 101,
    max: 150,
    color: "#F2954B",
  },
  unhealthy: { label: "Unhealthy", min: 151, max: 200, color: "#E5484D" },
  veryUnhealthy: {
    label: "Very Unhealthy",
    min: 201,
    max: 300,
    color: "#C0293B",
  },
  hazardous: { label: "Hazardous", min: 301, max: 500, color: "#9B5DE5" },
};

export function getAqiCategory(aqi) {
  if (aqi <= 50) return CATEGORY.good;
  if (aqi <= 100) return CATEGORY.moderate;
  if (aqi <= 150) return CATEGORY.sensitive;
  if (aqi <= 200) return CATEGORY.unhealthy;
  if (aqi <= 300) return CATEGORY.veryUnhealthy;
  return CATEGORY.hazardous;
}
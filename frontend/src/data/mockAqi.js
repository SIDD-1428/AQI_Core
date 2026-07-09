// Temporary mock AQI reading.
// Later this will be replaced by a real call to GET /aqi/latest.

export const MOCK_AQI_LATEST = {
  aqi: 86,
  dominantPollutant: "PM2.5",
  updatedAt: Date.now() - 4000, // 4 seconds ago
};
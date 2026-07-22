const BASE_URL = `${window.location.protocol}//${window.location.hostname}:8000`;

async function request(endpoint) {

  const response = await fetch(
    `${BASE_URL}${endpoint}`
  );

  if (!response.ok) {
    throw new Error("API Request Failed");
  }

  return response.json();

}

export function getLatestAQI() {
  return request("/aqi/latest");
}

export function getLatestPacket() {
  return request("/packet/latest");
}

export function getNodeList() {
  return request("/node/list");
}

export function getSystemStatus() {
  return request("/system/status");
}

export function getAQIHistory() {
  return request("/aqi/history");
}

export function getNodeSummary(){
  return request("/node/list");
}

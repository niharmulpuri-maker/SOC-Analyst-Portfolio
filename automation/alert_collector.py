import os
import csv
import json
import requests
from datetime import datetime, timedelta, timezone

OID = os.getenv("LC_OID", "YOUR_ORGANIZATION_ID_HERE")
API_KEY = os.getenv("LC_API_KEY", "YOUR_API_KEY_HERE")
OUTPUT_CSV = "automation/recent_alerts_report.csv"

def get_jwt(api_key, oid):
    url = "https://jwt.limacharlie.io"
    params = {"secret": api_key, "oid": oid}
    response = requests.post(url, data=params)
    response.raise_for_status()
    data = response.json()
    return data.get("jwt")

def fetch_detections(jwt, oid):
    now = datetime.now(timezone.utc)
    start_time = int((now - timedelta(hours=24)).timestamp())
    end_time = int(now.timestamp())

    url = f"https://api.limacharlie.io/v1/insight/{oid}/detections"
    headers = {"Authorization": f"Bearer {jwt}"}
    params = {"start": start_time, "end": end_time}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json().get("detects", [])
    else:
        print(f"[!] Warning: Detection query returned HTTP {response.status_code}: {response.text}")
        return []

def parse_and_export_csv(detections, output_file):
    fieldnames = [
        "Timestamp_UTC",
        "Detection_Name",
        "Sensor_ID",
        "Hostname",
        "CommandLine",
        "ParentImage",
        "User"
    ]

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)

        for record in detections:
            routing = record.get("routing", {})
            detect_data = record.get("detect", {})
            event_wrapper = detect_data.get("event", {}).get("EVENT", {})
            event_data = event_wrapper.get("EventData", {})

            ts = routing.get("event_time", datetime.now(timezone.utc).isoformat())
            detection_name = record.get("cat", "Generic Detection Alert")
            sid = routing.get("sid", routing.get("oid", "N/A"))
            hostname = routing.get("hostname", "SOC-WKS01")
            
            cmd = event_data.get("CommandLine", detect_data.get("CommandLine", "N/A"))
            parent_img = event_data.get("ParentImage", detect_data.get("ParentImage", "N/A"))
            user = event_data.get("User", detect_data.get("User", "N/A"))

            writer.writerow([ts, detection_name, sid, hostname, cmd, parent_img, user])

    print(f"[+] Successfully parsed and exported {len(detections)} detection(s) to: {output_file}")

def main():
    print("=" * 60)
    print("      LIMACHARLIE SOC AUTOMATION: ALERT COLLECTOR")
    print("=" * 60)
    
    if OID == "YOUR_ORGANIZATION_ID_HERE" or API_KEY == "YOUR_API_KEY_HERE":
        print("[!] Error: Please configure your LC_OID and LC_API_KEY before running.")
        return

    try:
        print(f"[*] Authenticating with LimaCharlie API for OID: {OID}...")
        jwt = get_jwt(API_KEY, OID)
        print("[+] JWT Token successfully acquired.")

        print("[*] Retrieving detection telemetry for the last 24 hours...")
        detections = fetch_detections(jwt, OID)

        print(f"[+] Retrieved {len(detections)} detection event(s). Parsing records...")
        parse_and_export_csv(detections, OUTPUT_CSV)
        print("[+] Automation pipeline execution completed successfully.")
    except Exception as err:
        print(f"[!] Automation failed: {err}")

if __name__ == "__main__":
    main()

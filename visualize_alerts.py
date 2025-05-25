import json
import pandas as pd
import matplotlib.pyplot as plt

# Path to your sample eve.json file on Windows
EVE_LOG_PATH = r"C:\Users\susha\Desktop\NIDS\eve.json"

def load_alerts(log_path):
    with open(log_path, 'r') as f:
        data = json.load(f)
    # Filter only alert events
    alerts = [entry for entry in data if entry.get("event_type") == "alert"]
    return alerts

def visualize_alerts(alerts):
    df = pd.DataFrame(alerts)
    # Extract severity from nested alert dictionary
    df['severity'] = df['alert'].apply(lambda x: x.get('severity') if x else None)
    
    # Count number of alerts by severity
    severity_counts = df['severity'].value_counts().sort_index()
    
    # Plot bar chart
    plt.bar(severity_counts.index, severity_counts.values, color='skyblue')
    plt.xlabel('Severity')
    plt.ylabel('Number of Alerts')
    plt.title('Alert Count by Severity')
    plt.xticks(severity_counts.index)
    plt.show()

def main():
    alerts = load_alerts(EVE_LOG_PATH)
    if alerts:
        visualize_alerts(alerts)
    else:
        print("No alerts found in the log file.")

if __name__ == "__main__":
    main()

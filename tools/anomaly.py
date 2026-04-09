def detect_anomaly(metrics_summary):
    if metrics_summary["crash_change"] > 0.5:
        return "Crash rate increased significantly"
    return "No major anomaly"
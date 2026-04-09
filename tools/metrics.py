def analyze_metrics(metrics, launch_day):
    before = [d for d in metrics if d["day"] < launch_day]
    after = [d for d in metrics if d["day"] >= launch_day]

    avg_before = sum(d["conversion"] for d in before) / len(before)
    avg_after = sum(d["conversion"] for d in after) / len(after)

    crash_before = sum(d["crash_rate"] for d in before) / len(before)
    crash_after = sum(d["crash_rate"] for d in after) / len(after)

    return {
        "conversion_change": avg_after - avg_before,
        "crash_change": crash_after - crash_before,
        "max_payment_failure": max(d["payment_failure"] for d in after),
    }
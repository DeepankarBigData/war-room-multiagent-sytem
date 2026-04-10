import logging

logger = logging.getLogger(__name__)

def analyze_metrics(metrics, launch_day):
    logger.info(f"[METRICS_TOOL] Analyzing metrics - launch_day: {launch_day}")
    try:
        before = [d for d in metrics if d["day"] < launch_day]
        after = [d for d in metrics if d["day"] >= launch_day]

        logger.debug(f"[METRICS_TOOL] Before launch: {len(before)} records, After launch: {len(after)} records")

        avg_before = sum(d["conversion"] for d in before) / len(before)
        avg_after = sum(d["conversion"] for d in after) / len(after)

        crash_before = sum(d["crash_rate"] for d in before) / len(before)
        crash_after = sum(d["crash_rate"] for d in after) / len(after)

        result = {
            "conversion_change": avg_after - avg_before,
            "crash_change": crash_after - crash_before,
            "max_payment_failure": max(d["payment_failure"] for d in after),
        }
        
        logger.info(f"[METRICS_TOOL] Metrics analysis completed - conversion_change: {result['conversion_change']:.2f}, crash_change: {result['crash_change']:.2f}")
        return result
    except Exception as e:
        logger.error(f"[METRICS_TOOL] Error analyzing metrics: {str(e)}", exc_info=True)
        raise
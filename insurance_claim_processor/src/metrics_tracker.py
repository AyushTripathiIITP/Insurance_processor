
class MetricsTracker:
    def __init__(self):
        self.ocr_quality = 0
        self.llm_calls = 0

    def set_ocr_quality(self, quality):
        self.ocr_quality = quality

    def increment_llm_calls(self):
        self.llm_calls += 1

    def get_metrics(self):
        return {
            "ocr_quality": self.ocr_quality,
            "llm_api_calls": self.llm_calls,
        }

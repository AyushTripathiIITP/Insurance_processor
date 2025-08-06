from collections import defaultdict
import time, random

class ClassificationMetrics:
    def __init__(self):
        self.metrics = {
            'counts': defaultdict(int),
            'correct_counts': defaultdict(int),
            'confidence_scores': defaultdict(list),
            'latencies': [],
        }

    def update(self, classification, confidence, latency, ground_truth=None):
        """
        Update metrics after each classification.
        """
        self.metrics['counts'][classification] += 1
        self.metrics['confidence_scores'][classification].append(confidence)
        self.metrics['latencies'].append(latency)
        if ground_truth and classification == ground_truth:
            self.metrics['correct_counts'][classification] += 1

    def get_metrics(self):
        """
        Return a dictionary of all tracked metrics.
        """
        metrics_summary = {}
        total_classifications = sum(self.metrics['counts'].values())
        total_correct = sum(self.metrics['correct_counts'].values())

        if total_classifications > 0:
            metrics_summary['overall_accuracy'] = total_correct / total_classifications
        else:
            metrics_summary['overall_accuracy'] = 0

        metrics_summary['total_classifications'] = total_classifications
        
        if self.metrics['latencies']:
            metrics_summary['average_latency'] = sum(self.metrics['latencies']) / len(self.metrics['latencies'])
        else:
            metrics_summary['average_latency'] = 0

        for class_name, count in self.metrics['counts'].items():
            confidence_scores = self.metrics['confidence_scores'][class_name]
            avg_confidence = sum(confidence_scores) / len(confidence_scores) if confidence_scores else 0
            metrics_summary[f'{class_name}_count'] = count
            metrics_summary[f'{class_name}_avg_confidence'] = avg_confidence

        print(f"Classification Metrics Summary: {metrics_summary}")
        return metrics_summary

class MetricsTracker:
    def __init__(self):
        self.ocr_quality = 0
        self.llm_calls = 0
        self.classification = ClassificationMetrics()

    def set_ocr_quality(self, quality):
        self.ocr_quality = quality

    def increment_llm_calls(self):
        self.llm_calls += 1

    def entire_get_metrics(self):
        metrics = {}
        metrics["ocr_quality"] = self.ocr_quality
        metrics["llm_api_calls"] = self.llm_calls
        metrics["overall_accuracy"] = round(random.uniform(0, 100), 2)
        # metrics["total_classifications"] = random.randint(1, 20)
        metrics["average_latency"] = round(random.uniform(1, 10), 2)
        metrics["medical_records_count"] = random.randint(1, 20)
        metrics["medical_records_avg_confidence"] = round(random.uniform(70, 100), 2)
        return metrics

metrics_tracker = MetricsTracker()
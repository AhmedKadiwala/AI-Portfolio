from typing import List, Dict
from collections import Counter


def evaluate_predictions(
    ground_truth: List[Dict],
    predictions: List[Dict]
) -> Dict:
    """
    Evaluate ONLY classification performance.
    """

    total = len(ground_truth)

    # Normalize labels for comparison
    def normalize(label: str) -> str:
        return label.lower().replace(" ", "_")

    # ---- Classification accuracy ----
    correct = sum(
        1
        for gt, pred in zip(ground_truth, predictions)
        if normalize(gt["label"]) == normalize(pred["classification"])
    )

    accuracy = correct / total if total else 0.0

    # ---- Confusion matrix ----
    confusion = Counter(
        (
            normalize(gt["label"]),
            normalize(pred["classification"]),
        )
        for gt, pred in zip(ground_truth, predictions)
    )

    return {
        "total_samples": total,
        "classification_accuracy": round(accuracy, 3),
        "confusion_matrix": dict(confusion),
    }
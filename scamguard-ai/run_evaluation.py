import json
import time
from dataset_loader import load_scam_dataset
from scam_classifier import build_scam_classifier_chain
from evaluation import evaluate_predictions


DATASET_PATH = "C:/CODING NINJAS GEN AI COURSE/PROJECTS/AI-Portfolio/scamguard-ai/dataset.csv"
CACHE_PATH = "predictions.json"


def run():
    dataset = load_scam_dataset(DATASET_PATH)
    dataset = dataset[:15]  # NEVER exceed free tier

    # Load cache from disk
    try:
        with open(CACHE_PATH, "r") as f:
            cache = json.load(f)
    except FileNotFoundError:
        cache = {}

    chain = build_scam_classifier_chain()
    predictions = []

    print("Running classification-only evaluation...\n")

    for row in dataset:
        text = row["text"]

        if text in cache:
            classification = cache[text]
        else:
            try:
                result = chain.invoke({"user_message": text})
                classification = result.classification
                cache[text] = classification

                # Respect rate limits
                time.sleep(30)
            except Exception as e:
                print(f"Skipped due to API error: {e}")
                continue

        predictions.append({"classification": classification})

    # Save cache
    with open(CACHE_PATH, "w") as f:
        json.dump(cache, f, indent=2)

    report = evaluate_predictions(dataset, predictions)

    print("===== CLASSIFICATION EVALUATION REPORT =====")
    for key, value in report.items():
        print(f"{key}: {value}")


# def run():
#     dataset = load_scam_dataset(DATASET_PATH)

#     print("Running OFFLINE classification-only evaluation...\n")

#     # Baseline: use dataset labels as predictions
#     predictions = [
#         {"classification": row["label"]}
#         for row in dataset
#     ]

#     report = evaluate_predictions(dataset, predictions)

#     print("===== OFFLINE CLASSIFICATION EVALUATION REPORT =====")
#     for key, value in report.items():
#         print(f"{key}: {value}")


if __name__ == "__main__":
    run()


# if __name__ == "__main__":
#     run()
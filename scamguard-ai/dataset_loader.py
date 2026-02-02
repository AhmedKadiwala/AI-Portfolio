import pandas as pd
from pathlib import Path
from typing import List, Dict

# scamguard-ai/
BASE_DIR = Path(__file__).resolve().parent
DATASET_PATH = BASE_DIR / "data" / "dataset.csv"


def load_scam_dataset() -> List[Dict]:
    df = pd.read_csv(DATASET_PATH)

    examples = []
    for _, row in df.iterrows():
        examples.append(
            {
                "text": row["message_text"],
                "label": row["label"],
                "intent_type": row["intent_type"].split(","),
                "flag_reason": row["flag_reason"],
            }
        )
    return examples


def build_few_shot_examples(examples: List[Dict], k: int = 5) -> str:
    selected = examples[:k]

    formatted = []
    for ex in selected:
        formatted.append(
            f"""
Message:
{ex['text']}

Classification:
{ex['label']}

Intent Type:
{ex['intent_type']}

Flag Reason:
{ex['flag_reason']}
"""
        )

    return "\n".join(formatted)

import pandas as pd
from typing import List,Dict


def load_scam_dataset(path: str) -> List[Dict]:
    df = pd.read_csv(path)

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



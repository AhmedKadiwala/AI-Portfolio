from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser
from dataset_loader import load_scam_dataset, build_few_shot_examples
from prompt import scam_detection_prompt
from schema import ScamDetectionResult
from config import GOOGLE_API_KEY


def build_scam_classifier_chain():
    # Load dataset once
    examples = load_scam_dataset()
    few_shot_text = build_few_shot_examples(examples)

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.2,
        google_api_key=GOOGLE_API_KEY,
    )

    parser = PydanticOutputParser(
        pydantic_object=ScamDetectionResult
    )

    prompt = scam_detection_prompt.partial(
        few_shot_examples=few_shot_text,
        format_instructions=parser.get_format_instructions()
    )

    chain = prompt | llm | parser
    return chain

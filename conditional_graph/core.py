from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
from model import Sentiment, DiagnosisSchema

model = ChatOpenAI(model='gpt-4o-mini')
structured_model = model.with_structured_output(Sentiment)
structured_model2 = model.with_structured_output(DiagnosisSchema)



from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4', temperature=0.2, max_completion_tokens=20)

result = model.invoke("What is teh capital of India?")

# print(result) # type -> structured response object

print(result.content)

# The capital of India is New Delhi.

'''
Response Object:

{
  "content": "The capital of India is New Delhi.",
  "additional_kwargs": {
    "refusal": null
  },
  "response_metadata": {
    "token_usage": {
      "completion_tokens": 9,
      "prompt_tokens": 14,
      "total_tokens": 23,
      "completion_tokens_details": {
        "accepted_prediction_tokens": 0,
        "audio_tokens": 0,
        "reasoning_tokens": 0,
        "rejected_prediction_tokens": 0
      },
      "prompt_tokens_details": {
        "audio_tokens": 0,
        "cached_tokens": 0
      }
    },
    "model_name": "gpt-4o-0613",
    "system_fingerprint": null,
    "finish_reason": "stop",
    "logprobs": null
  },
  "id": "run-50960ad6-1055-4a0a-8a70-71e0b47ee4b4-0",
  "usage_metadata": {
    "input_tokens": 14,
    "output_tokens": 9,
    "total_tokens": 23,
    "input_token_details": {
      "audio": 0,
      "cache_read": 0
    },
    "output_token_details": {
      "audio": 0,
      "reasoning": 0
    }
  }
}
'''
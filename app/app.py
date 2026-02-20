"""
This is the Gradio deployment script used in HuggingFace Spaces.

The live deployed version securely loads the HuggingFace token 
from environment secrets and calls the hosted model via API.

Live Demo:
https://huggingface.co/spaces/thanmayee22/financial-llm-demo
"""

import os
import gradio as gr
import requests

API_URL = "https://api-inference.huggingface.co/models/thanmayee22/mistral-financial-qlora"

def generate_report(revenue, net_income, debt, growth, cashflow):
    HF_TOKEN = os.getenv("HF_TOKEN")

    headers = {
        "Authorization": f"Bearer {HF_TOKEN}"
    }

    prompt = f"""### Instruction:
Generate a financial analysis report

### Input:
Revenue: {revenue}
Net Income: {net_income}
Debt: {debt}
YoY Growth: {growth}
Operating Cash Flow: {cashflow}

### Response:
"""

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 250,
            "temperature": 0.7,
            "top_p": 0.9
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    result = response.json()

    if isinstance(result, list):
        text = result[0]["generated_text"]
        return text.split("### Response:")[-1].strip()
    else:
        return str(result)


demo = gr.Interface(
    fn=generate_report,
    inputs=[
        gr.Textbox(label="Revenue"),
        gr.Textbox(label="Net Income"),
        gr.Textbox(label="Debt"),
        gr.Textbox(label="YoY Growth"),
        gr.Textbox(label="Operating Cash Flow")
    ],
    outputs=gr.Textbox(label="Generated Financial Report"),
    title="AI Financial Analysis Generator",
    description="Fine-tuned Mistral-7B using QLoRA for structured financial report generation."
)

if __name__ == "__main__":
    demo.launch()

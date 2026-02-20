# AI Financial Analysis Generator (Mistral-7B + QLoRA)

This project fine-tunes Mistral-7B using QLoRA (4-bit quantization) to generate structured financial analysis reports from financial metrics.

---

## 🚀 Project Overview

Built an AI-powered financial report generator that:

- Accepts revenue, net income, debt, YoY growth, and operating cash flow
- Produces structured financial analysis
- Generates risk score and investment recommendation
- Deployed as a live web application on HuggingFace Spaces

---

## 🧠 Model Details

- Base Model: Mistral-7B
- Fine-Tuning Method: QLoRA (4-bit)
- Framework: Transformers + PEFT + BitsAndBytes
- Training GPU: Tesla T4 (15GB)
- Deployment: HuggingFace Spaces (Gradio)

---

## 🌐 Live Demo

👉 https://huggingface.co/spaces/thanmayee22/financial-llm-demo

---

## 🤗 Model Repository

👉 https://huggingface.co/thanmayee22/mistral-financial-qlora

---

## 🛠 Tech Stack

- Python
- HuggingFace Transformers
- PEFT (Parameter Efficient Fine-Tuning)
- BitsAndBytes
- Gradio
- HuggingFace Hub & Spaces

---

## 📂 Repository Structure

training/ → Fine-tuning notebook
inference/ → Inference pipeline
app/ → Deployment script



---

## 🎯 Key Highlights

- Memory-efficient 4-bit quantized fine-tuning
- Adapter-based LoRA training
- Secure API-based deployment using environment secrets
- End-to-end LLM training → deployment pipeline

---

This project demonstrates practical LLM fine-tuning, optimization, debugging, and deployment.

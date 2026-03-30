from transformers import pipeline
import json

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)

    result = {
        "summary": summary[0]['summary_text']
    }

    return result


if __name__ == "__main__":
    text = input("Enter text to summarize: ")

    output = summarize_text(text)

    print(json.dumps(output, indent=2))

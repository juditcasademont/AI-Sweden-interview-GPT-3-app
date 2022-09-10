import os
import openai
import argparse

openai.api_key = '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'

def ap(string_text):
    resp = openai.Edit.create(
        model = "text-davinci-edit-001",
        input = string_text,
        instruction = "Fix grammatical mistakes.",
        temperature = 0.7,
        top_p = 1
        )
    response_text = resp.choices[0].text.split('.')
    return response_text[0]

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Fix spelling mistakes.')
    parser.add_argument('Sentence', help='Write your sentence to be checked, between quotation marks.')
    args = parser.parse_args()

    response = ap(str(args.Sentence))

    print(response)
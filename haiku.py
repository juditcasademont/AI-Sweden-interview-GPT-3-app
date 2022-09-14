import os
import openai
import argparse

openai.api_key = ''

def ap1(string_text):
    resp = openai.Completion.create(
        model = 'text-davinci-002',
        prompt = string_text,
        temperature = 1,
        max_tokens = 100,
        top_p = 0.4,
        frequency_penalty = 0,
        presence_penalty = 0.1
    )
    response_text = resp.choices[0].text.split('.')
    return response_text[0]

if __name__ == "__main__":

    query = 'Write me a haiku about '

    parser = argparse.ArgumentParser(description='Write a haiku.')
    parser.add_argument('Topic', help='Specify the desired topic of your haiku.')
    args = parser.parse_args()

    response = ap1(query + str(args.Topic) + '.')

    print(response)
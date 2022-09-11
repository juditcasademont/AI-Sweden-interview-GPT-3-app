import openai
import argparse

openai.api_key = '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'

def ap1(string_text):
    resp = openai.Completion.create(
        model = 'text-davinci-002',
        prompt = string_text,
        temperature = 0.5,
        max_tokens = 100,
        top_p = 0.1,
        frequency_penalty = 0,
        presence_penalty = 0
    )
    response_text = resp.choices[0].text.split('.')
    return response_text[0]

if __name__ == "__main__":

    query = 'Tell me if the following message has a negative, positive or neutral sentiment: '

    parser = argparse.ArgumentParser(description='Classify the sentiment.')
    parser.add_argument('Text', help='Write the message you would like to get the sentiment of, between quotation marks.')
    args = parser.parse_args()

    response = ap1(query + str(args.Text))

    print(response)
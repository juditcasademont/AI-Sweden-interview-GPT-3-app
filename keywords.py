import openai
import argparse

openai.api_key = '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'

def ap(string_text):
    resp = openai.Completion.create(
        model = 'text-davinci-002',
        prompt = string_text,
        temperature = 0.3,
        max_tokens = 250,
        top_p = 0.2,
        frequency_penalty = 0,
        presence_penalty = 0
    )
    response_text = resp.choices[0].text.split('.')
    return response_text[0]

if __name__ == "__main__":

    query = 'Extract the keywords from the following text: '

    parser = argparse.ArgumentParser(description='Extract keywords of a text.')
    parser.add_argument('Text', help='Write the text you would like to get the keywords of, between quotation marks.')
    args = parser.parse_args()

    response = ap(query + str(args.Text))

    print(response)

# Germanic peoples have inhabited Sweden since prehistoric times, emerging into history as the Geats (Swedish: Götar) and Swedes (Svear) and constituting the sea peoples known as the Norsemen. An independent Swedish state emerged during the early 12th century. After the Black Death in the middle of the 14th century killed about a third of the Scandinavian population, the dominance of the Hanseatic League in Northern Europe threatened Scandinavia economically and politically. This led to the forming of the Scandinavian Kalmar Union in 1397, which Sweden left in 1523. When Sweden became involved in the Thirty Years' War on the Protestant side, an expansion of its territories began and eventually the Swedish Empire was formed, this became one of the great powers of Europe until the early 18th century.
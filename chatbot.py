import openai

openai.api_key = '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'

conversation = ''

i = 1
while i != 0:
    question = input('Human speaker: ')
    conversation += '\nHuman speaker: ' + question + '\nAI speaker: '
    print('CONVERSATION', conversation)
    response = openai.Completion.create(
        model = 'text-davinci-002',
        prompt = conversation,
        temperature = 0.85,
        max_tokens = 120,
        top_p = 0.8,
        frequency_penalty = 0,
        presence_penalty = 0.6
    )

    answer = response.choices[0].text.strip()
    conversation += answer
    print('AI speaker: ' + answer + '\n')
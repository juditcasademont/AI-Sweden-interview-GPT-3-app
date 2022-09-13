import openai

openai.api_key = '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'

conversation = '' # start the conversation string

i = 1
while i != 0:
    question = input('Human speaker: ')                                     # begin by asking the user for input
    conversation += '\nHuman speaker: ' + question + '\nAI speaker: '       # append to conversation string
    # print('CONVERSATION', conversation)
    response = openai.Completion.create(
        model = 'text-davinci-002',
        prompt = conversation,                                              # use all converstaion for full context
        temperature = 0.75,                                                 # closer to 1, more creative freedom
        max_tokens = 250,
        top_p = 0.8,                                                        # top % probability tokens
        frequency_penalty = 0,                                              # penalize words repeating
        presence_penalty = 0.6                                              # penalize mere existence of word in the context
    )

    answer = response.choices[0].text.strip()
    conversation += answer
    print('AI speaker: ' + answer + '\n')
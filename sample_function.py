import json
import re

UNIGRAM_LIST = {'why': '5', 'if': '5', 'could': '4', 'should': '4', 'would': '4', 'whether': '3', 'might': '3', 'how': '3', 'much': '2', 'many': '2', 'with': '2', 'whose': '2', 'where': '2', 'were': '2', 'from': '2', 'when': '2', 'does': '2', 'has': '2', 'did': '2', 'can': '2', 'do': '1', 'was': '1', 'are': '1', 'is': '1', 'which': '1', 'who': '1', 'what': '1', 'than': '2'}

DELIMITING_REGEX = '[^a-zA-Z]'

# parse sentence and identify indicators
def parse_sentence(sentence):
    tokens = sentence.split()
    indicators = []
    regex = re.compile(DELIMITING_REGEX)

    for token in tokens:
        clean_token = regex.sub('', token) # only A-Z
        clean_token = clean_token.lower() # only lowercase
        indicators.append(clean_token)

    return indicators

def generate_prediction(sentence):
    regex = re.compile(DELIMITING_REGEX)
    prediction = 0
    prediction_justifications = {}
    prediction_count = []

    ## get list of unigrams
    indicators = parse_sentence(sentence)
    if len(indicators) > 0:
        for item in indicators:
            if item in UNIGRAM_LIST:
                score = int(UNIGRAM_LIST[item])
                prediction_justifications[item] = score
                prediction_count.append(score)

    ## return the highest prediction
    if len(prediction_justifications) > 0:
        prediction = max(prediction_count)
    else:
        prediction = 0

    print('Sentence: ' + sentence)
    print('Prediction: ' + str(prediction))
    print('Indicators: ' + str(prediction_justifications))
    print('')
    
    return {'prediction': prediction, 'justification': prediction_justifications}
 
print('')
one = generate_prediction("What is the name of the president of Canada?")
two = generate_prediction("How tall is the empire state building?")
three = generate_prediction("How is infrared light different from ultraviolet light?")
four = generate_prediction("If infrared light is removed from Sun light, what would happen to Earth?")
five = generate_prediction("If the President Trump never meets with Kim Jong Un ever again, what would be the consequence on world peace?")
gibberish1 = generate_prediction("President Trump Kim Jong Un consequence")
gibberish2 = generate_prediction("what if")
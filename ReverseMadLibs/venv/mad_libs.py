import torch
from pytorch_pretrained_bert import BertTokenizer, BertForMaskedLM

story = [[]]

text = (
      "I would like to say a few _. words about the "
      "most important invetion of the twentieth century. I am not "
      "referring to _. or  evento the dsicovery of _. ."
      "The most _. ivention, in my opion, is the sneaker. "
      "It it were not fo sneakers, our _. would be dirty, "
      " cold, and _. . Sneakers keep me from skidding if the "
      "_.  are slippery, and whenI ru, thy keep me from "
      "stubbing my _. ."
)

# text = (
#     "Shall I _. thee to a summer’s _.? "
#     "Thou art more _. and more temperate: "
#     "_. winds do shake the darling buds of ._, "
#     "And summer’s lease hath all too short a date; "
#     "Sometime too _. the eye of heaven shines, "
#     "And often is his gold _. dimm'd; "
#     "And every _. from fair sometime declines, "
#     "By chance or nature’s changing _. untrimm'd; "
#     "But thy _. summer shall not fade, "
#     "Nor _. possession of that fair thou ow’st; "
#     "Nor shall _. brag thou wander’st in his shade, "
#     "When in eternal _. to time thou grow’st: "
#     "So long as men can _. or eyes can see, "
#     "So long lives this, and this gives _. to thee."
# )

# text = (
#     "Four score and _. years ago our fathers brought forth on this _., a new "
#     "_., conceived in Liberty, and dedicated to the _. that all men are "
#     "created _. . Now we are _. in a great civil war, _. whether that nation "
#     ", or any nation so _. and so dedicated, can _. endure. We are met on a "
#     "great _. of that war. We have come to dedicate a _. of that field, "
#     "as a final resting place for _. who here gave their lives that _. nation "
#     "might live. It is _. fitting and proper that we should do this."
# )

# text = (
#     "Today I went to the zoo. I saw a _. _. jumping up and down in its tree."
#     "He _. through the large tunnel that led to its _. .  I got some peanuts "
#     "and passed them through the cage to a gigantic gray _. towering above my "
#     "head.  Feeding that animal made me hungry.  I went to get a _. scoop of "
#     "ice cream. It filled my stomach.  Afterwards I had to _. _. to catch our bus. "
#     "When I got home I _. my mom for a _. day at the zoo."
# )

# text = (
#     "A vacation is when you take a trip to a _. place with your "
#     "_. family. Usually you go to some place that is near a _. or up "
#     "on a _. . A good vacation is one where you can ride _. or play _. "
#     "or go hunting for _. I like to spend my time _. or _. . When "
#     "parents go on vacation, they spend their time eating three _. a day, "
#     "and fathers play golf, and mothers sit around _. all day"
# )

# Load pre-trained model with masked language model head
bert_version = 'bert-large-uncased'
model = BertForMaskedLM.from_pretrained(bert_version)

# Preprocess text
tokenizer = BertTokenizer.from_pretrained(bert_version)
tokenized_text = tokenizer.tokenize(text)
mask_positions = []
for i in range(len(tokenized_text)):
    if tokenized_text[i] == '_':
        tokenized_text[i] = '[MASK]'
        mask_positions.append(i)

# Predict missing words from left to right
model.eval()
for mask_pos in mask_positions:
    # Convert tokens to vocab indices
    token_ids = tokenizer.convert_tokens_to_ids(tokenized_text)
    tokens_tensor = torch.tensor([token_ids])
    # Call BERT to predict token at this position
    predictions = model(tokens_tensor)[0, mask_pos]
    predicted_index = torch.argmax(predictions).item()
    predicted_token = tokenizer.convert_ids_to_tokens([predicted_index])[0]
    # Update text
    tokenized_text[mask_pos] = predicted_token

for mask_pos in mask_positions:
    tokenized_text[mask_pos] = "_" + tokenized_text[mask_pos] + "_"
print(' '.join(tokenized_text).replace(' ##', ''))

import torch
from pytorch_pretrained_bert import BertTokenizer, BertForMaskedLM

text = (
    "Today, every student has a computer small enough to fit into "
    "his _. He can solve any math problem by simply pushing the "
    "computer's little _. Computers can add, multiply, divide, and "
    "_. They can also _ better than a human. Some computers are "
    "_. Others have an _ screen that shows all kinds of _ and _ "
    "figures. "
)

# text = (
#     "A vacation is when you take a trip to a _. place with your "
#     "_. family. Usually you go to some place that is near a _. or up "
#     "on a _. . A good vacation is one where you can ride _. or play _. "
#     "or go hunting for _. I like to spend my time _. or ._ . When "
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
import torch
from tkinter import *
from tkinter import font
from tkinter.filedialog import askopenfilename
from pytorch_pretrained_bert import BertTokenizer, BertForMaskedLM

# input story
text = (
    "A vacation is when you take a trip to a _. place with your "
    "_. family. Usually you go to some place that is near a _. or up "
    "on a _. . A good vacation is one where you can ride _. or play _. "
    "or go hunting for _. I like to spend my time _. or _. . When "
    "parents go on vacation, they spend their time eating three _. a day, "
    "and fathers play golf, and mothers sit around _. all day"
)


def NewFile():
    print("New File!")


def OpenFile():
    name = askopenfilename()
    print(name)


def About():
    print("This is a simple example of a menu")


def predict():
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
    # print(' '.join(tokenized_text).replace(' ##', ''))
    madlib = (' '.join(tokenized_text).replace(' ##', ''))

    # left = Label(madlibsframe, text=madlib)
    left = Text(madlibsframe, height=10, width=50, wrap=WORD)
    left.configure(font=("Times New Roman", 18, "bold"))
    left.insert(END, madlib)
    left.pack()


# set up main window
root = Tk()
menu = Menu(root)
root.config(menu=menu)
root.title('Reverse Mad Libs')
root.iconbitmap('William_Shakespeare.ico')
root.geometry("800x550")
root['background'] = '#808080'

# Set up the menu
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

# set up orginal story frame
originalframe = LabelFrame(root, text="Original Story")
originalframe.pack(fill="both", expand="yes")

left = Text(originalframe, height=10, width=50, wrap=WORD)
left.configure(font=("Times New Roman", 18, "bold"))
left.insert(END, text)
left.pack()

left.pack(fill=BOTH, expand=True)

getButton = Button(originalframe, text="Get a Story")
getButton.pack(side=LEFT)
genButton = Button(originalframe, text="Generate", command=predict)
genButton.pack(side=LEFT, padx=5, pady=5)

# set up mad lib story frame
madlibsframe = LabelFrame(root, text="Madlibs Story")
madlibsframe.pack(fill="both", expand="yes")

left.pack(fill=BOTH, expand=True)

closeButton = Button(root, text="Close", command=root.quit)

closeButton.pack(side=RIGHT, padx=5, pady=5)

mainloop()

mainloop()

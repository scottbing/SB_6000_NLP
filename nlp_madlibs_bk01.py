import torch
from tkinter import *
from tkinter import font
from tkinter.filedialog import askopenfilename
from pytorch_pretrained_bert import BertTokenizer, BertForMaskedLM

# # input story
# text = (
#     "A vacation is when you take a trip to a _. place with your "
#     "_. family. Usually you go to some place that is near a _. or up "
#     "on a _. . A good vacation is one where you can ride _. or play _. "
#     "or go hunting for _. I like to spend my time _. or _. . When "
#     "parents go on vacation, they spend their time eating three _. a day, "
#     "and fathers play golf, and mothers sit around _. all day"
# )

# set text index
idx = 0
bottom = None

text = (
    (
        "A vacation is when you take a trip to a _. place with your "
        "_. family. Usually you go to some place that is near a _. or up "
        "on a _. . A good vacation is one where you can ride _. or play _. "
        "or go hunting for _. I like to spend my time _. or _. . When "
        "parents go on vacation, they spend their time eating three _. a day, "
        "and fathers play golf, and mothers sit around _. all day"
    ),
    (
        "I can't believe its already _. ! I can't wait to put on  "
        "my _. and visit every _. in my neighborhood.  This year, I "
        "am going to dress up as (a) _. with _. _. .  Before I _. , "
        " I make sure to grab my _. _. to hold all of my _. . "
        "Finally, all of my _. are ready to go! When _. answers the door, "
        "I say, _. or Treat  Yum! I got (a) _. and (a) _. .  We "
        "visit _. houses and decide it's time to _. home.  My _. "
        "says if I eat too much _. , my stomach will _. , so I'll eat "
        "just _. pieces  and go straight to bed.  I hope I'll  have _. "
        "dreams fo _. tonight!  Happy _."
    ),
    (
        "Shall I _. thee to a summer’s _.? "
        "Thou art more _. and more temperate: "
        "_. winds do shake the darling buds of ._, "
        "And summer’s lease hath all too short a date; "
        "Sometime too _. the eye of heaven shines, "
        "And often is his gold _. dimm'd; "
        "And every _. from fair sometime declines, "
        "By chance or nature’s changing _. untrimm'd; "
        "But thy _. summer shall not fade, "
        "Nor _. possession of that fair thou ow’st; "
        "Nor shall _. brag thou wander’st in his shade, "
        "When in eternal _. to time thou grow’st: "
        "So long as men can _. or eyes can see, "
        "So long lives this, and this gives _. to thee."
    ),
    (
        "Four score and _. years ago our fathers brought forth on this _., a new "
        "_., conceived in Liberty, and dedicated to the _. that all men are "
        "created _. . Now we are _. in a great civil war, _. whether that nation "
        ", or any nation so _. and so dedicated, can _. endure. We are met on a "
        "great _. of that war. We have come to dedicate a _. of that field, "
        "as a final resting place for _. who here gave their lives that _. nation "
        "might live. It is _. fitting and proper that we should do this."
    ),
    (
        "Today I went to the zoo. I saw a _. _. jumping up and down in its tree."
        "He _. through the large tunnel that led to its _. .  I got some peanuts "
        "and passed them through the cage to a gigantic gray _. towering above my "
        "head.  Feeding that animal made me hungry.  I went to get a _. scoop of "
        "ice cream. It filled my stomach.  Afterwards I had to _. _. to catch our bus. "
        "When I got home I _. my mom for a _. day at the zoo."
    )
)


def NewFile():
    print("New File!")


def OpenFile():
    name = askopenfilename()
    print(name)


def About():
    print("This is a simple example of a menu")


def predict():
    global bottom
    #Acknowledgment
    #Article: A.I. Plays Mad Libs and the Results are Terrifying
    #Taken From: https://towardsdatascience.com/a-i-plays-mad-libs-and-the-results-are-terrifying-78fa44e7f04e

    # Load pre-trained model with masked language model head
    bert_version = 'bert-large-uncased'
    model = BertForMaskedLM.from_pretrained(bert_version)

    # Preprocess text
    tokenizer = BertTokenizer.from_pretrained(bert_version)
    tokenized_text = tokenizer.tokenize(text[idx])
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
    bottom = Text(madlibsframe, height=10, width=50, wrap=WORD, state=NORMAL)
    bottom.configure(font=("Times New Roman", 18, "bold"))
    bottom.delete(1.0, END)
    bottom.insert(END, madlib)
    bottom.pack()

def getAStory():
    global idx
    global bottom
    idx += 1
    if idx > 4:
        idx = 0

    top.config(state=NORMAL)
    top.delete(1.0, END)
    top.insert(END, text[idx])
    top.pack(fill=BOTH, expand=True)

def clearTextInput():
    top.delete("1.0","end")
    bottom.delete("1.0", "end")



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

top = Text(originalframe, height=10, width=50, wrap=WORD)
top.configure(font=("Times New Roman", 18, "bold"))
top.insert(END, text[idx])
#top.pack()

top.pack(fill=BOTH, expand=True)

getButton = Button(originalframe, text="Get a Story", command=getAStory)
getButton.pack(side=LEFT)
genButton = Button(originalframe, text="Generate", command=predict)
genButton.pack(side=LEFT, padx=5, pady=5)

# set up mad lib story frame
madlibsframe = LabelFrame(root, text="Madlibs Story")
madlibsframe.pack(fill="both", expand="yes")

#left.pack(fill=BOTH, expand=True)

closeButton = Button(root, text="Close", command=root.quit)

closeButton.pack(side=RIGHT, padx=5, pady=5)

mainloop()


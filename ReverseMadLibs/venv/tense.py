from pytorch_pretrained_bert.tokenization import BertTokenizer
tokenizer = BertTokenizer.from_pretrained(args.bert_model, do_lower_case=args.do_lower_case)
def get_tokenized_samples(samples, max_seq_length, tokenizer):
    """
    we assume a function label_map that maps each label to an index or vector encoding. Could also be a dictionary.
    :param samples: we assume struct {.text, .label) 
    :param max_seq_length: the maximal sequence length
    :param tokenizer: BERT tokenizer
    :return: list of features
    """

    features = []
    for sample in samples:
        textlist = sample.text.split(' ')
        labellist = sample.label
        tokens = []
        labels = []
        for i, word in enumerate(textlist):
            token = tokenizer.tokenize(word) #tokenize word according to BERT
            tokens.extend(token)
            label = labellist[i]
            # fit labels to tokenized size of word
            for m in range(len(token)):
                if m == 0:
                    labels.append(label)
                else:
                    labels.append("X")
        # if we exceed max sequence length, cut sample
        if len(tokens) >= max_seq_length - 1:
            tokens = tokens[0:(max_seq_length - 2)]
            labels = labels[0:(max_seq_length - 2)]
            
        ntokens = []
        segment_ids = []
        label_ids = []
        # start with [CLS] token
        ntokens.append("[CLS]")
        segment_ids.append(0)
        label_ids.append(label_map(["[CLS]"]))
        for i, token in enumerate(tokens):
            # append tokens
            ntokens.append(token)
            segment_ids.append(0)
            label_ids.append(label_map(labels[i]))
        # end with [SEP] token
        ntokens.append("[SEP]")
        segment_ids.append(0)
        label_ids.append(label_map(["[SEP]"]))
        # convert tokens to IDs
        input_ids = tokenizer.convert_tokens_to_ids(ntokens)
        # build mask of tokens to be accounted for
        input_mask = [1] * len(input_ids) 
        while len(input_ids) < max_seq_length:
            # pad with zeros to maximal length
            input_ids.append(0)
            input_mask.append(0)
            segment_ids.append(0)
            label_ids.append([0] * (len(label_list) + 1))

        features.append((input_ids,
                              input_mask,
                              segment_ids,
                              label_id))
    return features
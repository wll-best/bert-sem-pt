# coding=utf-8
from main import main


if __name__ == "__main__":

    model_name = "BertOrigin"
    label_list = ['1','2','3','4','5']
    data_dir = "./sem"
    output_dir = ".sem_output/"
    cache_dir = ".sem_cache/"
    log_dir = ".sem_log/"

    # bert-base
    bert_vocab_file = "./bert-base-uncased-vocab.txt"
    bert_model_dir = "./bert-base-uncased"

    # bert_vocab_file = "https://s3.amazonaws.com/models.huggingface.co/bert/bert-base-uncased-vocab.txt"
    # bert_model_dir = "https://s3.amazonaws.com/models.huggingface.co/bert/bert-base-uncased.tar.gz"

    # # bert-large
    # bert_vocab_file = "/search/hadoop02/suanfa/songyingxin/pytorch_Bert/bert-large-uncased-vocab.txt"
    # bert_model_dir = "/search/hadoop02/suanfa/songyingxin/pytorch_Bert/bert-large-uncased"

    if model_name == "BertOrigin":
        from BertOrigin import args

    elif model_name == "BertCNN":
        from BertCNN import args

    elif model_name == 'BertLSTM':
        from BertLSTM import args

    elif model_name == "BertATT":
        from BertATT import args

    elif model_name == "BertRCNN":
        from BertRCNN import args

    elif model_name == "BertCNNPlus":
        from BertCNNPlus import args
    
    elif model_name == "BertDPCNN":
        from BertDPCNN import args

    config = args.get_args(data_dir, output_dir, cache_dir,
                           bert_vocab_file, bert_model_dir, log_dir)

    main(config, config.save_name, label_list)

    #命令行语句
    #python3 run_sem.py --max_seq_length=128 --num_train_epochs=10.0 --do_train --gradient_accumulation_steps=8 --print_step=100  # train and test
    #python3 run_sem.py --max_seq_length=128   # test
        


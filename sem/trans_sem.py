import csv
import matplotlib.pyplot as plt
from pytorch_pretrained_bert.tokenization import BertTokenizer
import numpy as np
import json

def reformat_data(oldfile,newfile):
    #将数据集改造成glove要用的格式，来源：https://github.com/AnubhavGupta3377/Text-Classification-Models-Pytorch
    # import sys
    # import os
    # if __name__ == '__main__':
    #     if len(sys.argv) < 2:
    #         print("Expected filename as an argument")
    #         sys.exit()
    #     filepath = sys.argv[1]
    #     path, filename = os.path.split(filepath)
    #     name, ext = os.path.splitext(os.path.basename(filename))
    #     new_filepath = os.path.join(path, 'processed_' + name + '.txt')
    with open(newfile, 'w', encoding='utf-8') as new_file:
        with open(oldfile, 'r', encoding='utf-8') as old_file:
            for line in old_file:
                # question, number = line.strip().split('\t')
                # y = '2' if float(number) >= 0.5 else '1'
                # label = '__label__' + y
                # new_line = label + ' , ' + question + '\n'
                sentence,labe=line.strip().split('\t')
                label = '__label__' + labe
                new_line = label + ' , ' + sentence + '\n'
                new_file.write(new_line)
    print('Finished')

def trans(input_file, output_file):
    #tsv文件转成json文件
    dump = []
    total = 1
    with open(input_file, 'r', encoding='utf-8') as fh:
        rowes = csv.reader(fh, delimiter='\t')
        for row in rowes:
            idx = str(total)
            label = int(row[1])
            text = row[0]

            dump.append(dict([
                ('idx', idx),
                ('text', text),
                ('label', label)
            ]))
            total += 1
    
    with open(f'{output_file}l', 'w', encoding='utf-8') as f:
        for line in dump:
            json.dump(line, f)
            print('', file=f)

def analysis(filename, type, tokenizer):
    #tsv文件中句子tokenize后的长度分析
    text_lens = []
    with open(filename, "r", encoding='utf-8') as f:
        reader = csv.reader(f, delimiter="\t", quotechar=None)
        for line in reader:
            text = tokenizer.tokenize(line[0])
            text_lens.append(len(text))

    x = list(range(len(text_lens)))

    plt.plot(x, text_lens, label="text length")

    # 设置坐标轴范围
    plt.ylim((0, 100))

    # 设置坐标轴刻度
    y_ticks = np.arange(0,  100, 5)
    plt.yticks(y_ticks)

    plt.title(type)
    plt.ylabel("text length")

    plt.legend()
    plt.show()

if __name__ == "__main__":


    # tokenizer = BertTokenizer.from_pretrained(
    #     "../bert-base-uncased-vocab.txt", do_lower_case=True)
    #
    # analysis("train.tsv", "train", tokenizer)
    # analysis("dev.tsv", "dev", tokenizer)
    # analysis("test.tsv", "test", tokenizer)
    #句子长度在tokenizer之后变小了，那bert到底是看这个还是原句长啊？？？

    #---------以下代码与本程序无关----------
    # trans("train.tsv", "train.json")
    # trans("dev.tsv", "dev.json")
    # trans("test.tsv", "test.json")

    # 将数据集改造-->4.https://github.com/AnubhavGupta3377/Text-Classification-Models-Pytorch
    reformat_data('dev.tsv','processed_dev.txt')
# -*-coding:utf-8 -*-
import csv

def txt2tsv():
    #将 格式为“句子####标签”的txt文件 改成，标题为sentence	label的tsv文件
    with open('dev.tsv', 'w+', newline='', encoding='utf-8') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter= '\t',)  # dialect可用delimiter= ','代替，后面的值是自己想要的符号
        spamwriter.writerow(['sentence','label'])
    # 读要转换的txt文件，文件每行各词间以字符分隔
        with open('Restaurants_All_dev_bdf.txt', 'r', encoding='utf-8') as filein:
            for line in filein:
                line_list = line.strip('\n').split('####')  # 我这里的数据之间是以 tab 间隔的
                spamwriter.writerow(line_list)


if __name__ == "__main__":
    txt2tsv()#改格式
    #查看句子长度

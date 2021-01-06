## Introduction

本仓库专注于 Bert  在文本分类领域的应用， 探索在 Bert 之上如何提高文本分类上的表现。

## Requirements

下面命令还未经过完整测试， 可以参考。

推荐使用 Anconda 来管理包环境， 我采用的是 Anconda python 3.7，其余 3.0 以上应该都可以， 推荐新建一个环境来做测试。

```
conda create -n BertText  # 创建新环境
conda activate BertText   # 激活指定环境

Pytorch ： [conda install pytorch torchvision cudatoolkit=9.0 -c pytorch](https://pytorch.org/get-started/locally/)

scikit-learn： conda install scikit-learn

pytorch-pretrained-BERT： pip install pytorch-pretrained-bert

numpy： conda install numpy

tensorboardx： pip install tensorboardX

tensorflow： pip install tensorflow
```

## 数据集

- 情感分类： 采用 SST-2, 以及 semeval 数据集。

## 关于 Bert 

这里，使用了 [pytorch-pretrained-BERT](https://github.com/huggingface/pytorch-pretrained-BERT) 来加载 Bert 模型， 考虑到国内网速问题，推荐先将相关的 Bert 文件下载，主要有两种文件：
> - vocab.txt: 记录了Bert中所用词表
> - 模型参数： 主要包括预训练模型的相关参数

相关文件下载连接在 [Bert](./Bert.md)

## 实验设置

- 没有删除在单机多卡上的逻辑，只是删除了分布式运算的逻辑，主要是考虑到大多数实验大家都没有必要去用到分布式。
- 删除了采用 fp16 的逻辑， 考虑到文本分类所需的资源并没有那么大， 采用 默认的32位浮点类型在大多数情况下是可以的， 没必要损失精度。其实最主要的还是精简逻辑。
- **注意**： Bert 的参数量随着文本长度的增加呈现接近线性变化的趋势, 测试在单1080ti上， 文本长度设置为150左右已经是极限。
- **注意：** 我有用 tensorboard 将相关的日志信息保存，推荐采用 tensorboard 进行分析。


## Results

### SST-2

python3 run_SST2.py --max_seq_length=65 --num_train_epochs=5.0 --do_train --gpu_ids="1" --gradient_accumulation_steps=8 --print_step=100  # train and test

python3 run_SST2.py --max_seq_length=65   # test
```

| 模型                 | loss  | acc    | f1     |
| -------------------- | ----- | ------ | ------ |
| BertOrigin(base)     | 0.170 | 94.458 | 94.458 |
| BertCNN (5,6) (base) | 0.148 | 94.607 | 94.62  |
| BertATT (base)       | 0.162 | 94.211 | 94.22  |
| BertRCNN (base)      | 0.145 | 95.151 | 95.15  |
| BertCNNPlus (base)   | 0.160 | 94.508 | 94.51  |

```
## 如何适配自己的数据集

对于新的数据集，只需要将你的数据集转化为对应的 tsv 格式：
```
sentence label
```
然后简历一个 `run_your_dataset.py`， 然后模仿 `run_SST2.py` 修改对应的文件夹和`label_list`， 其余的文件完全不需要改动， 不需要设置 `Processor`， 因为我将这部分重新封装了一下。

## 关于保存对应的结果

有同学提出要求能够最终获得 `id, pred_label, true_label` 三元组， 考虑到 Pytorch 中无法使用字符串，因此采用数字0，1，...，n 表示，因此如果是想要对应真实的 id 的话，需要我们将数字与id进行对应，其实很简单， Excel 排个序然后复制粘贴就行。








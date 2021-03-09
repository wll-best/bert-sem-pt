## Introduction

本仓库专注于 Bert  在文本分类领域的应用， 探索在 Bert 之上如何提高文本分类上的表现。

## Requirements

```

Pytorch ： [conda install pytorch torchvision cudatoolkit=9.0 -c pytorch](https://pytorch.org/get-started/locally/)

scikit-learn： conda install scikit-learn

pytorch-pretrained-BERT： pip install pytorch-pretrained-bert

numpy： conda install numpy

tensorboardx： pip install tensorboardX

tensorflow： pip install tensorflow
```

## 数据集

采用sem数据集。

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

## 如何适配自己的数据集

对于新的数据集，只需要将你的数据集转化为对应的 tsv 格式：
```
sentence label
```
然后建立一个 `run_your_dataset.py`， 然后模仿 `run_SST2.py` 修改对应的文件夹和`label_list`， 其余的文件完全不需要改动， 不需要设置 `Processor`， 因为我将这部分重新封装了一下。

## 关于保存对应的结果

有同学提出要求能够最终获得 `id, pred_label, true_label` 三元组， 考虑到 Pytorch 中无法使用字符串，因此采用数字0，1，...，n 表示，因此如果是想要对应真实的 id 的话，需要我们将数字与id进行对应，其实很简单， Excel 排个序然后复制粘贴就行。








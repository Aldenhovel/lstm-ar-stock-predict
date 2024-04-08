# LSTM 自回归股票预测

[![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com)

![s](img/title.png)

## Update

【2024/4/7】

>
>
>- 调整：目录结构`gui`->`web-ui`。
>- 新增：在`web-ui`中使用bat脚本**一键构造venv环境**（这是为了方便直接用户使用，假如您想要研发改进，我依然推荐配置anaconda环境并使用jupyter模式）。

【2024/2/23】

>
>
>- 升级了爬虫，增加对 tushare pro API 的支持，请看 `使用——API配置` 。
>- 旧版的数据 API 已失效，因此删除了无效的代码。
>- 优化了数据样本形式。



## 声明

这个项目并非为了研究金融交易投资工具，实际上这是我研究 Image Caption 任务时突发奇想做的小玩具。因为没有经过经济学或者投资策略上的专业设计，效果不好很正常，你可以自己改进。



### 框架

![s](img/framework.png)



## 数据

**训练数据** 在目录 `data/train/` 下有示例的训练数据，且需要解压。训练数据目录以时间区间为名，其下有大量 `yaml` 文件，每一个文件代表一个股票在某一段时间区间内的走势信息，包含以下字段：

- `date` 采集数据时间。
- `end` 该股票数据的结束时间。
- `code` 该股票代码。
- `stdchange` 该股票在时间区间内的涨跌百分比情况列表。

**测试数据** 在目录 `data/test` 下有示例的测试数据，测试数据也是 `yaml` 文件，其内容格式与训练数据一致，但是直接存放在测试目录下。



## 模型

### Tokenizer

采用了网格化方式将连续区间离散化的形式将股票的涨跌幅映射到 `token id` ，设定涨跌幅有效区间为-10%~10%，分为100格，每格区间为0.2%，通过转换涨跌幅数值为所落在的区间为 `token id` 。此外由于`PAD` 占用了位置0，所有 `token id`需要后移一位。最后将 `token` 补充到相同长度，与原序列长度一起返回。

```python
from utils.Tokenizer import Tokenizer
tk = Tokenizer(grid=100, maxlen=10)

arr = [-9.81,  -1.05, -0.10, 5.26, 15.24]
tk.tokenize(arr)

>>
([1, 1, 45, 50, 77, 101, 0, 0, 0, 0], 5)
```

例如这里 -9.81 在(-10, -9.8] 属于区间0，右移一位得到 `token id` = 1；5.26 在 (5.2, 5.4] 属于区间26，右移一位得到 `token id` = 27；15.24超出了区间因此取区间100，右移一位得到 `token id` = 101。

### LSTM解码器

对于 LSTM 解码器的模型定义在于 `models/LSTMDecoder.py` 中，可以修改其参数实现量化模型大小。训练之后的模型保存至 `checkpoints` 中，我们提供了一个预训练的模型 `model-pretrained.pt` 可以直接使用。

### 推理模块

LSTM的自回归生成式推理过程与训练有点不同，需要融合搜索策略，这里提供了贪婪搜索和波束搜索两种。

**贪婪搜索** 每次将当前阶段概率最大者作为预测结果，直到搜索结束，最后会生成1个预测结果。

**波束搜索** 每次维护一个大小为 `beam_size` 的候选群，直到搜索结束，最后会生成 `beam_size` 个预测结果。



## 使用Jupyter开发

### 环境

**假如您想要直接使用功能，推荐直接使用脚本一键建立`venv`环境，请跳转到【使用图形化界面】。**如果您的目的是继续研究本项目，我们建议使用Anaconda来创建这个运行环境。

```shell
conda create -n tmp python==3.7
conda activate tmp
```

```shell
cd lstm-ar-stock-predict
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
```

### API配置

由于原版的开放 tushare API 已失效，现在需要新的 tushare pro API 来抓取数据，请到 [tushare 官网](https://tushare.pro/)注册申请。将 api token 复制到 `web-ui/config.json` 中。

### 训练与推理

参考 `main.ipynb` 中的示例。

### 获取测试样本

参考 `get_sample.ipynb` 中的示例。



## 使用图形化界面（测试）

![gui](img/gui.png)

### 安装venv虚拟环境

我们在 `web-ui/` 下设计了使用Flask的前后端交互界面，首先配置Python环境：

1. 进入`web-ui/venv/`下双击运行`install_py.bat`，其中会下载Python安装包并弹出安装步骤，使用默认即可。随后会自动安装依赖模块，请耐心等待一切就绪。

2. 安装`venv`环境需要消耗存储空间，如果您是专业人士，可以手动配置Anaconda环境提高模块复用率。
3. 假如您想要卸载虚拟环境，请运行`uninstall_py.bat`，注意这里安装和卸载都仅在本目录下，不会影响系统或其他地方的Python环境，除非您修改了安装和卸载的默认选项（最好不要这样）。

*由于没钱买苹果电脑，这里只在Windows上经过初步设计，如使用MacOS或者遇到问题，请使用Anaconda配置环境吧（尬住）。*

### API配置

由于原版的开放 tushare API 已失效，现在需要新的 tushare pro API 来抓取数据，请到 [tushare 官网](https://tushare.pro/)注册申请。将 api token 复制到 `web-ui/config.json` 中。

### 启动web-ui

当安装完成后，在`web-ui/`下运行`run-web-ui.bat`即可启动网页端图形界面。请点击显示链接或者在浏览器手动打开，一般是 `http://127.0.0.1:5000` 。



## 结果示例

![sample](img/sample01.png)

<hr/>

![sample](img/sample11.png)

<hr/>

![sample](img/sample21.png)

\* @N 表示向后推理N步。



## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=aldenhovel/lstm-ar-stock-predict&type=Date)](https://star-history.com/#aldenhovel/lstm-ar-stock-predict&Date)
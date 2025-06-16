本项目实现了一个 MCP 服务器，工具为`fileEcho()`

被调用后会返回本项目下 **files 文件夹** 内的文件内容

暂时只支持 **txt** 文件

# 快速开始

## 文件准备
比如需要读取 A.txt 和 B.txt 文件，那么保证本项目 files 目录下放置了 A.txt 和 B.txt

```
fileEcho/
│
├── files/                     # 存放文本文件的目录
│   ├── A.txt                  # 需要读取的文件 A
│   └── B.txt                  # 需要读取的文件 B
│
├── server.py                  # 主程序
└── README.md                  # 项目说明文件
```

## 工具准备
安装 uv 工具：https://docs.astral.sh/uv/getting-started/installation/

## 启动 MCP 服务器
安装了`uv`后

运行`uv run server.py`

## MCP 客户端配置示例
```json
{
  "mcpServers": {
    "fileEcho": {
      "url": "http://localhost:5080/sse"
    }
  }
}
```

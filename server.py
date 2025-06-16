from mcp.server.fastmcp import FastMCP

mcp = FastMCP("fileEcho", port=5080)

@mcp.tool()
async def fileEcho() -> str:
    """
    返回目录下的所有 .txt 文件内容，作为聊天记录
    """
    import os

    # 硬编码路径（服务器只会读取该目录下的 txt 文件）
    BASE_DIR = os.path.join(os.getcwd(), "files")

    try:
        # 遍历 BASE_DIR 下所有 .txt 文件
        txt_files = [f for f in os.listdir(BASE_DIR) if f.endswith('.txt') and os.path.isfile(os.path.join(BASE_DIR, f))]

        if not txt_files:
            return "ERROR: No .txt files found."

        content_list = []
        for filename in txt_files:
            file_path = os.path.join(BASE_DIR, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                content_list.append(f"--- {filename} ---\n{content}")

        return "\n".join(content_list)

    except Exception as e:
        return f"ERROR: {str(e)}"
    
if __name__ == '__main__':
    mcp.run(transport="sse")
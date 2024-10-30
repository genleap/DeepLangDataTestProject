import gradio as gr
import traceback


def hello_world_fn(username: str) -> tuple[str, str]:
    try:
        return f"HELLO WORLD\n{username.upper()}", "SUCCESS"
    except Exception as e:
        return f"opus! some exception {e}\n{traceback.format_exc()}", "FAILED"


def html_parser(html: str) -> str:
    result = ''
    start = html.find('<')
    stage = 0
    inside_tag = 0
    while start >=0:
        if 'p>' == html[start+1:start+3]:
            pre = start+3
            stage += 1
        elif '/p>' == html[start+1:start+4]:
            content = html[pre:start].strip()
            if content:
                result += html[pre:start].strip() + '\n'
            stage -= 1
        elif stage > 0:
            if inside_tag <= 0:
                content = html[pre:start].strip()
                if content:
                    result += html[pre:start].strip() + '\n'
            if '/' == html[start+1]:
                inside_tag -= 1
            else:
                inside_tag += 1
            pre = html.find('>', start)+1
        start = html.find('<', start+1)
    return result.strip()
            

def main() -> None:
    with gr.Blocks(title="DeepLang Data test project") as demo:
        with gr.Tab("hello world 0"):
            raw_input = gr.Textbox(lines=1, placeholder="输入你的名字(英文)", label="")
            pack_output = gr.Textbox(label="输出")
            status_output = gr.Textbox(label="状态信息")

            btn = gr.Button("开始转换")
            btn.click(
                fn=hello_world_fn,
                inputs=raw_input,
                outputs=[pack_output, status_output],
            )

        with gr.Tab("hello world 1"):
            raw_input = gr.Textbox(lines=1, placeholder="输入你的名字(英文)", label="")
            pack_output = gr.Textbox(label="输出")
            status_output = gr.Textbox(label="状态信息")

            btn = gr.Button("开始转换")
            btn.click(
                fn=hello_world_fn,
                inputs=raw_input,
                outputs=[pack_output, status_output],
            )

        with gr.Tab("html parser"):
            raw_input = gr.Textbox(lines=10, placeholder="HTML data", label="")
            parse_output = gr.Textbox(label="输出")

            btn = gr.Button("开始转换")
            btn.click(
                fn=html_parser,
                inputs=raw_input,
                outputs=[parse_output],
            )

    demo.queue(default_concurrency_limit=100).launch(
        inline=False,
        debug=False,
        server_name="127.0.0.1",
        server_port=8081,
        show_error=True,
    )


if __name__ == "__main__":
    main()

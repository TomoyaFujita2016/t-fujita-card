import typer
from rich import print
from rich.panel import Panel
from rich.align import Align
from rich.console import Console
from rich.text import Text
from rich.live import Live
from rich.style import Style
from time import sleep

app = typer.Typer()


def create_content():
    content = Text()
    content.append(" \n Tomoya Fujita / t-fujita\n\n", style="bold cyan")
    content.append("    Work:  ", style="green")
    content.append("Software Engineer at 🏠 :)\n", style="yellow")
    content.append("    Freelance: ", style="green")
    content.append("PolarBytes\n\n", style="yellow")
    content.append("    GitHub:   ", style="green")
    content.append("https://github.com/TomoyaFujita2016\n", style="blue underline")
    content.append("    Qiita:    ", style="green")
    content.append("https://qiita.com/TomoyaFujita2016\n", style="blue underline")
    content.append("    PyPI:     ", style="green")
    content.append("https://pypi.org/user/t-fujita\n\n", style="blue underline")
    content.append("    Contact:  ", style="green")
    content.append("t-fujita@polarbytes.jp\n", style="magenta")
    content.append("    Card:     ", style="green")
    content.append("pipx run t-fujita", style="red")
    return content


@app.command()
def main():
    full_content = create_content()
    lines = full_content.split("\n")

    console = Console()

    with Live(console=console, refresh_per_second=20) as live:
        content = Text()
        for line in lines:
            for char in line:
                content.append(char)
                panel = Panel(
                    Align.center(content, vertical="middle"),
                    border_style="white",
                    expand=False,
                )
                live.update(panel)
                sleep(0.02)  # タイピング速度の調整
            content.append("\n")
            live.update(panel)
            sleep(0.1)  # 行の間の短い停止

        for i in range(1, 50):
            panel.border_style = Style(color=f"color({i*5})")
            live.update(panel)
            sleep(0.1)


if __name__ == "__main__":
    app()

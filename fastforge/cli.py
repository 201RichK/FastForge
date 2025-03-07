import typer
from typing import Optional
from pathlib import Path
import rich

app = typer.Typer(
    name="fastforge",
    help="A fast and powerful Python fastapi project generator",
    add_completion=True
)

@app.command()
def new(
    name: str = typer.Argument(..., help="Project name"),
    template: str = typer.Option("basic", help="Template to use (basic, api, fullstack)")
):
    """
    Create a new FastForge project with the chosen structure
    """
    rich.print(f"[bold green]🚀 Creation of project[/bold green] [bold blue]{name}[/bold blue] with the template [bold yellow]{template}[/bold yellow]")

@app.command()
def generate(
    type: str = typer.Argument(..., help="Type of component (controller, model, middleware)"),
    name: str = typer.Argument(..., help="Nom du composant"),
    directory: Optional[Path] = typer.Option(None, help="Dossier de destination")
):
    """
    Generate a new component (controller, model, middleware, etc.)
    """
    rich.print(f"[bold green]✨ Generate new[/bold green] [bold blue]{type}[/bold blue]: [bold yellow]{name}[/bold yellow]")
    if directory:
        rich.print(f"📁 In the directory: {directory}")

@app.command()
def info():
    """
    Display information about the current FastForge project
    """
    rich.print("[bold blue]FastForge[/bold blue] - [italic]A modern framework for your API's[/italic]")
    rich.print("\n[yellow]Commands available:[/yellow]")
    rich.print("  • new     : Create a new project")
    rich.print("  • generate: Generate a new component")
    rich.print("  • info    : Display information about the current project")

if __name__ == "__main__":
    app()
from car_search import find_by_plate, find_by_vin
from query_parser import QueryType, detect_query_type, normalize


from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()


# ── Інтерфейс ────────────────────────────────────────────────────────────────
def show_greeting() -> None:
    console.print(Panel("Вітаю! 👋", border_style="magenta", box=box.DOUBLE))


def show_header() -> None:
    console.print(Panel("Введіть номерний знак або VIN (q — вихід)",
                        border_style="blue", box=box.HEAVY))

def show_error() -> None:
    console.print(Panel("НЕ правильний Номерний знак або VIN",
                        border_style="blue", box=box.ROUNDED))


def show_result(text: str) -> None:
    console.print(Panel(text, title="Відомості", border_style="green",
                        box=box.ROUNDED, padding=(1, 2)))


def main() -> None:
    show_greeting()                              # лише один раз

    while True:
        show_header()
        value = normalize(Prompt.ask("[bold]Номер / VIN[/]").strip())

        if value.lower() == "q":
            break

        query_type = detect_query_type(value)
        if query_type[0] is QueryType.UNKNOWN:
            show_error()
        elif query_type[0] is QueryType.PLATE:
            result = find_by_plate(value)
            show_result(result)
            console.print()
        elif query_type[0] is QueryType.VIN:
            result = find_by_vin(value)
            show_result(result)
            console.print()
                                # далі — знову show_header() без вітання


if __name__ == "__main__":
    main()
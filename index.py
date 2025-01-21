import psutil
import os
import math
import platform

def clear_console():
    """Clear the console."""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def list_active_ports():
    """List all active ports on localhost."""
    connections = psutil.net_connections(kind='inet')
    ports = []
    for conn in connections:
        if conn.laddr and conn.status == 'LISTEN':
            port = conn.laddr.port
            pid = conn.pid
            process_name = psutil.Process(pid).name() if pid else "Unknown"
            ports.append({"port": port, "pid": pid, "name": process_name})
    return ports

def display_ports(ports, page, page_size=5):
    """Display a paginated list of ports."""
    total_pages = math.ceil(len(ports) / page_size)
    start = (page - 1) * page_size
    end = start + page_size
    ports_to_display = ports[start:end]

    clear_console()

    print(f"Page {page}/{total_pages}")
    print("-" * 40)
    print(f"{'Index':<6}{'Port':<10}{'PID':<10}{'Process Name'}")
    print("-" * 40)
    for i, port_info in enumerate(ports_to_display, start=start + 1):
        print(f"{i:<6}{port_info['port']:<10}{port_info['pid']:<10}{port_info['name']}")
    print("-" * 40)

    return total_pages

def terminate_process(pid):
    """Terminate a process using its PID."""
    try:
        os.kill(pid, 9)
        print(f"Process with PID {pid} successfully terminated.")
    except Exception as e:
        print(f"Error terminating the process: {e}")

def main():
    ports = list_active_ports()
    if not ports:
        print("No active ports detected.")
        return

    page = 1
    page_size = 5

    while True:
        total_pages = display_ports(ports, page, page_size)

        print("\nOptions:")
        print("[n] Next page")
        print("[p] Previous page")
        print("[q] Quit")
        print("[index] Terminate the process at the specified index")

        choice = input("\nEnter your choice: ").strip().lower()

        if choice == "n":
            if page < total_pages:
                page += 1
            else:
                print("You are on the last page.")
        elif choice == "p":
            if page > 1:
                page -= 1
            else:
                print("You are on the first page.")
        elif choice == "q":
            clear_console()
            print("Exiting...")
            break
        elif choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(ports):
                port_info = ports[index]
                print(f"Terminating process '{port_info['name']}' on port {port_info['port']}...")
                terminate_process(port_info['pid'])
                ports.pop(index)  # Remove from the list after termination
                page = min(page, math.ceil(len(ports) / page_size) or 1)  # Adjust page if necessary
            else:
                print("Invalid index.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# Localhost Active Ports Manager

This script allows you to:
- List all active ports on `localhost`.
- View process details like port, PID, and process name.
- Terminate processes by selecting them from a clean, paginated list.
- Navigate through the list with pagination.
- Enjoy a clean console display after every action.

## Features

- **List Active Ports**: View all active ports on `localhost` with their associated processes.
- **Clean and Paginated Display**: Easily navigate through a large list of ports with pagination.
- **Process Termination**: Terminate processes by selecting the corresponding index in the list.
- **Cross-Platform Console Clearing**: Works on both Windows and Linux/macOS for a clutter-free experience.

## Prerequisites

### Python Version
Ensure you have **Python 3.6+** installed on your system.

### Required Package
Install the `psutil` library:
```bash
pip install psutil
```

## How to use

1 Go inside the folder
```bash
cd ./localhost-port-tool-main
```
2 Launch the `index.py`
```bash
python index.py
```
3 Follow the Prompts:
> The script will display a paginated list of active ports.
> 
>  Navigate with:
> - [n] to move to the next page.
> - [p] to move to the previous page.
> - [q] to quit the program.
>
> Select a process to terminate by entering the index shown in the list.

### Exemple of interaction:

```bash
Page 1/2
----------------------------------------
Index  Port      PID       Process Name
----------------------------------------
1      8080      12345     python
2      3000      67890     node
3      5432      98765     postgres
4      6379      34567     redis
5      8000      56789     uvicorn
----------------------------------------

Options:
[n] Next page
[p] Previous page
[q] Quit
[index] Terminate the process at the specified index

Enter your choice: 1
Terminating process 'python' on port 8080...
Process with PID 12345 successfully terminated.
```
### Notes:
1 Permissions:
> Administrative/root privileges may be required to terminate certain processes.
>
> Use sudo on Linux/macOS for elevated permissions
```bash
sudo index.py
```
2 Safety
> Avoid terminating critical system processes as this may destabilize your system.
## 🚧End of Readme
Made with ❤️
### License
[MIT](https://choosealicense.com/licenses/mit/)

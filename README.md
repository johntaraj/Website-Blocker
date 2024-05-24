# Host File Blocker

Host File Blocker is a simple GUI application built with Python and Tkinter that allows you to block and unblock websites by modifying the `hosts` file on a Windows system. It provides an easy-to-use interface for managing blocked websites.

## Features

- Block websites by adding entries to the `hosts` file.
- Unblock websites by removing entries from the `hosts` file.
- View a list of currently blocked websites.
- Simple and intuitive GUI built with tkinter.

## Requirements

- Python 3.x

## Installation

1. **Clone the Repository:**
    ```sh
    git clone https://github.com/xota1999/Host-Blocker.git
    cd host-file-blocker
    ```


## Usage

1. **Run the Application:**
    ```sh
    python blocker.py
    ```

2. **Block a Website:**
    - Go to the "Block Website" tab.
    - Enter the website you want to block (e.g., `instagram.com`) in the input field.
    - Click the "Block Website" button.

3. **Unblock a Website:**
    - Go to the "Manage Blocked Websites" tab.
    - View the list of blocked websites.
    - Click the "Remove" button next to the website you want to unblock.

## How It Works

- The application modifies the `hosts` file located at `C:\Windows\System32\drivers\etc\hosts`.
- To block a website, it adds an entry that redirects the domain to `127.0.0.1`.
- To unblock a website, it removes the corresponding entry from the `hosts` file.
- The application backs up the original `hosts` file before making any changes.

## Screenshots

### Block Website Tab
![image](https://github.com/johntaraj/Website-Blocker/assets/134852121/2ad3bbe3-1f61-4830-9d3a-f05f4ba18638)
![image](https://github.com/johntaraj/Website-Blocker/assets/134852121/72d861a2-5af3-4858-bbda-c2656ca0d112)



### Manage Blocked Websites Tab

![image](https://github.com/johntaraj/Website-Blocker/assets/134852121/93a1f2b9-d5d6-4281-a8b9-c69758c0c8e1)
![image](https://github.com/johntaraj/Website-Blocker/assets/134852121/0af8dac3-1ab8-46bb-80f0-33efad2bbb38)


## Notes

- The application requires administrative privileges to modify the `hosts` file. Run your terminal or command prompt as an administrator.
- Changes to the `hosts` file will take effect immediately, but you may need to restart your browser to see the changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or suggestions.

## Acknowledgements

- Inspired by the need for simple website blocking mechanisms for parental control and productivity enhancement.

---

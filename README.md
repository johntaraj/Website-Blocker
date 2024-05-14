# Host File Blocker

Host File Blocker is a simple GUI application built with Python and PyQt5 that allows you to block and unblock websites by modifying the `hosts` file on a Windows system. It provides an easy-to-use interface for managing blocked websites.

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
![image](https://github.com/xota1999/Host-Blocker/assets/73914338/be938170-b11e-4649-bc22-a9c1cdad5ef0)
![image](https://github.com/xota1999/Host-Blocker/assets/73914338/8d20f3a1-5482-420b-a093-da9b2b26818f)


### Manage Blocked Websites Tab
![image](https://github.com/xota1999/Host-Blocker/assets/73914338/f207abeb-64be-49ec-9e93-184483fa9b4e)
![image](https://github.com/xota1999/Host-Blocker/assets/73914338/48fa7729-40a9-4663-9d0b-744c728b3079)

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

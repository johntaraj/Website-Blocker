import os
import subprocess
import sys
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk  # Import ttk from tkinter

# Define the paths to the hosts file and backup file
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
backup_hosts_path = r"C:\Windows\System32\drivers\etc\hosts.bak" 

# Default content for a new hosts file
default_hosts_content = """# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
#
# This file contains the mappings of IP addresses to host names. Each
# entry should be kept on an individual line. The IP address should
# be placed in the first column followed by the corresponding host name.
# The IP address and the host name should be separated by at least one
# space.
#
# Additionally, comments (such as these) may be inserted on individual
# lines or following the machine name denoted by a '#' symbol.
#
# For example:
#
#      102.54.94.97     rhino.acme.com          # source server
#       38.25.63.10     x.acme.com              # x client host
#
# localhost name resolution is handled within DNS itself.
#       127.0.0.1       localhost
#       ::1             localhost
"""

def check_hosts_file():
    if os.path.exists(hosts_path):
        print("Hosts file exists.")
    else:
        print("Hosts file was deleted. Recovering it...")
        with open(hosts_path, 'w') as file:
            file.write(default_hosts_content)
        print("Hosts file has been recovered.")

def block_website(website):
    redirect_ip = "127.0.0.1" 
    
    try:
        # Backup the current hosts file
        with open(hosts_path, 'r') as file:
            content = file.read() 

        with open(backup_hosts_path, 'w') as backup_file:
            backup_file.write(content) 

        # Check if the website is already blocked
        if f"{redirect_ip} {website}" in content or f"{redirect_ip} www.{website}" in content:
            print(f"{website} is already blocked.")
            return

        # Block the website
        with open(hosts_path, 'a') as file:
            if not website.startswith("www."):
                file.write(f"{redirect_ip} www.{website}\n")
            file.write(f"{redirect_ip} {website}\n")

        # Flush DNS cache
        subprocess.run("ipconfig /flushdns", shell=True, check=True)
        print(f"{website} has been blocked.")
    
    except PermissionError:
        print("Permission denied: Please run the script with administrative privileges.")
    except Exception as e:
        print(f"An error occurred: {e}")

def unblock_website(website):
    try:
        with open(hosts_path, 'r') as file:
            lines = file.readlines()

        with open(hosts_path, 'w') as file:
            for line in lines:
                if website not in line and f"www.{website}" not in line:
                    file.write(line) 

        # Flush DNS cache
        subprocess.run("ipconfig /flushdns", shell=True, check=True)
        print(f"{website} has been unblocked.")
    
    except PermissionError:
        print("Permission denied: Please run the script with administrative privileges.")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_blocked_websites():
    blocked_websites = []
    with open(hosts_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if "127.0.0.1" in line and not line.strip().startswith("#"): 
                blocked_websites.append(line.split()[1])
    return blocked_websites

class HostFileBlockerApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Host File Blocker')
        self.geometry('500x400')

        # Main frame with some padding
        main_frame = tk.Frame(self, bg='#f0f0f0', padx=20, pady=20)
        main_frame.pack(expand=True, fill='both')

        self.tab_control = ttk.Notebook(main_frame)  # Create a tab control widget
        self.tab1 = tk.Frame(self.tab_control, bg='#ffffff')
        self.tab2 = tk.Frame(self.tab_control, bg='#ffffff')

        self.tab_control.add(self.tab1, text='Block Website')
        self.tab_control.add(self.tab2, text='Manage Blocked Websites')

        self.tab_control.pack(expand=1, fill='both')

        self.tab1UI()
        self.tab2UI()

    def tab1UI(self):
        tab1_frame = tk.Frame(self.tab1, bg='#ffffff', padx=10, pady=10)
        tab1_frame.pack(expand=True, fill='both')

        self.website_input = tk.Entry(tab1_frame, font=('Arial', 12))
        self.website_input.pack(pady=10, fill='x')

        self.block_button = tk.Button(tab1_frame, text='Block Website', command=self.block_website, bg='#0078d7', fg='#ffffff', font=('Arial', 12))
        self.block_button.pack(pady=10)

    def tab2UI(self):
        tab2_frame = tk.Frame(self.tab2, bg='#ffffff', padx=10, pady=10)
        tab2_frame.pack(expand=True, fill='both')

        self.blocked_websites_frame = tk.Frame(tab2_frame, bg='#f0f0f0')
        self.blocked_websites_frame.pack(pady=10, fill='both', expand=True)

        self.load_blocked_websites()

    def load_blocked_websites(self):
        for widget in self.blocked_websites_frame.winfo_children():
            widget.destroy()

        blocked_websites = get_blocked_websites()
        for website in blocked_websites:
            item_frame = tk.Frame(self.blocked_websites_frame, bg='#ffffff', pady=5, padx=5)
            item_frame.pack(fill='x', pady=2)

            label = tk.Label(item_frame, text=website, anchor='w', bg='#ffffff', font=('Arial', 12))
            label.pack(side='left', expand=True, fill='x')

            remove_button = tk.Button(item_frame, text='Remove', command=lambda w=website: self.unblock_website(w), bg='#d9534f', fg='#ffffff', font=('Arial', 10))
            remove_button.pack(side='right')

    def block_website(self):
        website = self.website_input.get().strip()
        if website:
            block_website(website)
            self.load_blocked_websites()
            messagebox.showinfo('Info', f'{website} has been blocked.\nPlease restart your browser for the changes to take effect.')
        else:
            messagebox.showwarning('Warning', 'Please enter a website to block.')

    def unblock_website(self, website):
        unblock_website(website)
        self.load_blocked_websites()
        messagebox.showinfo('Info', f'{website} has been unblocked.\nPlease restart your browser for the changes to take effect.')

if __name__ == '__main__':
    # Check if hosts file exists
    check_hosts_file()

    app = HostFileBlockerApp()
    app.mainloop()

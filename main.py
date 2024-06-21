import webbrowser

def open_url(url):
    webbrowser.open_new_tab(url)

# Example usage
if __name__ == "__main__":
    url = "fbi.bet"  # Replace with your desired URL
    open_url(url)

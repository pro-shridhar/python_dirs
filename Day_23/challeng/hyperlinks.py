def tidy_link(url, name, hover_text):

    if hover_text:
        string = f'[{name}]({url} "{hover_text}")'
        return string
    else:
        string = f"[{name}]({url})"
        return string

    # "[Google](https://www.google.com "Google Search")"


url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
name = "Click Me!,"
print(tidy_link(url, name, None))

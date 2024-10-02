class BrowsingHistory:
    def __init__(self):
        self.history_stack = []

    def add_page(self, page_url):

        self.history_stack.append(page_url)
        print(f"Added: {page_url}")

    def remove_page(self):

        if not self.is_empty():
            removed_page = self.history_stack.pop()
            print(f"Removed: {removed_page}")
        else:
            print("No pages to remove.")

    def page_count(self):

        return len(self.history_stack)

    def is_empty(self):

        return len(self.history_stack) == 0

    def display_history(self):

        if self.is_empty():
            print("Browsing history is empty.")
        else:
            print("Browsing History:")
            for page in self.history_stack:
                print(page)


browsing_history = BrowsingHistory()


browsing_history.add_page("https://www.youtube.com")
browsing_history.add_page("https://www.google.com")
browsing_history.add_page("https://www.wikipedia.org")


browsing_history.display_history()


print(f"Pages viewed: {browsing_history.page_count()}")


browsing_history.remove_page()

print(f"Is browsing history empty? {browsing_history.is_empty()}")
browsing_history.display_history()

"""Extract all highlighted text of the given HTML file."""

class Extract():
    def __init__(self, html_file):
        self.html_file = html_file
        self.html_fp = open(self.html_file, "r")
        self.highlights_html = []
        self.highlights = []

    def strip_html(self):
        """Remove all unnecessary lines in HTML."""
        save_next = False
        for line in self.html_fp:
            if (save_next):
                self.highlights_html.append(line)
                save_next = False
            if ("<!-- Highlight text -->" in line):
                save_next = True
    
    def clean_highlights(self):
        """Remove HTML from highlight text."""
        START_REGEX = "base\">"
        START_OFFSET = len(START_REGEX)
        END_REGEX = "</span>"

        for h in self.highlights_html:
            start = h.find(START_REGEX) + START_OFFSET
            end = h.find(END_REGEX)
            self.highlights.append(h[start:end])

    def save_highlights_to_file(self):
        FNAME = self.html_file[:-4] + "txt"
        
        f = open(FNAME, "w")
        for h in self.highlights: f.write(h + "\n")


if __name__=="__main__":
    e = Extract("../data/Mans-Search-for-Meaning.html")
    e.strip_html()
    e.clean_highlights()
    e.save_highlights_to_file()

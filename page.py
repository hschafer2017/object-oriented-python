class Page():
    def __init__(self, template, data):
        self.template = template
        self.data = data

    def render(self):
        output_text = self.template
        for k, v in self.data.items():
            change_this = "#" + k + "#"
            output_text = output_text.replace(change_this, v)
        
        return output_text
    
    def save(self, path):
        with open(path, 'w') as f:
            f.write(self.render())

class HTMLPage(Page):
    
    def render(self):
        return '<html>' + Page.render(self) + '</html>'
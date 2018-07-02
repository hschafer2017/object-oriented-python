class Report():
    
    def __init__(self, message):
        self.message = message

    def output(self):
        print(self.message)

    def output_upper(self):
        print(self.message.upper())
        

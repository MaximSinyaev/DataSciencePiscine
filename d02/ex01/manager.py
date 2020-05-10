class Manager:
    def __init__(self, name='Yet another manager'):
        self.name = name

    def __str__(self):
        return self.name

    class Analytics:
        def __str__(self):
            return "Here is my report, please!"

        def working(self):
            raise Exception("I’m working on your report. "
                            "Need a little more time.")

    def make_analysis(self):
        return self.Analytics()

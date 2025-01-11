import npyscreen

class TestApp(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", MainForm, name="Hello World")

class MainForm(npyscreen.Form):
    def create(self):
        self.myText = self.add(npyscreen.TitleText, name="Text:", value="Hello, World!")

if __name__ == "__main__":
    app = TestApp()
    app.run()
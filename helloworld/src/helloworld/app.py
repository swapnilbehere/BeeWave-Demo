"""
This is my first UI app
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import httpx

## This is code for before testing 
"""

def greeting(name):
    if name:
        return f"Hello, {name}"
    else:
        return "Hello, stranger"

"""
# This is after implementing the testing
def greeting(name):
    if name:
        if name == "Brutus":
            return "BeeWare the IDEs of Python!"
        else:
            return f"Hello, {name}"
    else:
        return "Hello, stranger"
class HelloWorld(toga.App):
    def startup(self):
        main_box = toga.Box(style= Pack(direction= COLUMN))
        name_label = toga.Label(
            "Your name: ",
            style=Pack(padding=(0, 5)),
        )
        self.name_input = toga.TextInput(style=Pack(flex=1))
        
        name_box = toga.Box(style= Pack(direction=ROW, padding = 5))
        name_box.add(name_label)
        name_box.add(self.name_input)

        button = toga.Button(
            "Say Hello World!",
            on_press= self.say_hello,
            style=Pack(padding = 5),
        )

        main_box.add(name_box)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    # Button handler function
    async def say_hello(self, widget):
        # PART 1: 
        # this is to print the output in console
        #print(f"Hello, {self.name_input.value} :)")

        # PART 2:
        # instead we will print the output to UI
        '''self.main_window.info_dialog(
            f"Hello, {self.name_input.value}",
            "Hello There, senior!!")
            '''
        # PART 3:
        # Now we will integrate an API call
        async with httpx.AsyncClient() as client:
            response = await client.get("https://jsonplaceholder.typicode.com/posts/42")
        
        payload = response.json()
        
        self.main_window.info_dialog(
            greeting(self.name_input.value),
            payload["body"],
        )
def main():
    return HelloWorld()

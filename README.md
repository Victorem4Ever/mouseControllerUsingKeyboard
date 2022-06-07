# mouseControllerUsingKeyboard
A simple python script that allows you to control your mouse using a keyboard

**How to use :**

Start the python file or :
```python
from controller import Controller

Controller().run()
```

You can change the step like this :
```python
controller = Controller()
controller.pixels = 10 # set the step to 10 pixels
controller.run()
```

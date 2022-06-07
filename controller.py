import threading
import pynput

class Controller(threading.Thread):

	def __init__(self, *args, **kwargs) -> None:
		super().__init__(*args, **kwargs)

		self.__pressed = {

			"Key.up": False,
			"Key.down": False,
			"Key.right": False,
			"Key.left": False,

		}
		self.__mouse = pynput.mouse.Controller()
		self.pixels = 5

	def __on_press(self, key):

		if isinstance(key, pynput.keyboard.KeyCode):
			key = key.char

		else:
			key = str(key)

		if key in self.__pressed.keys():
			self.__pressed[key] = True

		x = self.pixels * self.__pressed["Key.right"] - self.pixels * self.__pressed["Key.left"]
		y = self.pixels * self.__pressed["Key.down"] - self.pixels * self.__pressed["Key.up"]
		self.__mouse.move(x,y)

	def __on_release(self, key):

		if isinstance(key, pynput.keyboard.KeyCode):
			key = key.char

		else:
			key = str(key)

		if key in self.__pressed.keys():
			self.__pressed[key] = False

		if key == "Key.enter":

			self.__mouse.press(pynput.mouse.Button.left)
			self.__mouse.release(pynput.mouse.Button.left)

		elif key == "Key.space":

			self.__mouse.press(pynput.mouse.Button.right)
			self.__mouse.press(pynput.mouse.Button.right)

	def run(self):

		keyboard = pynput.keyboard.Listener(on_press=self.__on_press, on_release=self.__on_release)
		keyboard.start()
		keyboard.join()


if __name__ == "__main__":

	controller = Controller()
	controller.run()
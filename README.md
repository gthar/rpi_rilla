# rpi_rilla

A few simple scripts to do stuff on the Pi

## Includes:
* alarm: Script intended to be a wake-up alarm. When it is called, it turns off the screen and turns of the GPIO-controlled lights. When it is time to wake up, the screen is turned back on, the lights are turned on (for 10 minutes) and a song starts playing. Accepts messages from a socket:
  * snooze: snooze the alarm for 10 more minutes
  * awake: abort the alarm

* alarmctl: used to interact with `alarm` (via a socket)

* gpio_light.py: daemon to control the lights via GPIO. Accepts messages from a socket. These messages are a number, indicating which light (1 or 2) to control followed by a command:
  * on
  * off
  * toggle

* light: communicate with `gpio_light.py`'s socket

* ir_screensaver.py: daemon with screensaver-like functionality. After 10 minutes without detecting movement through the IR sensor, assume there is no-one in the room, and power off the screen to save power. Once it detects movement again, turn it on again to keep the wall display doing its job. Can also manually power off or turn on the screen in response to a socket message.

* screen: communicate with `ir_screensaver.py` (via a socket) to manually power off or turn on the screen

# rpi_rilla

A few simple scripts to do stuff on the Pi

## Includes:
* alarm: Script intended to be a wake-up alarm. When it is called, it turns off the screen and turns of the GPIO-controlled lights. When it is time to wake up, the screen is turned back on, the lights are turned on (for 10 minutes) and a song starts playing. Accepts messages from a socket.
  * snooze: snooze the alarm for 10 more minutes
  * awake: abort the alarm

* alarmctl: used to interact with `alarm` (via a socket)


# Googly Eye Hexpansion!

Add some googly eyes to your badge.  This will work with any 35mm googly eye.

Add side-looking LEDs so you can make the eyes ANGERYY.

Heres a photo!

![a photo of the (v1) hexpansion](photo.jpg)

And here's a render!

![a render of the v2 hexpansion](render.png)

## Some Code!

For the firmware running on the hexpansion, have a look at `app.py`

To flash this, have mpremote open, make sure you have a checkout of
`badge-2024-software` and replace the `prepare_eeprom.py` in modules/scripts/
with the one from here, then run the following:

```
mpremote mount modules + run modules/scripts/prepare_eeprom.py + cp ../badge-2024-addons/thinkl33t/googly-eye-hexpansion/firmware/app.py :/eeprom/app.py + reset
```

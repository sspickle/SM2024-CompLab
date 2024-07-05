export $(ls /dev/cu.usb* | xargs -I {} echo PORT={} | xargs)

ampy -p $PORT put DACBlink.py
ampy -p $PORT put DIOBlink.py
ampy -p $PORT put code.py
ampy -p $PORT put settings.toml
ampy -p $PORT put testBoard.py
ampy -p $PORT ls


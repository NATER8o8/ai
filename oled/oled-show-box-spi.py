import spidev
import RPi.GPIO as GPIO

# Set up SPI
spi = spidev.SpiDev()
spi.open(0, 0)  # Use SPI bus 0, device 0
spi.max_speed_hz = 8000000  # Set SPI speed (adjust as needed)

# Initialize GPIO for D/C (data/command) pin
DC_PIN = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(DC_PIN, GPIO.OUT)

# Clear the display
GPIO.output(DC_PIN, GPIO.LOW)  # Set D/C to command mode
spi.writebytes([0x00, 0xAE])  # Display off
# ... other initialization commands ...

# Draw the box (similar to previous example)
# ...

# Display the box
GPIO.output(DC_PIN, GPIO.HIGH)  # Set D/C to data mode
spi.writebytes([0x40] + [0xFF] * (WIDTH * HEIGHT // 8))  # Send pixel data

# Wait for a few seconds
time.sleep(5)

# Clear the display
# ...

# Close SPI
spi.close()

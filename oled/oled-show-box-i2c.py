# Import necessary libraries
import time
import Adafruit_SSD1306

# Set up the display
WIDTH, HEIGHT = 128, 64
i2c = board.I2C()
oled = Adafruit_SSD1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)

# Clear the display
oled.fill(0)
oled.show()

# Define the coordinates for the 3D box
x1, y1, z1 = 10, 10, 0
x2, y2, z2 = 50, 50, 20

# Draw the box
oled.rectangle((x1, y1, x2, y2), outline=1)  # Front face
oled.line((x1, y1, x2, y1), fill=1)  # Connect front face corners
oled.line((x1, y2, x2, y2), fill=1)
oled.line((x1, y1, x1, y2), fill=1)
oled.line((x2, y1, x2, y2), fill=1)

oled.line((x1, y1, x1 + z2 - z1, y1 - z2 + z1), fill=1)  # Connect front and back faces
oled.line((x2, y1, x2 + z2 - z1, y1 - z2 + z1), fill=1)# Import necessary libraries
import time
import Adafruit_SSD1306

# Set up the display
WIDTH, HEIGHT = 128, 64
i2c = board.I2C()
oled = Adafruit_SSD1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)

# Clear the display
oled.fill(0)
oled.show()

# Define the coordinates for the 3D box
x1, y1, z1 = 10, 10, 0
x2, y2, z2 = 50, 50, 20

# Draw the box
oled.rectangle((x1, y1, x2, y2), outline=1)  # Front face
oled.line((x1, y1, x2, y1), fill=1)  # Connect front face corners
oled.line((x1, y2, x2, y2), fill=1)
oled.line((x1, y1, x1, y2), fill=1)
oled.line((x2, y1, x2, y2), fill=1)

oled.line((x1, y1, x1 + z2 - z1, y1 - z2 + z1), fill=1)  # Connect front and back faces
oled.line((x2, y1, x2 + z2 - z1, y1 - z2 + z1), fill=1)
oled.line((x1, y2, x1 + z2 - z1, y2 - z2 + z1), fill=1)
oled.line((x2, y2, x2 + z2 - z1, y2 - z2 + z1), fill=1)

oled.rectangle((x1 + z2 - z1, y1 - z2 + z1, x2 + z2 - z1, y2 - z2 + z1), outline=1)  # Back face

# Display the box
oled.show()

# Wait for a few seconds
time.sleep(5)

# Clear the display
oled.fill(0)
oled.show()

oled.line((x1, y2, x1 + z2 - z1, y2 - z2 + z1), fill=1)
oled.line((x2, y2, x2 + z2 - z1, y2 - z2 + z1), fill=1)

oled.rectangle((x1 + z2 - z1, y1 - z2 + z1, x2 + z2 - z1, y2 - z2 + z1), outline=1)  # Back face

# Display the box
oled.show()

# Wait for a few seconds
time.sleep(5)

# Clear the display
oled.fill(0)
oled.show()

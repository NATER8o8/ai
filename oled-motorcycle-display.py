# Import modules
import adafruit_ssd1306
import board
import busio
import digitalio
import gpsd
import requests
from PIL import Image, ImageDraw, ImageFont

# Initialize oled display
i2c = busio.I2C(board.SCL, board.SDA)
reset_pin = digitalio.DigitalInOut(board.D4) # any pin!
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, reset=reset_pin)

# Create drawing canvas
canvas = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(canvas)

# Load fonts
small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 8)
large_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)

# Get weather data from API
api_key = "your_api_key" # get your own api key from https://driveweatherapp.com/
base_url = "https://api.driveweatherapp.com/v1/weather"
params = {
    "lat": 40.7128, # your current or destination latitude
    "lon": -74.0060, # your current or destination longitude
    "units": "imperial" # or "metric"
}
response = requests.get(base_url, params=params, headers={"x-api-key": api_key})
data = response.json()

# Get speed and route information from GPS device
gpsd.connect()
packet = gpsd.get_current()
speed = packet.speed() # in meters per second
route = packet.track() # in degrees

# Draw weather information
weather_icon = Image.open(data["icon"]) # load weather icon from API response
draw.bitmap((0, 0), weather_icon, fill=1) # draw weather icon at top left corner
draw.text((32, 0), data["summary"], font=small_font, fill=1) # draw weather summary next to icon
draw.text((32, 16), f"Temp: {data['temperature']}°F", font=small_font, fill=1) # draw temperature below summary
draw.text((32, 24), f"Precip: {data['precipProbability']}%", font=small_font, fill=1) # draw precipitation probability below temperature

# Draw speed and route information
draw.text((0, 32), f"Speed: {speed * 2.237:.1f} mph", font=large_font, fill=1) # draw speed at bottom left corner
draw.text((64, 32), f"Route: {route:.0f}°", font=large_font, fill=1) # draw route at bottom right corner

# Display canvas on oled display
oled.image(canvas)
oled.show()

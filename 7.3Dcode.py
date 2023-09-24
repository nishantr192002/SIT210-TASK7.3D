from time import sleep
from gpiozero import DistanceSensor, PWMOutputDevice

# Create a PWM led on GPIO pin 13
led = PWMOutputDevice(9)

# Create a distance sensor with echo on GPIO 23 and trigger on GPIO 24
distance_sensor = DistanceSensor(echo=23 trigger=24)

# Main function to control the led based on distance
def main():
    running = True
    try:
        # Turn on the led initially
        led.on()
        
        while running:
            # Get the distance from the sensor
            distance = distance_sensor.value
            print(f'Distance: {distance:0.5f} meters')
            
            # Calculate the duty cycle for led intensity
            intensity = round(1.0 - distance, 1)
            
            # Ensure the intensity is not below 0
            if intensity < 0:
                intensity = 0.0
            
            # Set the led pulse
            led.value = intensity
            
            # Sleep for a short duration
            sleep(0.1)
    
    except KeyboardInterrupt:
        pass
    
    finally:
        # Clean up and close the sensor
        running = False
        distance_sensor.close()

if _name_ == '_main_':
    main()
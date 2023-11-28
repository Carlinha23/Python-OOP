"""Python serial number generator."""

class SerialGenerator:



    
  

    def __init__(self, start=0):
        """Initialize the SerialGenerator with a starting value."""
        self.start = start
        self.current = start

    def generate(self):
        """Generate the next serial number."""
        serial_number = self.current
        self.current += 1
        return serial_number

    def reset(self):
        """Reset the serial number to the starting value."""
        self.current = self.start

serial = SerialGenerator
print(serial.generate())
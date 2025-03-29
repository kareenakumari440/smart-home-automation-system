import time

# Simulated smart home devices
class Light:
    def __init__(self, name):
        self.name = name
        self.state = False

    def toggle(self):
        self.state = not self.state
        print(f"{self.name} light is {'on' if self.state else 'off'}.")

class Thermostat:
    def __init__(self, name, temperature):
        self.name = name
        self.temperature = temperature

    def set_temperature(self, temperature):
        self.temperature = temperature
        print(f"{self.name} thermostat set to {self.temperature}°C.")

# Smart home automation logic
def automate_home():
    # Simulated devices
    living_room_light = Light("Living Room")
    kitchen_light = Light("Kitchen")
    thermostat = Thermostat("Living Room", 22.0)

    # Welcome message and available actions
    print("Welcome to the Smart Home Automation System!")
    print("Available Actions:")
    print("1. Toggle Living Room Light")
    print("2. Toggle Kitchen Light")
    print("3. Set Thermostat Temperature")
    print("4. Exit")

    while True:
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            living_room_light.toggle()
        elif choice == '2':
            kitchen_light.toggle()
        elif choice == '3':
            temperature = float(input("Enter desired temperature (in °C): "))
            thermostat.set_temperature(temperature)
        elif choice == '4':
            print("Exiting Smart Home Automation System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    automate_home()
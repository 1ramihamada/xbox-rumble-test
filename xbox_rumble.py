#!/usr/bin/env python3
import sys
import time
import pygame

class RumbleTester:
    def __init__(self):
        # Initialize Pygame and joystick modules
        pygame.init()
        pygame.joystick.init()
        
        # Setup console colors for better visibility
        self.GREEN = '\033[92m'
        self.RED = '\033[91m'
        self.BLUE = '\033[94m'
        self.RESET = '\033[0m'
        
        self.running = True
        self.controller = None
        self.connect_controller()

    def connect_controller(self):
        """Initialize and connect to the first available controller."""
        if pygame.joystick.get_count() == 0:
            print(f"{self.RED}No controllers found!{self.RESET}")
            print("Please connect an Xbox controller and try again.")
            sys.exit(1)

        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()
        print(f"{self.GREEN}Connected to: {self.controller.get_name()}{self.RESET}")

    def show_menu(self):
        """Display the main menu options."""
        print(f"\n{self.BLUE}=== Xbox Controller Rumble Test ==={self.RESET}")
        print("1. Custom rumble test")
        print("2. Quick test (75% intensity)")
        print("3. Stop rumble")
        print("q. Quit")
        print("\nChoice: ", end='', flush=True)

    def get_intensity_input(self, motor=""):
        """Get and validate intensity input from user."""
        while True:
            try:
                intensity = float(input(f"Enter {motor}intensity (0-100%): "))
                if 0 <= intensity <= 100:
                    return intensity / 100.0
                print(f"{self.RED}Please enter a value between 0 and 100{self.RESET}")
            except ValueError:
                print(f"{self.RED}Please enter a valid number{self.RESET}")

    def get_duration_input(self):
        """Get and validate duration input from user."""
        while True:
            try:
                duration = float(input("Enter duration (seconds): "))
                if duration > 0:
                    return duration
                print(f"{self.RED}Duration must be greater than 0{self.RESET}")
            except ValueError:
                print(f"{self.RED}Please enter a valid number{self.RESET}")

    def custom_rumble_test(self):
        """Run a custom rumble test with user-specified parameters."""
        left = self.get_intensity_input("left motor ")
        right = self.get_intensity_input("right motor ")
        duration = self.get_duration_input()

        print(f"\n{self.BLUE}Running custom rumble test...{self.RESET}")
        self.controller.rumble(left, right, int(duration * 1000))
        time.sleep(duration)
        self.controller.stop_rumble()

    def quick_test(self):
        """Run a quick rumble test at 75% intensity."""
        print(f"\n{self.BLUE}Running quick test (75% intensity for 2 seconds)...{self.RESET}")
        self.controller.rumble(0.75, 0.75, 2000)
        time.sleep(2)
        self.controller.stop_rumble()

    def stop_rumble(self):
        """Stop any ongoing rumble effect."""
        self.controller.stop_rumble()
        print(f"\n{self.GREEN}Rumble stopped{self.RESET}")

    def run(self):
        """Main program loop."""
        while self.running:
            self.show_menu()
            
            choice = input().lower()
            
            if choice == '1':
                self.custom_rumble_test()
            elif choice == '2':
                self.quick_test()
            elif choice == '3':
                self.stop_rumble()
            elif choice == 'q':
                self.running = False
            else:
                print(f"{self.RED}Invalid choice!{self.RESET}")

            # Process events to keep controller connection alive
            pygame.event.pump()

    def cleanup(self):
        """Clean up pygame resources."""
        if self.controller:
            self.controller.stop_rumble()
            self.controller.quit()
        pygame.quit()

def main():
    tester = None
    try:
        tester = RumbleTester()
        tester.run()
    except KeyboardInterrupt:
        print("\nExiting...")
    except Exception as e:
        print(f"\nError: {e}")
    finally:
        if tester:
            tester.cleanup()

if __name__ == "__main__":
    main()
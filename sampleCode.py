import threading
import time

# Sample class with an __init__ method
class MyClass:
    def __init__(self, value):
        self.value = value

    def process(self):
        # Simulating some processing within the class method
        for i in range(5):
            print(f"Processing value {self.value} - Step {i+1}")
            time.sleep(1)

# Function to create an instance of MyClass and call its __init__ method
def create_instance(value):
    obj = MyClass(value)
    obj.process()

if __name__ == "__main__":
    value_to_pass = 10  # Value to pass to the MyClass instance

    # Create a thread and pass the __init__ method of MyClass as the target
    thread = threading.Thread(target=MyClass.__init__, args=(MyClass, value_to_pass))
    
    # Start the thread
    thread.start()

    # Wait for the thread to complete
    thread.join()

    print("Thread finished.")
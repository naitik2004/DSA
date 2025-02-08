from sortedcontainers import SortedList  

class NumberContainers:  
    def __init__(self):  
        self.number_to_container = {}  # Maps number to its container  
        self.container_to_numbers = {}  # Maps container to a sorted list of numbers  

    def change(self, number: int, container: int) -> None:  
        # Remove the number from its old container if it exists  
        if number in self.number_to_container:  
            old_container = self.number_to_container[number]  
            if old_container in self.container_to_numbers:  
                self.container_to_numbers[old_container].remove(number)  # Efficient removal from SortedList  
                if not self.container_to_numbers[old_container]:  
                    del self.container_to_numbers[old_container]  # Clean up empty containers  

        # Add the number to the new container  
        if container not in self.container_to_numbers:  
            self.container_to_numbers[container] = SortedList()  
        self.container_to_numbers[container].add(number)  
        self.number_to_container[number] = container  

    def find(self, container: int) -> int:  
        # Return the smallest number in the specified container, or -1 if empty  
        if container in self.container_to_numbers and self.container_to_numbers[container]:  
            return self.container_to_numbers[container][0]  # Access the smallest element directly  
        else:  
            return -1
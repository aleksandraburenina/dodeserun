     class Car:
         def __init__(self, model, color):
             self.model = model
             self.color = color
         
         def show(self) -> None:
             print(f"Model: {self.model}, Color: {self.color}")
     
     # Creating an instance of the Car class
     car1 = Car("Audi A4", "Blue")
     car1.show()  # This will display the model and color of the car
     
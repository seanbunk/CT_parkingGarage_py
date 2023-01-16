class Car:
    def __init__(self, license_plate, model, color):
        self.license_plate = license_plate
        self.model = model
        self.color = color

    def __repr__(self):
        return f"{self.license_plate}, {self.model}, {self.color}"

class Garage:

    def __init__(self):
        self.cars_added = []
        self.spots = 26
        self.car_info = {}
        self.bill = 0

    def spots_available(self):
        return self.spots    

    def add_car(self, car):
        # labeling parking spots
        self.identifier = ['A1','B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'J1', 'K1', 'L1', 'M1', 
        'N1', 'O1', 'P1', 'Q1', 'R1', 'S1', 'T1', 'U1', 'V1', 'W1', 'X1', 'Y1', 'Z1' ]

        if self.spots > 0:
            self.cars_added.append(str(car).split(', '))
            self.spots -= 1
            self.car_info = {'code': [], 'license plate': [], 'model':  [], 'color': []}

            for index, i in enumerate(self.cars_added):
                self.car_info['code'].append(self.identifier[index])
                self.car_info['license plate'].append(i[0])
                self.car_info['model'].append(i[1])
                self.car_info['color'].append(i[2])
            return 'vehicle successfully added to the parking lot'
        else:
            print(f"We have {self.spots} spots available. I am sorry")

    def remove_car(self, given_code, bill_hours):
            past_len = len(self.car_info['code'])
            if given_code not in self.car_info['code']:
                print("We couldn't find your car.  Are you sure you paked here? ")

            else:
                for index, value in enumerate(self.car_info['code']):
                    if value == given_code:
                        print("Your license plate number is: ",self.car_info['license plate'][index])
                        print("Your car is a: ", self.car_info["model"][index])
                        print('Your cars color is: ', self.car_info['color'][index])

                        removed_car_index = self.car_info['code'].pop(index)
                        self.car_info['license plate'].pop(index)
                        self.car_info["model"].pop(index)
                        self.car_info['color'].pop(index)
                        self.spots += 1

            if len(self.car_info['code']) < past_len:
                while True:
                    if bill_hours.isnumeric():
                        list_of_time_and_code = [bill_hours, removed_car_index]
                        break

                    else:
                        print("Your input must be a whole number.  Sample: 6 ")

                    
                    bill_hours = input("Enter how long you were parked in this lot in hours or 'q' to quit:  ")

    
                    if bill_hours in ['q', 'Q']:                    
                        break
        
            if int(list_of_time_and_code[0]) < 26:
                self.bill = int(list_of_time_and_code[0]) * 5
                return f'Your total bill is ${self.bill}'

            else:
                self.bill = int(list_of_time_and_code[0]) * 5 + 100
                return f'Your total bill is ${self.bill}'

    def cars_in_garage(self):
        for i in self.car_info.items():
            print(i)


SeansGarage = Garage()
print(SeansGarage.spots_available())
SeansGarage.add_car(Car('OG420', "Pinto", 'Yellow'))
SeansGarage.add_car(Car('HHT26', 'Honda', "Polka-Dot"))
SeansGarage.add_car(Car('UTYE22', 'Tesla', 'White'))
SeansGarage.cars_in_garage()
print(SeansGarage.remove_car('B1','8'))
print(SeansGarage.spots_available())





    
class User:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        

class Address: 
    def __init__(self, area, city, state):
        self.area = area
        self.city = city
        self.state = state


class GymCenter:
    def __init__(self, center_id, address):
        self.center_id = center_id
        self.address = address 
        self.slots = []
    
    def add_slot(self, slot):
        self.slots.append(slot)    


class WorkoutType:
    def __init__(self, worktype_id, type_name):
        self.worktype_id = worktype_id
        self.type_name = type_name

class Slot:
    def __init__(self, slot_id,  start_time, end_time, center_id):
        self.slot_id = slot_id
        self.start_time = start_time
        self.end_time = end_time
        self.current_capacity = 0
        self.workout_type_list = []

class SlotBooking:
    def __init__(self, slot_id, user_phone):
        self.slot_id = slot_id
        self.user_phone = user_phone        



class CenterHandler:
    def __init__(self):
        self.centers = []
        self.slots = []
        self.workouttype = []

    def add_center(self, gym_center):
        self.centers.append(gym_center)
    
    def add_gym_slot(self, gym_center_id, slot_id):
        for center in self.centers:
            if center.center_id == gym_center_id:
                for slot in self.slots:
                    if slot.slot_id == slot_id:
                        center.slots.append(slot)


class GymService:
    def __init__(self, Center_handler):
        self.users = {}
        self.center_handler = Center_handler
        self.slots = {}

    def user_registration(self, name, phone, email):
        user = User(name = name, phone = phone, email = email)

        #  check this mobile number is already register or not
   
        if phone in self.users.keys():
                print(f"{phone} already exist use another mobile number")
        self.users[phone] = user        
    

    def book_slot(self, slotid, centerid, user_phone_number, workouttype_id):
        # first check this slot and centerid is exist or not
        if (centerid, slotid) in self.slots.keys():
            if len(self.slots[(centerid, slotid)]) > 3:
                print("This slot is full")
            else:
                self.slots[(centerid, slotid)] = self.users[user_phone_number]     













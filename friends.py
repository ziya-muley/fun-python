class Friend:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.birth_month = None
        self.birth_day = None
        self.birth_year = None
        self.phone_number = None

class FriendCollection:
    def __init__(self):
        self.friends = {}

    def addFriend(self, friend):
        self.friends[friend.birth_month] = friend
    
    def getFriendWhoseBirthdayIsInGivenMonth(self, month):
        if month in self.friends:
            return self.friends[month]
        return None
                  
fc = FriendCollection()

friendAnika = Friend()
friendAnika.birth_day = 23
friendAnika.birth_month = 1
friendAnika.birth_year = 2010
friendAnika.first_name = "Anika"
friendAnika.last_name = "Phadnis"
friendAnika.phone_number = "123-456-7890"

friendCharu = Friend()
friendCharu.birth_day = 30
friendCharu.birth_month = 2
friendCharu.birth_year = 2010
friendCharu.first_name = "Charu"
friendCharu.last_name = "123"
friendCharu.phone_number = "123-456-7890"

fc.addFriend(friendAnika)
fc.addFriend(friendCharu)

friend = fc.getFriendWhoseBirthdayIsInGivenMonth(1)
print(friend.first_name + " " + friend.last_name)

friend = fc.getFriendWhoseBirthdayIsInGivenMonth(2)
print(friend.first_name + " " + friend.last_name)

friend = fc.getFriendWhoseBirthdayIsInGivenMonth(3)
if friend is None:
    print("No birthday in this month")
else:
    print(friend.first_name + " " + friend.last_name)
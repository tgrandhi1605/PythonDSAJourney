# Instance
class Instance:
    def __init__(self, name):
        self.name = name

    def realInstance(self):
        print("This is a real instance of class with name: " + self.name)

object = Instance("Tharun")
object.realInstance()

# Class
class User:
    password_policy = {"min_length" : 8, "require_special_char" : True}

    @classmethod
    def updatePasswordPolicy(cls, policy):
        cls.password_policy = policy

print(User.password_policy)
print(User.updatePasswordPolicy({"min_length": 12, "require_special_char": False}))
print(User.password_policy)

# Static
class Password:
    @staticmethod
    def isPasswordStrong(password):
        return len(password) >=8

print(Password.isPasswordStrong(""))
print(Password.isPasswordStrong("Hakunama Tata"))
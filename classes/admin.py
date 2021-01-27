from user import User
from privileges import Privileges


class Admin(User):

    def __init__(self, first_name, last_name, age, dob, *privileges):
        super().__init__(first_name, last_name, age, dob)
        self.privileges = Privileges(*privileges)


admin = Admin('A1', 'B1', 35, '04/19/1985', 'can add post', 'can delete post', 'can ban user')
admin.describe_user()
admin.greet_user()
admin.privileges.show_privileges()

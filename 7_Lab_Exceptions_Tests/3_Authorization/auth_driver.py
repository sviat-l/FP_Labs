"""
Lan 7.3
"""

import auth


# Set up an admin user and permission
auth.authenticator.add_user("admin", "password")
auth.authorizor.add_permission("test program")
auth.authorizor.add_permission("change program")
auth.authorizor.add_permission("own notebook")
auth.authorizor.permit_user("test program", "admin")
auth.authorizor.permit_user("change program", "admin")
auth.authorizor.permit_user("own notebook", "admin")


class Editor:
    def __init__(self):
        self.username = None
        self.menu_map = {
            "login": self.login,
            "sign": self.sign,
            "notebook": self.notebook,
            "test": self.test,
            "change": self.change,
            "quit": self.quit
        }
        self.change_menu = {
            "permit": self.permit,
            "delete": self.delete,
        }

    def is_permitted(self, permission):
        try:
            auth.authorizor.check_permission(permission, self.username)
        except auth.NotLoggedInError as e:
            print("{} is not logged in".format(e.username))
            return False
        except auth.NotPermittedError as e:
            print("{} cannot {}".format(e.username, permission))
            return False
        else:
            return True


    def login(self):
        username = input("username: ")
        password = input("password: ")
        try:
            auth.authenticator.login(username, password)
        except auth.InvalidUsername:
            print("Sorry, username does not exist")
        except auth.InvalidPassword:
            print("Sorry, incorrect password")
        else:
            self.username = username


    def sign(self):
        username = input("username: ")
        password = input("password: ")
        try:
            auth.authenticator.add_user(username, password)
        except auth.UsernameAlreadyExists:
            print("Sorry, Username already exists")
        except auth.PasswordTooShort:
            print("Sorry, too short password")


    def test(self):
        if self.is_permitted("test program"):
            print("Testing program now...")
            print('Users notebooks:')

            for user in auth.authenticator.users:
                print(f'\nUser {user} notebooks:')
                auth.authenticator.users[user].notebook.show_notes()


    def notebook(self):
        if self.is_permitted('own notebook'):
            try:
                auth.authenticator.users[self.username].notebook.run()
            except SystemExit:
                print('Notebook was closed')


    def permit(self):
        username = input("username: ")
        permission = input("permission: ")
        try:
            auth.authorizor.permit_user(permission, username)
        except auth.PermissionError:
            print("Permission doesn't exist")
        except auth.InvalidUsername:
            print("Username doesn't exist")

    def delete(self):
        username = input("username: ")
        if username == self.username:
            print("Unable to delete yourself")
        else:
            try:
                auth.authenticator.delete_user(username)
            except auth.InvalidUsername:
                print("Sorry, that username doesn't exist")

    def quit(self):
        raise SystemExit()


    def menu(self):
        try:
            answer = ""
            while True:
                print(
                    f"""
You are logged in as: {self.username}
Please enter a command:
\tlogin\tLogin
\tsign\tSign up
\tnotebook\tOpen notebook
\ttest\tTest the program
\tchange\tChange the program
\tquit\tQuit
"""
                )
                answer = input("enter a command: ").lower()
                try:
                    func = self.menu_map[answer]
                except KeyError:
                    print("{} is not a valid option".format(answer))
                else:
                    func()
        finally:
            print("Thank you for testing the auth module")


    def change(self):
        if self.is_permitted("change program"):
            print("Changing program now...")
            try:
                answer = ""
                while True:
                    print(
                        f"""
Please enter a command to change a menu:
\tpermit\tAdd permition
\tdelete\tdelete user
\texit\tExit change menu
    """
                    )
                    answer = input("enter a command: ").lower()
                    if answer == 'exit':
                        break
                    try:
                        func = self.change_menu[answer]
                    except KeyError:
                        print("{} is not a valid option".format(answer))
                    else:
                        func()
            finally:
                print('Program was changed')

Editor().menu()

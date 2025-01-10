from os import name
import time

# User class represents each user in the social media app
class User:
    def _init_(self, username, email):
        self.username = username
        self.email = email
        self.posts = []  # List of posts made by the user
        self.following = []  # Users that this user is following
        self.followers = []  # Users following this user

    def make_post(self, content):
        new_post = Post(self, content)
        self.posts.append(new_post)
        return new_post

    def follow(self, user):
        if user != self and user not in self.following:
            self.following.append(user)
            user.followers.append(self)
            print(f"{self.username} is now following {user.username}")
        else:
            print(f"Cannot follow {user.username}.")

    def unfollow(self, user):
        if user in self.following:
            self.following.remove(user)
            user.followers.remove(self)
            print(f"{self.username} unfollowed {user.username}")
        else:
            print(f"You are not following {user.username}.")

# Post class represents a post made by a user
class Post:
    def _init_(self, user, content):
        self.user = user
        self.content = content
        self.timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())

    def _str_(self):
        return f"{self.user.username} posted at {self.timestamp}: {self.content}"

# SocialMediaApp class manages all users and posts in the system
class SocialMediaApp:
    def _init_(self):
        self.users = []  # List of all users in the system
        self.logged_in_user = None

    def register_user(self, username, email):
        for user in self.users:
            if user.username == username:
                print(f"Username '{username}' is already taken!")
                return None
        new_user = User(username, email)
        self.users.append(new_user)
        print(f"User {username} registered successfully!")
        return new_user

    def login(self, username):
        for user in self.users:
            if user.username == username:
                self.logged_in_user = user
                print(f"Welcome back, {username}!")
                return user
        print(f"User {username} not found.")
        return None

    def logout(self):
        if self.logged_in_user:
            print(f"Goodbye, {self.logged_in_user.username}!")
            self.logged_in_user = None
        else:
            print("No user is logged in.")

    def view_feed(self):
        if self.logged_in_user:
            print(f"\n{self.logged_in_user.username}'s Feed:")
            all_posts = []
            # Collect posts from the logged-in user and users they follow
            all_posts.extend(self.logged_in_user.posts)
            for user in self.logged_in_user.following:
                all_posts.extend(user.posts)
            all_posts.sort(key=lambda x: x.timestamp, reverse=True)

            for post in all_posts:
                print(post)
        else:
            print("You need to log in to view the feed.")

    def display_users(self):
        if self.logged_in_user:
            print("\nList of Users:")
            for user in self.users:
                print(f"- {user.username}")
        else:
            print("You need to log in to view the user list.")

# Main function to interact with the application
def main():
    app = SocialMediaApp()
    
    while True:
        print("\n===== Social Media App =====")
        print("1. Register")
        print("2. Login")
        print("3. Logout")
        print("4. Create a Post")
        print("5. Follow User")
        print("6. Unfollow User")
        print("7. View Feed")
        print("8. View Users")
        print("9. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username: ")
            email = input("Enter email: ")
            app.register_user(username, email)

        elif choice == "2":
            username = input("Enter username to log in: ")
            app.login(username)

        elif choice == "3":
            app.logout()

        elif choice == "4":
            if app.logged_in_user:
                content = input("Enter your post content: ")
                app.logged_in_user.make_post(content)
                print("Post created successfully!")
            else:
                print("You need to log in to create a post.")

        elif choice == "5":
            if app.logged_in_user:
                username_to_follow = input("Enter username to follow: ")
                user_to_follow = None
                for user in app.users:
                    if user.username == username_to_follow:
                        user_to_follow = user
                        break
                if user_to_follow:
                    app.logged_in_user.follow(user_to_follow)
                else:
                    print(f"User {username_to_follow} not found.")
            else:
                print("You need to log in to follow users.")

        elif choice == "6":
            if app.logged_in_user:
                username_to_unfollow = input("Enter username to unfollow: ")
                user_to_unfollow = None
                for user in app.users:
                    if user.username == username_to_unfollow:
                        user_to_unfollow = user
                        break
                if user_to_unfollow:
                    app.logged_in_user.unfollow(user_to_unfollow)
                else:
                    print(f"User {username_to_unfollow} not found.")
            else:
                print("You need to log in to unfollow users.")

        elif choice == "7":
            app.view_feed()

        elif choice == "8":
            app.display_users()

        elif choice == "9":
            print("Exiting the app. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")
if name == "_main_":
        main()
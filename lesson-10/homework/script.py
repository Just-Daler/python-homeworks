from datetime import datetime

# ------------------- Task Class -------------------
class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.status = "Incomplete"

    def mark_complete(self):
        self.status = "Complete"

    def __str__(self):
        return f"[{self.status}] {self.title} - {self.description} (Due: {self.due_date.date()})"


# ------------------- ToDoList Class -------------------
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                task.mark_complete()
                print(f"Task '{title}' marked as complete.")
                return
        print(f"Task '{title}' not found.")

    def list_all_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                print(task)

    def list_incomplete_tasks(self):
        incomplete = [task for task in self.tasks if task.status == "Incomplete"]
        if not incomplete:
            print("No incomplete tasks.")
        else:
            for task in incomplete:
                print(task)


# ------------------- Main Program -------------------
def main():
    todo = ToDoList()

    while True:
        print("\n--- ToDo List Menu ---")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. List All Tasks")
        print("4. List Incomplete Tasks")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            try:
                task = Task(title, description, due_date)
                todo.add_task(task)
                print("Task added successfully!")
            except ValueError:
                print("Invalid date format! Please use YYYY-MM-DD.")

        elif choice == "2":
            title = input("Enter task title to mark complete: ")
            todo.mark_task_complete(title)

        elif choice == "3":
            todo.list_all_tasks()

        elif choice == "4":
            todo.list_incomplete_tasks()

        elif choice == "5":
            print("Exiting ToDo List. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")


# ------------------- Run Program -------------------
if __name__ == "__main__":
    main()

#task-2

from datetime import datetime

# ------------------- Post Class -------------------
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.date = datetime.now()

    def edit(self, new_title=None, new_content=None):
        if new_title:
            self.title = new_title
        if new_content:
            self.content = new_content
        print("Post updated successfully.")

    def __str__(self):
        return f"{self.title} by {self.author} on {self.date.strftime('%Y-%m-%d %H:%M')}\n{self.content}"


# ------------------- Blog Class -------------------
class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_all_posts(self):
        if not self.posts:
            print("No posts available.")
        else:
            for post in self.posts:
                print("-" * 50)
                print(post)
                print("-" * 50)

    def list_posts_by_author(self, author):
        author_posts = [p for p in self.posts if p.author.lower() == author.lower()]
        if not author_posts:
            print(f"No posts found by author '{author}'.")
        else:
            for post in author_posts:
                print("-" * 50)
                print(post)
                print("-" * 50)

    def delete_post(self, title):
        for post in self.posts:
            if post.title.lower() == title.lower():
                self.posts.remove(post)
                print(f"Post '{title}' deleted.")
                return
        print(f"Post '{title}' not found.")

    def edit_post(self, title):
        for post in self.posts:
            if post.title.lower() == title.lower():
                new_title = input("Enter new title (leave blank to keep current): ")
                new_content = input("Enter new content (leave blank to keep current): ")
                post.edit(new_title if new_title else None,
                          new_content if new_content else None)
                return
        print(f"Post '{title}' not found.")

    def display_latest_posts(self, count=3):
        if not self.posts:
            print("No posts available.")
        else:
            latest_posts = sorted(self.posts, key=lambda p: p.date, reverse=True)[:count]
            for post in latest_posts:
                print("-" * 50)
                print(post)
                print("-" * 50)


# ------------------- Main Program -------------------
def main():
    blog = Blog()

    while True:
        print("\n--- Simple Blog Menu ---")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. List Posts by Author")
        print("4. Delete Post")
        print("5. Edit Post")
        print("6. Display Latest Posts")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author name: ")
            post = Post(title, content, author)
            blog.add_post(post)
            print("Post added successfully!")

        elif choice == "2":
            blog.list_all_posts()

        elif choice == "3":
            author = input("Enter author name: ")
            blog.list_posts_by_author(author)

        elif choice == "4":
            title = input("Enter title of the post to delete: ")
            blog.delete_post(title)

        elif choice == "5":
            title = input("Enter title of the post to edit: ")
            blog.edit_post(title)

        elif choice == "6":
            count = input("How many latest posts to display? (default=3): ")
            blog.display_latest_posts(int(count) if count.isdigit() else 3)

        elif choice == "7":
            print("Exiting Blog System. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")


# ------------------- Run Program -------------------
if __name__ == "__main__":
    main()

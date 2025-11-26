#!/usr/bin/env python3
"""
To-Do List CLI Application
Roll Number: IMT2023103
"""

import sys
import unittest


class TodoApp:
    """Simple To-Do List application"""
    
    def __init__(self):
        self.todos = []
    
    def add_todo(self, task):
        """Add a new task to the list"""
        self.todos.append(task)
        print(f"Task added: {task}")
    
    def list_todos(self):
        """Display all tasks"""
        if not self.todos:
            print("No tasks available.")
            return
        
        print("\nYour To-Do List:")
        for i, task in enumerate(self.todos, 1):
            print(f"{i}. {task}")
    
    def remove_todo(self, index):
        """Remove a task by index"""
        if 0 <= index < len(self.todos):
            removed = self.todos.pop(index)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")
    
    def get_todo_count(self):
        """Return the number of tasks"""
        return len(self.todos)


class TodoAppTest(unittest.TestCase):
    """Unit tests for TodoApp"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.app = TodoApp()
    
    def test_add_todo(self):
        """Test adding a single todo"""
        self.app.add_todo("Buy groceries")
        self.assertEqual(1, self.app.get_todo_count())
    
    def test_add_multiple_todos(self):
        """Test adding multiple todos"""
        self.app.add_todo("Task 1")
        self.app.add_todo("Task 2")
        self.app.add_todo("Task 3")
        self.assertEqual(3, self.app.get_todo_count())
    
    def test_remove_todo(self):
        """Test removing a todo"""
        self.app.add_todo("Task to remove")
        self.app.remove_todo(0)
        self.assertEqual(0, self.app.get_todo_count())
    
    def test_remove_invalid_index(self):
        """Test removing with invalid index"""
        self.app.add_todo("Task 1")
        self.app.remove_todo(5)
        self.assertEqual(1, self.app.get_todo_count())
    
    def test_empty_list(self):
        """Test empty list initialization"""
        self.assertEqual(0, self.app.get_todo_count())


def run_cli():
    """Run the CLI application"""
    app = TodoApp()
    
    print("=== To-Do List CLI Application ===")
    print("Roll Number: IMT2023103\n")
    
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Choose option: ").strip()
        
        if choice == "1":
            task = input("Enter task: ").strip()
            if task:
                app.add_todo(task)
        elif choice == "2":
            app.list_todos()
        elif choice == "3":
            try:
                num = int(input("Enter task number to remove: ").strip())
                app.remove_todo(num - 1)
            except ValueError:
                print("Invalid number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        # Run tests
        unittest.main(argv=[''], exit=True, verbosity=2)
    else:
        # Run CLI application
        run_cli()

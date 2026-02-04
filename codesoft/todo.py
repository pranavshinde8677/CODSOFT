import json
import os
from datetime import datetime

class TodoList:
    def __init__(self, filename="todo_list.json"):
        self.filename = filename
        self.tasks = self.load_tasks()
        
    def load_tasks(self):
        """Load tasks from JSON file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    return json.load(file)
            except (json.JSONDecodeError, FileNotFoundError):
                return []
        return []
    
    def save_tasks(self):
        """Save tasks to JSON file"""
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)
    
    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_header(self):
        """Display application header"""
        print("=" * 60)
        print("📝 TO-DO LIST MANAGER".center(60))
        print("=" * 60)
    
    def display_menu(self):
        """Display main menu"""
        print("\n" + "-" * 60)
        print("MAIN MENU:")
        print("-" * 60)
        print("1. 📋 View All Tasks")
        print("2. ➕ Add New Task")
        print("3. ✏️  Update Task")
        print("4. ✅ Mark Task as Complete")
        print("5. ❌ Delete Task")
        print("6. 🔍 Search Tasks")
        print("7. 📊 View Statistics")
        print("8. 💾 Save & Exit")
        print("9. 🚫 Exit Without Saving")
        print("-" * 60)
    
    def add_task(self):
        """Add a new task"""
        self.clear_screen()
        print("\n" + "➕ ADD NEW TASK".center(60, "-"))
        
        title = input("\nEnter task title: ").strip()
        if not title:
            print("❌ Task title cannot be empty!")
            input("\nPress Enter to continue...")
            return
        
        description = input("Enter task description (optional): ").strip()
        due_date = input("Enter due date (DD-MM-YYYY, optional): ").strip()
        priority = input("Enter priority (1-High, 2-Medium, 3-Low): ").strip()
        
        # Validate priority
        if priority not in ['1', '2', '3']:
            priority = '2'
        
        priority_map = {'1': 'High', '2': 'Medium', '3': 'Low'}
        
        task = {
            'id': len(self.tasks) + 1,
            'title': title,
            'description': description,
            'due_date': due_date if self.validate_date(due_date) else None,
            'priority': priority_map[priority],
            'status': 'Pending',
            'created_at': datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            'completed_at': None
        }
        
        self.tasks.append(task)
        print(f"\n✅ Task '{title}' added successfully!")
        input("\nPress Enter to continue...")
    
    def validate_date(self, date_str):
        """Validate date format"""
        if not date_str:
            return False
        try:
            datetime.strptime(date_str, "%d-%m-%Y")
            return True
        except ValueError:
            return False
    
    def view_tasks(self, tasks=None, title="ALL TASKS"):
        """Display tasks"""
        self.clear_screen()
        if tasks is None:
            tasks = self.tasks
        
        print(f"\n📋 {title}".center(60, "-"))
        
        if not tasks:
            print("\n📭 No tasks found!")
        else:
            pending_count = sum(1 for task in tasks if task['status'] == 'Pending')
            completed_count = sum(1 for task in tasks if task['status'] == 'Completed')
            
            print(f"\n📊 Summary: {pending_count} Pending | {completed_count} Completed")
            print("-" * 60)
            
            for task in tasks:
                status_icon = "✅" if task['status'] == 'Completed' else "⏳"
                priority_icon = "🔴" if task['priority'] == 'High' else "🟡" if task['priority'] == 'Medium' else "🟢"
                
                print(f"\n{status_icon} Task #{task['id']}: {task['title']}")
                print(f"   Priority: {priority_icon} {task['priority']}")
                print(f"   Status: {task['status']}")
                
                if task['description']:
                    print(f"   Description: {task['description']}")
                
                if task['due_date']:
                    due_status = " (Overdue)" if self.is_overdue(task['due_date']) else ""
                    print(f"   Due Date: {task['due_date']}{due_status}")
                
                if task['status'] == 'Completed' and task['completed_at']:
                    print(f"   Completed: {task['completed_at']}")
                
                print(f"   Created: {task['created_at']}")
                print("-" * 60)
        
        input("\nPress Enter to continue...")
    
    def is_overdue(self, due_date):
        """Check if task is overdue"""
        try:
            due = datetime.strptime(due_date, "%d-%m-%Y")
            return due.date() < datetime.now().date()
        except:
            return False
    
    def update_task(self):
        """Update an existing task"""
        self.view_tasks()
        
        try:
            task_id = int(input("\nEnter Task ID to update: "))
            task = next((t for t in self.tasks if t['id'] == task_id), None)
            
            if not task:
                print(f"❌ Task with ID {task_id} not found!")
                input("\nPress Enter to continue...")
                return
            
            print(f"\nUpdating Task #{task_id}: {task['title']}")
            print("-" * 40)
            
            print("\nLeave field blank to keep current value:")
            new_title = input(f"New title [{task['title']}]: ").strip()
            new_desc = input(f"New description [{task['description']}]: ").strip()
            new_due = input(f"New due date (DD-MM-YYYY) [{task['due_date']}]: ").strip()
            
            if new_title:
                task['title'] = new_title
            if new_desc:
                task['description'] = new_desc
            if new_due:
                if self.validate_date(new_due):
                    task['due_date'] = new_due
                else:
                    print("❌ Invalid date format! Date not updated.")
            
            print("\nPriority levels:")
            print("1. High 🔴")
            print("2. Medium 🟡")
            print("3. Low 🟢")
            new_priority = input(f"New priority (1-3) [{task['priority']}]: ").strip()
            
            if new_priority in ['1', '2', '3']:
                priority_map = {'1': 'High', '2': 'Medium', '3': 'Low'}
                task['priority'] = priority_map[new_priority]
            
            print(f"\n✅ Task #{task_id} updated successfully!")
            
        except ValueError:
            print("❌ Please enter a valid Task ID!")
        except Exception as e:
            print(f"❌ Error: {e}")
        
        input("\nPress Enter to continue...")
    
    def mark_complete(self):
        """Mark a task as complete"""
        pending_tasks = [t for t in self.tasks if t['status'] == 'Pending']
        self.view_tasks(pending_tasks, "PENDING TASKS")
        
        try:
            task_id = int(input("\nEnter Task ID to mark as complete: "))
            task = next((t for t in self.tasks if t['id'] == task_id), None)
            
            if not task:
                print(f"❌ Task with ID {task_id} not found!")
            elif task['status'] == 'Completed':
                print(f"⚠️ Task #{task_id} is already completed!")
            else:
                task['status'] = 'Completed'
                task['completed_at'] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                print(f"\n✅ Task '{task['title']}' marked as complete!")
                
        except ValueError:
            print("❌ Please enter a valid Task ID!")
        
        input("\nPress Enter to continue...")
    
    def delete_task(self):
        """Delete a task"""
        self.view_tasks()
        
        try:
            task_id = int(input("\nEnter Task ID to delete: "))
            task = next((t for t in self.tasks if t['id'] == task_id), None)
            
            if not task:
                print(f"❌ Task with ID {task_id} not found!")
            else:
                confirm = input(f"\nAre you sure you want to delete '{task['title']}'? (y/n): ").lower()
                if confirm == 'y':
                    self.tasks = [t for t in self.tasks if t['id'] != task_id]
                    # Reassign IDs
                    for idx, task in enumerate(self.tasks, 1):
                        task['id'] = idx
                    print(f"\n✅ Task deleted successfully!")
                else:
                    print("\n❌ Deletion cancelled!")
        
        except ValueError:
            print("❌ Please enter a valid Task ID!")
        
        input("\nPress Enter to continue...")
    
    def search_tasks(self):
        """Search tasks by keyword"""
        self.clear_screen()
        print("\n🔍 SEARCH TASKS".center(60, "-"))
        
        keyword = input("\nEnter search keyword (title or description): ").strip().lower()
        
        if not keyword:
            print("❌ Please enter a search keyword!")
            input("\nPress Enter to continue...")
            return
        
        results = []
        for task in self.tasks:
            if (keyword in task['title'].lower() or 
                keyword in task['description'].lower()):
                results.append(task)
        
        if results:
            self.view_tasks(results, f"SEARCH RESULTS FOR '{keyword}'")
        else:
            print(f"\n📭 No tasks found containing '{keyword}'")
            input("\nPress Enter to continue...")
    
    def view_statistics(self):
        """Display task statistics"""
        self.clear_screen()
        print("\n📊 TASK STATISTICS".center(60, "-"))
        
        if not self.tasks:
            print("\n📭 No tasks available!")
            input("\nPress Enter to continue...")
            return
        
        total_tasks = len(self.tasks)
        pending_tasks = sum(1 for t in self.tasks if t['status'] == 'Pending')
        completed_tasks = sum(1 for t in self.tasks if t['status'] == 'Completed')
        
        high_priority = sum(1 for t in self.tasks if t['priority'] == 'High')
        medium_priority = sum(1 for t in self.tasks if t['priority'] == 'Medium')
        low_priority = sum(1 for t in self.tasks if t['priority'] == 'Low')
        
        overdue_tasks = 0
        for task in self.tasks:
            if task['due_date'] and task['status'] == 'Pending' and self.is_overdue(task['due_date']):
                overdue_tasks += 1
        
        completion_rate = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
        
        print(f"\n📈 Overall Statistics:")
        print(f"   Total Tasks: {total_tasks}")
        print(f"   Pending: {pending_tasks}")
        print(f"   Completed: {completed_tasks}")
        print(f"   Completion Rate: {completion_rate:.1f}%")
        
        print(f"\n🎯 Priority Distribution:")
        print(f"   High 🔴: {high_priority}")
        print(f"   Medium 🟡: {medium_priority}")
        print(f"   Low 🟢: {low_priority}")
        
        print(f"\n⚠️  Overdue Tasks: {overdue_tasks}")
        
        if completed_tasks > 0:
            completed_dates = []
            for task in self.tasks:
                if task['completed_at']:
                    try:
                        date_str = task['completed_at'].split()[0]  # Get date part only
                        completed_dates.append(datetime.strptime(date_str, "%d-%m-%Y"))
                    except:
                        pass
            
            if completed_dates:
                latest_completion = max(completed_dates)
                print(f"\n📅 Latest Completion: {latest_completion.strftime('%d-%m-%Y')}")
        
        input("\nPress Enter to continue...")
    
    def run(self):
        """Main application loop"""
        self.clear_screen()
        
        while True:
            self.clear_screen()
            self.display_header()
            self.display_menu()
            
            try:
                choice = input("\nEnter your choice (1-9): ").strip()
                
                if choice == '1':
                    self.view_tasks()
                elif choice == '2':
                    self.add_task()
                elif choice == '3':
                    self.update_task()
                elif choice == '4':
                    self.mark_complete()
                elif choice == '5':
                    self.delete_task()
                elif choice == '6':
                    self.search_tasks()
                elif choice == '7':
                    self.view_statistics()
                elif choice == '8':
                    self.save_tasks()
                    print("\n💾 Tasks saved successfully!")
                    print("👋 Thank you for using To-Do List Manager!")
                    break
                elif choice == '9':
                    confirm = input("\n⚠️  Exit without saving? All changes will be lost! (y/n): ").lower()
                    if confirm == 'y':
                        print("\n👋 Thank you for using To-Do List Manager!")
                        break
                else:
                    print("❌ Invalid choice! Please enter 1-9")
                    input("\nPress Enter to continue...")
                    
            except KeyboardInterrupt:
                print("\n\n⚠️  Interrupted by user!")
                save = input("Save changes before exiting? (y/n): ").lower()
                if save == 'y':
                    self.save_tasks()
                    print("💾 Tasks saved successfully!")
                print("👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ An error occurred: {e}")
                input("\nPress Enter to continue...")

def main():
    """Main function"""
    print("🚀 Starting To-Do List Manager...")
    
    # Check for data file
    if not os.path.exists("todo_list.json"):
        print("📁 Creating new data file...")
    
    # Create and run the application
    app = TodoList()
    app.run()

if __name__ == "__main__":
    main()
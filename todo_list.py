# todo_list.py

# Skapa en tom lista för att lagra uppgifterna
tasks = []

def add_task(task_name):
    """Lägger till en ny uppgift i listan."""
    tasks.append(task_name)
    print(f"'{task_name}' har lagts till i din att-göra-lista.")

def view_tasks():
    """Visar alla uppgifter i listan."""
    if not tasks:
        print("Din att-göra-lista är tom.")
    else:
        print("--- Din att-göra-lista ---")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print("--------------------------")

def delete_task(task_number):
    """Tar bort en uppgift från listan baserat på dess nummer."""
    try:
        # Justera numret till listans index (som börjar på 0)
        index_to_delete = int(task_number) - 1
        
        if 0 <= index_to_delete < len(tasks):
            removed_task = tasks.pop(index_to_delete)
            print(f"'{removed_task}' har tagits bort från listan.")
        else:
            print("Ogiltigt uppgiftsnummer. Vänligen försök igen.")
    except (ValueError, IndexError):
        print("Ogiltigt input. Vänligen ange ett giltigt nummer.")

def main():
    """Huvudfunktionen som kör programmet."""
    while True:
        print("\nVad vill du göra?")
        print("1. Lägg till en uppgift")
        print("2. Visa alla uppgifter")
        print("3. Ta bort en uppgift")
        print("4. Avsluta")
        
        choice = input("Välj ett alternativ (1-4): ")
        
        if choice == '1':
            task_name = input("Ange uppgift att lägga till: ")
            add_task(task_name)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            view_tasks()
            if tasks:
                task_number = input("Ange numret på uppgiften du vill ta bort: ")
                delete_task(task_number)
        elif choice == '4':
            print("Programmet avslutas. Hejdå!")
            break
        else:
            print("Ogiltigt val. Vänligen välj ett nummer mellan 1 och 4.")

# Kör programmet när filen exekveras
if __name__ == "__main__":
    main()

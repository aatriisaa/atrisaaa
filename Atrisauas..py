class EmployeeNode:
    # Membuat node untuk setiap pegawai
    def __init__(self, id=None, name=None, age=None):
        self.id = id
        self.name = name
        self.age = age
        self.next = None

class EmployeeLinkedList:
    # Membuat linked list untuk menyimpan data pegawai
    def __init__(self):
        self.head = None

    def append(self, id, name, age):
        # Menambahkan node baru ke linked list
        new_node = EmployeeNode(id, name, age)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        # Menampilkan data pegawai dalam linked list
        current = self.head
        while current:
            print(f"ID: {current.id}, Name: {current.name}, Age: {current.age}")
            current = current.next

    def delete_by_id(self, id):
        # Menghapus node dari linked list berdasarkan ID
        current = self.head
        if current and current.id == id:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.id != id:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        current = None

    def sort_by_name(self):
        # Mengurutkan linked list berdasarkan nama pegawai
        if not self.head or not self.head.next:
            return  
        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            if not sorted_list or sorted_list.name > current.name:
                current.next = sorted_list
                sorted_list = current
            else:
                temp = sorted_list
                while temp.next and temp.next.name < current.name:
                    temp = temp.next
                current.next = temp.next
                temp.next = current
            current = next_node
        self.head = sorted_list

class EmployeeStack:
    # Membuat stack untuk menyimpan data pegawai
    def __init__(self):
        self.stack = []

    def push(self, employee):
        # Menambahkan pegawai ke stack
        self.stack.append(employee)

    def pop(self):
        # Menghapus pegawai dari stack
        if not self.stack:
            return None
        return self.stack.pop()

    def display(self):
        # Menampilkan data pegawai dalam stack
        for emp in self.stack:
            print(f"ID: {emp.id}, Name: {emp.name}, Age: {emp.age}")

class EmployeeQueue:
    # Membuat queue untuk menyimpan data pegawai
    def __init__(self):
        self.queue = []

    def enqueue(self, employee):
        # Menambahkan pegawai ke queue
        self.queue.append(employee)

    def dequeue(self):
        # Menghapus pegawai dari queue
        if not self.queue:
            return None
        return self.queue.pop(0)

    def display(self):
        # Menampilkan data pegawai dalam queue
        for emp in self.queue:
            print(f"ID: {emp.id}, Name: {emp.name}, Age: {emp.age}")

# Data Pegawai
employees = [
    EmployeeNode(1, "Atrisa", 30),
    EmployeeNode(2, "Anggy", 25),
    EmployeeNode(3, "delvina", 28),
]

# Linked List
print("Linked List:")
ll = EmployeeLinkedList()
for emp in employees:
    # Menambahkan data pegawai ke linked list
    ll.append(emp.id, emp.name, emp.age)
ll.display()
print("\nSorted Linked List by Name:")
ll.sort_by_name()
ll.display()

# Stack
print("\nStack:")
stack = EmployeeStack()
for emp in employees:
    # Menambahkan data pegawai ke stack
    stack.push(emp)
stack.display()
print("\nPop from Stack:")
# Menghapus data pegawai dari stack
stack.pop()
stack.display()

# Queue
print("\nQueue:")
queue = EmployeeQueue()
for emp in employees:
    # Menambahkan data pegawai ke queue
    queue.enqueue(emp)
queue.display()
print("\nDequeue from Queue:")
# Menghapus data pegawai dari queue
queue.dequeue()
queue.display()

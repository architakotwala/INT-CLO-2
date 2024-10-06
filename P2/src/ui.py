# src/ui.py
import tkinter as tk
from load_balancer import load_balancer, on_prem_node, cloud_node
def allocate_resources():
    cpu = int(cpu_entry.get())
    memory = int(memory_entry.get())
    result = load_balancer(cpu, memory)
    result_label.config(text=result)
    on_prem_label.config(text=str(on_prem_node))
    cloud_label.config(text=str(cloud_node))
root = tk.Tk()
root.title("Resource Allocation Simulation")
# Labels and input fields
cpu_label = tk.Label(root, text="CPU Demand:")
cpu_label.pack()
cpu_entry = tk.Entry(root)
cpu_entry.pack()
memory_label = tk.Label(root, text="Memory Demand:")
memory_label.pack()
memory_entry = tk.Entry(root)
memory_entry.pack()
# Allocate button
allocate_button = tk.Button(root, text="Allocate", command=allocate_resources)
allocate_button.pack()
# Result and Node display labels
result_label = tk.Label(root, text="")
result_label.pack()
on_prem_label = tk.Label(root, text=str(on_prem_node))
on_prem_label.pack()

cloud_label = tk.Label(root, text=str(cloud_node))
cloud_label.pack()

root.mainloop()
cpu = int(cpu_entry.get())  # Assuming you have an Entry widget for CPU input
memory = int(memory_entry.get())  # Assuming you have an Entry widget for Memory input
result = load_balancer(cpu, memory)



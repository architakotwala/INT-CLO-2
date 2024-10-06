# src/load_balancer.py
from resource import Node, Resource
# Initialize nodes (on-premises and cloud)
on_prem_node = Node("On-Premises")
cloud_node = Node("Cloud")
# Add resources
on_prem_node.add_resource(Resource("CPU", 100))  # 100 units of CPU
on_prem_node.add_resource(Resource("Memory", 200))  # 200 units of Memory

cloud_node.add_resource(Resource("CPU", 200))  # 200 units of CPU
cloud_node.add_resource(Resource("Memory", 400))  # 400 units of Memory
def load_balancer(demand_cpu, demand_memory):
    try:
        # Try to allocate resources on-premises first
        on_prem_node.allocate_resource("CPU", demand_cpu)
        on_prem_node.allocate_resource("Memory", demand_memory)
        return "Resources allocated on-premises."
    except ValueError:
        # If on-premises fails, allocate resources to cloud
        cloud_node.allocate_resource("CPU", demand_cpu)
        cloud_node.allocate_resource("Memory", demand_memory)
        return "On-premises overloaded, allocated to cloud."
def release_resources(cpu, memory):
    try:
        on_prem_node.release_resource("CPU", cpu)
        on_prem_node.release_resource("Memory", memory)
        return "Resources released from on-premises."
    except ValueError:
        cloud_node.release_resource("CPU", cpu)
        cloud_node.release_resource("Memory", memory)
        return "Released from cloud."
def load_balancer(cpu, memory):
    try:
        on_prem_node.allocate_resource("CPU", cpu)
    except ValueError as e:
        print(f"On-premises node error: {e}")
        try:
            cloud_node.allocate_resource("CPU", cpu)
        except ValueError as e:
            print(f"Cloud node error: {e}")
            raise ValueError(f"Cannot allocate {cpu}. Exceeds total available capacity.")

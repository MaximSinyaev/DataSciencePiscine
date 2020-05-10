class Scaler:
    def __init__(self, nodes_list, cluster_management, nodes, ram, cpu):
        self.nodes_list = nodes_list
        self.num = nodes
        self.cluster_management = cluster_management
        self.cpu_per_node = cpu
        self.ram_per_node = cpu

    def get_params(self):
        full_cpu = self.num * self.cpu_per_node
        full_ram = self.num * self.ram_per_node
        # functions to get cluster params
        free_cpu = 0
        free_ram = 0
        return {'cpu': (full_cpu - free_cpu) / full_cpu,
                'ram': (full_ram - free_ram) / full_ram}

    
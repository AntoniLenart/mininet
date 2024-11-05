from mininet.topo import Topo


class MyTopo(Topo):
    def build(self):
        # Define nodes (switches and hosts)
        cities = [
            "Oslo", "Stockholm", "Copenhage", "Warsaw", "Berlin", "Hamburg",
            "Amsterdam", "Brussels", "London", "Paris", "Glasgow", "Dublin",
            "Frankfurt", "Strasbour", "Zurich", "Munich", "Prague", "Vienna",
            "Budapest", "Lyon", "Milan", "Zagreb", "Rome", "Madrid",
            "Bordeaux", "Barcelona", "Belgrade", "Athens"
        ]

        switches = {}
        hosts = {}

        # Add switches and hosts, with unique DPIDs for switches
        for idx, city in enumerate(cities, start=1):
            # Create a unique DPID in hexadecimal format
            dpid = f"{idx:04x}"  # 4-digit hex DPID (e.g., 0001)
            switch = self.addSwitch(f's{city}', dpid=dpid, stp=True)
            host = self.addHost(f'h{city}')
            self.addLink(switch, host)  # Link between switch and host
            switches[city] = switch

        # Define links between switches based on topology
        links = [
            ("Oslo", "Stockholm"),
            ("Oslo", "Copenhage"),
            ("Copenhage", "Berlin"),
            ("Stockholm", "Warsaw"),
            ("Warsaw", "Budapest"),
            ("Warsaw", "Berlin"),
            ("Budapest", "Belgrade"),
            ("Budapest", "Prague"),
            ("Belgrade", "Athens"),
            ("Belgrade", "Zagreb"),
            ("Athens", "Rome"),
            ("Rome", "Zagreb"),
            ("Rome", "Milan"),
            ("Zagreb", "Vienna"),
            ("Vienna", "Prague"),
            ("Vienna", "Munich"),
            ("Prague", "Berlin"),
            ("Berlin", "Hamburg"),
            ("Berlin", "Munich"),
            ("Hamburg", "Amsterdam"),
            ("Hamburg", "Frankfurt"),
            ("Frankfurt", "Strasbour"),
            ("Frankfurt", "Munich"),
            ("Frankfurt", "Brussels"),
            ("Amsterdam", "Brussels"),
            ("Milan", "Munich"),
            ("Milan", "Zurich"),
            ("Zurich", "Strasbour"),
            ("Zurich", "Lyon"),
            ("Strasbour", "Paris"),
            ("Lyon", "Paris"),
            ("Lyon", "Barcelona"),
            ("Barcelona", "Madrid"),
            ("Madrid", "Bordeaux"),
            ("Bordeaux", "Paris"),
            ("Paris", "London"),
            ("London", "Amsterdam"),
            ("London", "Dublin"),
            ("Dublin", "Glasgow"),
            ("Glasgow", "Amsterdam")
        ]

        for src, dst in links:
            self.addLink(switches[src], switches[dst])  # Link between switches


topos = {'mytopo': (lambda: MyTopo())}

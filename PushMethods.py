class Order:
    def __init__(self, order_id, customer_name, order_date, total_amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.order_date = order_date
        self.total_amount = total_amount  

    def calculate_tax(self, tax_rate):
        return self.total_amount * tax_rate

    def display_order(self):
        print(f"ID: {self.order_id} | Nama: {self.customer_name} | Tanggal: {self.order_date} | Total: Rp{self.total_amount:,}")

class OrderProcessor:
    def __init__(self):
        self.orders = [] 

    def add_order(self, order):
        self.orders.append(order)

    def calculate_total_revenue(self):
        total = 0
        for order in self.orders:
            total += order.total_amount
        return total

    def calculate_total_tax(self, tax_rate):
        total_pajak = 0
        for order in self.orders:
            total_pajak += order.calculate_tax(tax_rate)
        return total_pajak
    

processor = OrderProcessor()

order1 = Order("ORD001", "Budi", "2026-02-23", 500000)
order2 = Order("ORD002", "Andi", "2026-04-13", 300000)
order3 = Order("ORD003", "Kevin", "2026-01-09", 275000)
order4 = Order("ORD004", "Jane", "2026-05-02", 450000)

order1.display_order()
order2.display_order()
order3.display_order()
order4.display_order()
print("-" * 50)

processor.add_order(order1)
processor.add_order(order2)
processor.add_order(order3)
processor.add_order(order4)

tarif_pajak = 0.1
total_pendapatan = processor.calculate_total_revenue()
total_pajak = processor.calculate_total_tax(tarif_pajak)

print(f"Total Pendapatan : Rp{total_pendapatan:,}")
print(f"Total Pajak Terkumpul   : Rp{total_pajak:,}")
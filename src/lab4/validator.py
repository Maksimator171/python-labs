import re
import typing as tp

PHONE_PATTERN = re.compile(r"^\+\d-\d{3}-\d{3}-\d{2}-\d{2}$")
RUSSIA_NAMES = {"Россия", "Российская Федерация"}
PRIORITY_ORDER = {"MAX": 0, "MIDDLE": 1, "LOW": 2}
ERROR_ADDRESS = "1"
ERROR_PHONE = "2"
NO_DATA = "no data"

def read_orders(path: str) -> tp.List[tp.List[str]]:
    orders = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            orders.append(line.split(";"))
    return orders

def is_valid_phone(phone: str) -> bool:
    return bool(PHONE_PATTERN.match(phone.strip()))

def is_valid_address(address: str) -> bool:
    if not address.strip():
        return False
    return len(address.split(". ")) >= 4

def get_country(address: str) -> str:
    return address.split(". ")[0].strip()

def address_without_country(address: str) -> str:
    return address.split(". ", 1)[1].strip()

def format_products(products: str) -> str:
    counts = {}
    order = []
    for item in products.split(","):
        name = item.strip()
        if name not in counts:
            counts[name] = 0
            order.append(name)
        counts[name] += 1
    result = []
    for name in order:
        if counts[name] > 1:
            result.append(f"{name} x{counts[name]}")
        else:
            result.append(name)
    return ", ".join(result)

def validate_orders(
    orders: tp.List[tp.List[str]],
) -> tp.Tuple[tp.List[tp.List[str]], tp.List[str]]:
    valid_orders = []
    non_valid_lines = []
    for order in orders:
        number, _, _, address, phone, _ = order
        has_error = False
        if not is_valid_phone(phone):
            value = phone.strip() if phone.strip() else NO_DATA
            non_valid_lines.append(f"{number};{ERROR_PHONE};{value}")
            has_error = True
        if not is_valid_address(address):
            value = address.strip() if address.strip() else NO_DATA
            non_valid_lines.append(f"{number};{ERROR_ADDRESS};{value}")
            has_error = True
        if not has_error:
            valid_orders.append(order)
    return valid_orders, non_valid_lines

def sort_orders(orders: tp.List[tp.List[str]]) -> tp.List[tp.List[str]]:
    def key(order: tp.List[str]) -> tp.Tuple[int, str, int]:
        country = get_country(order[3])
        is_not_russia = 0 if country in RUSSIA_NAMES else 1
        priority_rank = PRIORITY_ORDER.get(order[5].strip(), len(PRIORITY_ORDER))
        return (is_not_russia, country, priority_rank)
    return sorted(orders, key=key)

def format_order(order: tp.List[str]) -> str:
    number, products, fio, address, phone, priority = order
    return ";".join([
        number,
        format_products(products),
        fio,
        address_without_country(address),
        phone,
        priority,
    ])

def write_lines(path: str, lines: tp.List[str]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

def main(
    source: str = "orders.txt",
    valid_path: str = "order_country.txt",
    non_valid_path: str = "non_valid_orders.txt",
) -> None:
    orders = read_orders(source)
    valid_orders, non_valid_lines = validate_orders(orders)
    sorted_orders = sort_orders(valid_orders)
    write_lines(non_valid_path, non_valid_lines)
    write_lines(valid_path, [format_order(order) for order in sorted_orders])

if __name__ == "__main__":
    main()
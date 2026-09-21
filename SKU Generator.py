def create_order():
    items = {
        "Americano": Element("americano"),
        "Spanish Latte": Element("spanish"),
        "Cold Brew Malt": Element("coldbrew"),
        "Affogato": Element("affogato"),
        "Caramel Macchiato": Element("caramel")
    }

    selected = []
    total = 0

    for name, el in items.items():
        if el.element.checked:
            price = int(el.element.value)
            selected.append(f"{name} — ₱{price}")
            total += price

    if selected:
        order_summary = "You ordered:\n" + "\n".join(selected) + f"\n\nTotal: ₱{total}"
    else:
        order_summary = "No items selected."

    Element("summary").write(order_summary)
    </py-script>
</body>
</html>

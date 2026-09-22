def create_order():
    order = Element("order").value.strip()
    if order:
        Element("order-summary").write(f"Order placed: {order}")
    else:
        Element("order-summary").write("Please enter your order.")
    </py-script>
</body>
</html>

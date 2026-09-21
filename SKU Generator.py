def generate_sku():
    category = Element("category").value.strip().upper()[:3]
    product = Element("product").value.strip().upper().replace(" ", "")[:5]
    quantity = Element("quantity").value.strip()

    if category and product and quantity:
        sku = f"{category}-{product}-{quantity}"
        Element("output").write(f"Generated SKU: {sku}")
    else:
        Element("output").write("Please fill in all fields.")
    </py-script>
</body>
</html>

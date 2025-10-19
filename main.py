from js import document, window, console

def calculate_total(evt=None):
    try:
        checkboxes = document.querySelectorAll("input[name='item']:checked")
        total = 0.0
        items = []

        for cb in checkboxes:
            name = cb.getAttribute("data-name")
            price = float(cb.value)
            total += price
            items.append(f"{name} – ₱{price:.2f}")

        name = document.getElementById("custName").value.strip()
        address = document.getElementById("address").value.strip()
        contact = document.getElementById("contact").value.strip()
        summary_text = document.getElementById("orderSummaryText")

        if not name or not address or not contact or not items:
            summary_text.innerHTML = "⚠️ Please complete all customer details and select at least one item."
            return

        order_summary = (
            f"<strong>Order for:</strong> {name}<br>"
            f"<strong>Address:</strong> {address}<br>"
            f"<strong>Contact:</strong> {contact}<br><br>"
            f"<strong>Items Ordered:</strong><br>"
            f"{'<br>'.join(items)}<br><br>"
            f"<strong>Total:</strong> ₱{total:.2f}"
        )

        summary_text.innerHTML = order_summary

        # Add a brief highlight effect
        summary_box = document.getElementById("summaryBox")
        summary_box.style.boxShadow = "0 8px 20px rgba(0,0,0,0.18)"
        window.setTimeout(lambda: setattr(summary_box.style, "boxShadow", "0 4px 12px rgba(0,0,0,0.12)"), 800)
        summary_box.scrollIntoView({"behavior": "smooth", "block": "center"})

    except Exception as e:
        console.error("calculate_total error:", str(e))
        try:
            document.getElementById("orderSummaryText").innerHTML = "An error occurred. Open console for details."
        except:
            pass


window.calculate_total = calculate_total


def bind_button(evt=None):
    try:
        btn = document.getElementById("createOrder")
        if btn:
            try:
                btn.removeEventListener("click", calculate_total)
            except:
                pass
            btn.addEventListener("click", calculate_total)
            console.log("✅ Create Order button connected to Python.")
    except Exception as e:
        console.error("bind_button error:", str(e))


try:
    if document.readyState in ("complete", "interactive"):
        bind_button()
    else:
        document.addEventListener("DOMContentLoaded", bind_button)
except Exception as e:
    console.error("setup binding failed:", str(e))

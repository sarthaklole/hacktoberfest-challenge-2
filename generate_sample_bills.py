import os
from PIL import Image, ImageDraw, ImageFont

output_dir = r"d:\hacktoberfest\sample_receipts"
os.makedirs(output_dir, exist_ok=True)

bills = [
    {
        "filename": "bill01_stationery.jpg",
        "vendor": "SAI STATIONERY & PRINTING",
        "date": "14-Sep-2026",
        "total": "INR 973.50",
        "items": [
            "A4 Copier Paper 2x: 640.00",
            "Lever Arch Files 4x: 220.00",
            "Gel Pens Box 1x: 113.50"
        ]
    },
    {
        "filename": "bill02_restaurant.jpg",
        "vendor": "HOTEL RAJDHANI DINING",
        "date": "15-Sep-2026",
        "total": "INR 1,113.00",
        "items": [
            "Executive Thali 3x: 840.00",
            "Butter Roti 4x: 100.00",
            "Water & Taxes: 173.00"
        ]
    },
    {
        "filename": "bill03_medical.jpg",
        "vendor": "KOLHAPUR MEDICAL STORE",
        "date": "02-Oct-2026",
        "total": "INR 249.76",
        "items": [
            "Antiseptic Liquid: 85.00",
            "Paracetamol Strip: 34.76",
            "Bandage Pack: 130.00"
        ]
    },
    {
        "filename": "bill04_hardware.jpg",
        "vendor": "SHREE DATTA HARDWARE",
        "date": "21-Aug-2026",
        "total": "INR 2,183.00",
        "items": [
            "Surge Extension 2x: 950.00",
            "Network Crimper Tool: 850.00",
            "Wall Anchors & Screws: 383.00"
        ]
    },
    {
        "filename": "bill06_bus_ticket.jpg",
        "vendor": "MSRTC BUS PASSENGER TICKET",
        "date": "28-Sep-2026",
        "total": "INR 245.00",
        "items": [
            "Kolhapur -> Pune (Swargate)",
            "Seat 14B Semi-Luxury AC",
            "Fare: 245.00"
        ]
    },
    {
        "filename": "bill07_chai_messy_photo.jpg",
        "vendor": "CHAI POINT EXPRESS",
        "date": "10-Oct-2026",
        "total": "INR 141.75",
        "items": [
            "Ginger Chai Flask: 95.00",
            "Cashew Cookies: 40.00",
            "GST: 6.75"
        ]
    }
]

for b in bills:
    img = Image.new('RGB', (450, 600), color=(248, 250, 252))
    draw = ImageDraw.Draw(img)
    
    # Outer border & header
    draw.rectangle([(15, 15), (435, 585)], outline=(203, 213, 225), width=2)
    draw.rectangle([(15, 15), (435, 90)], fill=(30, 41, 59))
    
    # Text
    draw.text((30, 32), b["vendor"], fill=(241, 245, 249))
    draw.text((30, 60), f"DATE: {b['date']} | TAX INVOICE", fill=(148, 163, 184))
    
    y = 120
    draw.text((30, y), "ITEMIZED DELIVERABLES:", fill=(71, 85, 105))
    y += 30
    for item in b["items"]:
        draw.text((35, y), f"• {item}", fill=(15, 23, 42))
        y += 35
    
    # Total Box
    draw.line([(30, y + 20), (420, y + 20)], fill=(203, 213, 225), width=2)
    draw.rectangle([(30, y + 40), (420, y + 110)], fill=(241, 245, 249), outline=(16, 185, 129), width=2)
    draw.text((45, y + 55), "TOTAL AMOUNT PAID", fill=(100, 116, 139))
    draw.text((45, y + 75), b["total"], fill=(16, 185, 129))
    
    # Footer
    draw.text((45, 545), "PrivaLedger Verified • Air-Gapped Local Receipt", fill=(148, 163, 184))

    out_path = os.path.join(output_dir, b["filename"])
    img.save(out_path, "JPEG", quality=92)
    print(f"Generated: {out_path}")

# Now generate a sample PDF: bill05_broadband_invoice.pdf
pdf_path = os.path.join(output_dir, "bill05_broadband_invoice.pdf")
pdf_img = Image.new('RGB', (595, 842), color=(255, 255, 255))
pdf_draw = ImageDraw.Draw(pdf_img)
pdf_draw.rectangle([(20, 20), (575, 822)], outline=(200, 200, 200), width=1)
pdf_draw.rectangle([(20, 20), (575, 110)], fill=(225, 29, 72)) # Airtel Red
pdf_draw.text((40, 45), "AIRTEL BROADBAND TAX INVOICE", fill=(255, 255, 255))
pdf_draw.text((40, 75), "Bharti Airtel Ltd | GSTIN: 27AAACB2894G1ZN | Date: 05-Oct-2026", fill=(255, 228, 230))

pdf_draw.text((40, 150), "Account No: 0231-9944-1288  |  Invoice: AT-WIFI-2026-10-05", fill=(50, 50, 50))
pdf_draw.text((40, 190), "Plan: Airtel Xstream Fiber Ultra 200 Mbps Unlimited: Rs 999.00", fill=(20, 20, 20))
pdf_draw.text((40, 220), "Static IP Add-on: Rs 0.00", fill=(20, 20, 20))
pdf_draw.text((40, 250), "CGST (9%): Rs 89.91", fill=(80, 80, 80))
pdf_draw.text((40, 280), "SGST (9%): Rs 89.91", fill=(80, 80, 80))
pdf_draw.line([(40, 320), (550, 320)], fill=(150, 150, 150), width=2)
pdf_draw.text((40, 340), "TOTAL INVOICE AMOUNT: INR 1,178.82", fill=(225, 29, 72))
pdf_draw.text((40, 370), "Status: Auto-Debited from Credit Card ending in *4910", fill=(16, 185, 129))

pdf_img.save(pdf_path, "PDF", resolution=100.0)
print(f"Generated: {pdf_path}")

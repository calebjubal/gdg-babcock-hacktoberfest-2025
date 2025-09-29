from reportlab.pdfgen import canvas

def generate_certificate(name: str, track: str) -> str:
    file_path = f"certificates/{name}_certificate.pdf"
    c = canvas.Canvas(file_path)
    c.setFont("Helvetica-Bold", 24)
    c.drawString(100, 500, "Hacktoberfest 2025 Certificate")
    c.setFont("Helvetica", 18)
    c.drawString(100, 450, f"Presented to {name}")
    c.drawString(100, 420, f"For contributions in {track}")
    c.save()
    return file_path

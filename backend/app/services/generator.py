from PIL import Image, ImageDraw, ImageFont
import os
from ..models.certificates import CertificateBase

def generate_certificate_from_model(cert_data: CertificateBase, output_path="certificate.png"):
    # Now you can access cert_data.name, cert_data.event, cert_data.date
    return generate_certificate(cert_data.participant_name, cert_data.event_name, cert_data.date_issued, cert_data.certificate_type, output_path)

def generate_certificate(name, event, date, type, output_path="certificate.png"):
    # Debug: show where it will save
    print("Saving certificate at:", os.path.abspath(output_path))
    
    # Load the certificate template PNG
    if type == "completion":
        template_path = os.path.join(os.path.dirname(__file__), "..", "..", "templates", "certificate_template_completion.png")
    else:
        template_path = os.path.join(os.path.dirname(__file__), "..", "..", "templates", "certificate_template_participation.png")

    try:
        certificate = Image.open(template_path)
        print(f"✅ Loaded template from: {template_path}")
    except FileNotFoundError:
        print(f"⚠️ Template not found at {template_path}. Creating blank certificate.")
        # Fallback to blank certificate if template not found
        certificate = Image.new("RGB", (1200, 850), color="#f8f9fa")
    
    width, height = certificate.size
    draw = ImageDraw.Draw(certificate)
    width, height = certificate.size
    draw = ImageDraw.Draw(certificate)
    
    # Load Google Sans fonts with fallback
    font_dir = os.path.join(os.path.dirname(__file__), "..", "..", "templates")
    try:
        # Google Sans Bold for name (29.07px ≈ 29pt)
        font_name = ImageFont.truetype(os.path.join(font_dir, "GoogleSans-Bold.ttf"), 29)
        # Google Sans Bold for event and date (16.15px ≈ 16pt)
        font_event_date = ImageFont.truetype(os.path.join(font_dir, "GoogleSans-Bold.ttf"), 16)
        print("✅ Google Sans fonts loaded successfully")
    except IOError:
        print("⚠️ Google Sans fonts not found. Using fallback fonts.")
        try:
            # Fallback to Arial Bold
            font_name = ImageFont.truetype("arialbd.ttf", 29)
            font_event_date = ImageFont.truetype("arialbd.ttf", 16)
        except IOError:
            print("⚠️ Arial fonts not found. Using default font.")
            font_name = ImageFont.load_default()
            font_event_date = ImageFont.load_default()
    
    # Helper function to left-align text with letter spacing at a fixed margin
    def left_align_text(text, y, font, color="black", letter_spacing=-0.04, margin=45):
        x = margin
        if letter_spacing != 0:
            for char in text:
                draw.text((x, y), char, font=font, fill=color)
                bbox = draw.textbbox((0, 0), char, font=font)
                char_width = bbox[2] - bbox[0]
                # Negative letter spacing shrinks the space between characters
                x += char_width + (char_width * letter_spacing / len(text))
        else:
            draw.text((x, y), text, font=font, fill=color)

    # Overlay text on the template, left-aligned at 45px margin
    if type == "completion":
        left_align_text(name, height // 2 - 15, font_name, "#000000")
        left_align_text(event, height // 2 + 57, font_event_date, "#000000")
        left_align_text(date, height // 2 + 78, font_event_date, "#000000", margin=120)
    else:
        left_align_text(name, height // 2 - 15, font_name, "#000000")
        left_align_text(event, height // 2 + 57, font_event_date, "#000000")
        left_align_text(date, height // 2 + 78, font_event_date, "#000000", margin=160)

    # Save file
    certificate.save(output_path)
    return output_path

if __name__ == "__main__":
    data = CertificateBase(
        participant_name="Jane Doe",
        event_name="Hacktoberfest 2025",
        date_issued="2025-10-03",
        certificate_type="completion"
    )

    file_path = generate_certificate_from_model(data)
    print("✅ Certificate generated at:", file_path)
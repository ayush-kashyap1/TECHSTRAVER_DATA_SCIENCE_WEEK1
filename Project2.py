import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
from PIL import Image, ImageTk
import io

# Function to generate the QR code
def generate_qr():
    text = input_entry.get()
    if not text:
        result_label.config(text="Please enter text or URL.")
        return

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    # Create an in-memory image
    img = qr.make_image(fill='black', back_color='white')
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)

    # Display the QR code in the GUI
    qr_image = Image.open(buffer)
    qr_photo = ImageTk.PhotoImage(qr_image)
    qr_label.config(image=qr_photo)
    qr_label.image = qr_photo

    # Enable the save button
    save_button.config(state=tk.NORMAL)

    result_label.config(text="QR Code Generated. You can now save it.")

# Function to save the QR code as a PNG file
def save_qr():
    text = input_entry.get()
    if not text:
        result_label.config(text="Please generate the QR code first.")
        return

    # Ask the user where to save the file
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png")],
                                             title="Save QR Code")
    if file_path:
        # Generate and save the QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img.save(file_path)
        result_label.config(text=f"QR Code saved at: {file_path}")
    else:
        result_label.config(text="Save operation canceled.")

# Create the main window
window = tk.Tk()
window.title("QR Code Generator")
window.geometry("1920x1080")  # Set window size to 1920x1080

# Load and set background image
bg_image = Image.open("Image.jpg")
bg_image = bg_image.resize((1920, 1080), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

background_label = tk.Label(window, image=bg_photo)
background_label.place(relwidth=1, relheight=1)

# Create and configure widgets
input_frame = tk.Frame(window, bg="#FFFFFF", bd=10)
input_frame.place(relx=0.5, rely=0.1, anchor="center")

input_label = tk.Label(input_frame, text="Enter URL or Text:", font=("Arial", 16), bg="#FFFFFF")
input_entry = tk.Entry(input_frame, font=("Arial", 14), width=80)
generate_button = tk.Button(input_frame, text="Generate QR Code", command=generate_qr, font=("Arial", 14), bg="#4CAF50", fg="white")
save_button = tk.Button(input_frame, text="Save QR Code", command=save_qr, state=tk.DISABLED, font=("Arial", 14), bg="#4CAF50", fg="white")

# Place widgets in the frame
input_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
input_entry.grid(row=1, column=0, padx=10, pady=10, columnspan=2)
generate_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
save_button.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

qr_label = tk.Label(window, bg="#FFFFFF")
qr_label.place(relx=0.5, rely=0.5, anchor="center")

result_label = tk.Label(window, text="", font=("Arial", 14), bg="#FFFFFF", wraplength=500)
result_label.place(relx=0.5, rely=0.9, anchor="center")

# Start the Tkinter main loop
window.mainloop()

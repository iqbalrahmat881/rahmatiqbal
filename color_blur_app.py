import tkinter as tk
from tkinter import filedialog, Label, Button
from PIL import Image, ImageTk, ImageFilter

class ColorBlurApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Pengeblur Warna")

        # Tombol untuk memilih gambar
        self.select_button = Button(root, text="Pilih Gambar", command=self.load_image)
        self.select_button.pack()

        # Label untuk menampilkan gambar
        self.image_label = Label(root)
        self.image_label.pack()

        # Tombol untuk menerapkan efek blur
        self.blur_button = Button(root, text="Terapkan Blur", command=self.apply_blur, state=tk.DISABLED)
        self.blur_button.pack()

        # Penyimpanan untuk gambar asli dan gambar yang sudah di-blur
        self.original_image = None
        self.blurred_image = None

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.original_image = Image.open(file_path)
            self.display_image(self.original_image)
            self.blur_button.config(state=tk.NORMAL)

    def display_image(self, image):
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo

    def apply_blur(self):
        if self.original_image:
            self.blurred_image = self.original_image.filter(ImageFilter.GaussianBlur(5))
            self.display_image(self.blurred_image)

# Inisialisasi aplikasi
if __name__ == "__main__":
    root = tk.Tk()
    app = ColorBlurApp(root)
    root.mainloop()

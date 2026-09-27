import os
import uuid
import webbrowser
import threading
import time
import ctypes
import winsound
import wave
import customtkinter as ctk

from tkinter import messagebox
from PIL import Image

from coffee_data import coffees
from database import create_database, save_order
from payment import calculate_total, check_payment
from bill import generate_bill


# ==========================================================
# PATHS
# ==========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(BASE_DIR, "images")
SOUNDS_DIR = os.path.join(BASE_DIR, "sounds")

# Always run relative-file operations from the project folder.
os.chdir(BASE_DIR)


# ==========================================================
# APP SETTINGS
# ==========================================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

BG_COLOR = "#120C09"
CARD_COLOR = "#211612"
CARD_HOVER = "#302019"
COFFEE_BROWN = "#8B5E3C"
LIGHT_BROWN = "#B9825B"
CREAM = "#F5E6D3"
WHITE = "#FFFFFF"
GRAY = "#A99A90"
GREEN = "#35B56A"
RED = "#D9534F"
GOLD = "#D9A441"


# ==========================================================
# FILE FINDERS
# ==========================================================

def normalize_name(value):
    """Make filenames easy to compare."""
    return "".join(ch.lower() for ch in value if ch.isalnum())


def find_image_file(image_name, coffee_name=None):
    """Find an image even if its filename has small differences.

    Example: espresso.png in coffee_data.py can still find
    the actual file espresso..png from the user's folder.
    """
    if not os.path.isdir(IMAGES_DIR):
        return None

    requested = normalize_name(os.path.splitext(image_name)[0])
    coffee_key = normalize_name(coffee_name or "")

    # 1. Exact path first.
    exact = os.path.join(IMAGES_DIR, image_name)
    if os.path.isfile(exact):
        return exact

    # 2. Search recursively and compare normalized names.
    supported = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".gif", ".jfif"}
    files = []

    for root, _, names in os.walk(IMAGES_DIR):
        for name in names:
            if os.path.splitext(name)[1].lower() in supported:
                files.append(os.path.join(root, name))

    # Exact normalized match. This catches espresso..png.
    for path in files:
        stem = normalize_name(os.path.splitext(os.path.basename(path))[0])
        if stem == requested:
            return path

    # Coffee-name match.
    if coffee_key:
        for path in files:
            stem = normalize_name(os.path.splitext(os.path.basename(path))[0])
            if stem == coffee_key:
                return path

    # Contains match. Useful for names such as espresso_1.png.
    for path in files:
        stem = normalize_name(os.path.splitext(os.path.basename(path))[0])
        if requested and (requested in stem or stem in requested):
            return path

    if coffee_key:
        for path in files:
            stem = normalize_name(os.path.splitext(os.path.basename(path))[0])
            if coffee_key in stem or stem in coffee_key:
                return path

    return None


def find_sound_file(kind):
    """Find the real sound file in the sounds folder.

    The user's actual files are:
      coffee_making_sound.wav
      payment_done_sound.wav
    """
    if not os.path.isdir(SOUNDS_DIR):
        return None

    aliases = {
        "payment": [
            "payment_done_sound",
            "payment_done",
            "payment",
            "success",
        ],
        "making": [
            "coffee_making_sound",
            "coffee_making",
            "making",
            "brew",
        ],
        "click": [
            "click",
            "button_click",
        ],
        "error": [
            "error",
        ],
        "ready": [
            "ready",
            "coffee_ready",
        ],
    }

    wanted = [normalize_name(x) for x in aliases.get(kind, [kind])]
    supported = {".wav", ".mp3", ".m4a", ".aac", ".wma"}

    files = []
    for root, _, names in os.walk(SOUNDS_DIR):
        for name in names:
            if os.path.splitext(name)[1].lower() in supported:
                files.append(os.path.join(root, name))

    # Exact normalized stem first.
    for path in files:
        stem = normalize_name(os.path.splitext(os.path.basename(path))[0])
        if stem in wanted:
            return path

    # Fuzzy match.
    for wanted_name in wanted:
        for path in files:
            stem = normalize_name(os.path.splitext(os.path.basename(path))[0])
            if wanted_name in stem or stem in wanted_name:
                return path

    return None


# ==========================================================
# SOUND PLAYER
# ==========================================================

def _play_with_mci(file_path):
    """Windows built-in fallback for non-WAV audio."""
    try:
        winmm = ctypes.WinDLL("winmm")
        alias = "coffee_" + uuid.uuid4().hex
        ext = os.path.splitext(file_path)[1].lower()

        if ext == ".wav":
            media_type = "waveaudio"
        else:
            media_type = "mpegvideo"

        result = winmm.mciSendStringW(
            f'open "{file_path}" type {media_type} alias {alias}',
            None,
            0,
            None,
        )

        if result == 0:
            winmm.mciSendStringW(f"play {alias}", None, 0, None)

            def close_later():
                time.sleep(12)
                try:
                    winmm.mciSendStringW(f"close {alias}", None, 0, None)
                except Exception:
                    pass

            threading.Thread(target=close_later, daemon=True).start()
            return True
    except Exception:
        pass

    return False


def play_project_sound(kind):
    """Play a project sound using the actual filenames in /sounds."""
    path = find_sound_file(kind)

    if not path:
        return False

    try:
        # winsound is perfect for WAV files.
        if path.lower().endswith(".wav"):
            winsound.PlaySound(
                path,
                winsound.SND_FILENAME | winsound.SND_ASYNC
            )
            return True
    except Exception:
        pass

    return _play_with_mci(path)


# ==========================================================
# MAIN APPLICATION
# ==========================================================

class CoffeeVendingMachine(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("☕ Coffee Vending Machine")
        self.geometry("1200x780")
        self.resizable(False, False)
        self.configure(fg_color=BG_COLOR)

        self.cart = {}
        self.image_cache = {}
        self.current_total = 0
        self.last_bill_path = None

        create_database()
        self.show_welcome_page()

    # ======================================================
    # COMMON
    # ======================================================

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

    # ======================================================
    # WELCOME PAGE
    # ======================================================

    def show_welcome_page(self):
        self.clear_screen()

        main_frame = ctk.CTkFrame(
            self,
            fg_color=BG_COLOR,
            corner_radius=0
        )
        main_frame.pack(fill="both", expand=True)

        ctk.CTkFrame(
            main_frame,
            height=6,
            fg_color=COFFEE_BROWN,
            corner_radius=0
        ).pack(fill="x")

        ctk.CTkLabel(
            main_frame,
            text="☕",
            font=("Segoe UI Emoji", 100),
            text_color=CREAM
        ).pack(pady=(55, 0))

        ctk.CTkLabel(
            main_frame,
            text="COFFEE",
            font=("Arial", 48, "bold"),
            text_color=CREAM
        ).pack()

        ctk.CTkLabel(
            main_frame,
            text="VENDING MACHINE",
            font=("Arial", 30, "bold"),
            text_color=LIGHT_BROWN
        ).pack(pady=(0, 8))

        ctk.CTkLabel(
            main_frame,
            text="Fresh Coffee  •  Fast Service  •  Perfect Taste",
            font=("Arial", 16),
            text_color=GRAY
        ).pack(pady=5)

        info_card = ctk.CTkFrame(
            main_frame,
            width=650,
            height=100,
            corner_radius=20,
            fg_color=CARD_COLOR
        )
        info_card.pack(pady=25)
        info_card.pack_propagate(False)

        ctk.CTkLabel(
            info_card,
            text=(
                "Choose your favorite coffee ☕\n"
                "Make your payment and enjoy your drink!"
            ),
            font=("Arial", 16),
            text_color=CREAM,
            justify="center"
        ).pack(expand=True)

        ctk.CTkButton(
            main_frame,
            text="☕  START ORDER",
            width=300,
            height=58,
            corner_radius=18,
            fg_color=COFFEE_BROWN,
            hover_color=LIGHT_BROWN,
            text_color=WHITE,
            font=("Arial", 19, "bold"),
            command=self.start_order
        ).pack(pady=10)

        ctk.CTkLabel(
            main_frame,
            text="Your coffee, your choice ❤️",
            font=("Arial", 13),
            text_color=GRAY
        ).pack(side="bottom", pady=20)

    def start_order(self):
        play_project_sound("click")
        self.show_menu_page()

    # ======================================================
    # MENU PAGE
    # ======================================================

    def show_menu_page(self):
        self.clear_screen()

        header = ctk.CTkFrame(
            self,
            height=70,
            corner_radius=18,
            fg_color=CARD_COLOR
        )
        header.pack(fill="x", padx=15, pady=(15, 8))
        header.pack_propagate(False)

        ctk.CTkLabel(
            header,
            text="☕  CHOOSE YOUR COFFEE",
            font=("Arial", 27, "bold"),
            text_color=CREAM
        ).pack(side="left", padx=25)

        ctk.CTkButton(
            header,
            text="← Back",
            width=90,
            height=35,
            corner_radius=12,
            fg_color="#4A3328",
            hover_color=COFFEE_BROWN,
            command=self.show_welcome_page
        ).pack(side="right", padx=20)

        menu_frame = ctk.CTkFrame(self, fg_color="transparent")
        menu_frame.pack(fill="both", expand=True, padx=15, pady=5)

        # LEFT: scrollable coffee menu
        left_frame = ctk.CTkFrame(
            menu_frame,
            corner_radius=18,
            fg_color="#18100D"
        )
        left_frame.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 8)
        )

        ctk.CTkLabel(
            left_frame,
            text="☕  SELECT YOUR FAVORITE",
            font=("Arial", 19, "bold"),
            text_color=CREAM
        ).pack(pady=(10, 4))

        cards_frame = ctk.CTkScrollableFrame(
            left_frame,
            fg_color="transparent",
            scrollbar_button_color="#5A3A2A",
            scrollbar_button_hover_color=COFFEE_BROWN
        )
        cards_frame.pack(fill="both", expand=True, padx=8, pady=(2, 8))

        for column in range(3):
            cards_frame.grid_columnconfigure(column, weight=1)

        row = 0
        column = 0

        for coffee_name, data in coffees.items():
            self.create_coffee_card(
                cards_frame,
                coffee_name,
                data,
                row,
                column
            )

            column += 1
            if column == 3:
                column = 0
                row += 1

        # RIGHT: fixed full-height cart
        self.create_cart_section(menu_frame)
        self.update_cart()

    # ======================================================
    # COFFEE CARD
    # ======================================================

    def create_coffee_card(self, parent, coffee_name, data, row, column):
        card = ctk.CTkFrame(
            parent,
            width=205,
            height=275,
            corner_radius=18,
            fg_color=CARD_COLOR
        )
        card.grid(
            row=row,
            column=column,
            padx=7,
            pady=7,
            sticky="nsew"
        )
        card.grid_propagate(False)

        # Fixed grid keeps the ADD TO CART button inside the card.
        card.grid_columnconfigure(0, weight=1)

        image_label = self.create_image_label(
            card,
            data.get("image", ""),
            coffee_name
        )
        image_label.grid(row=0, column=0, pady=(8, 2))

        ctk.CTkLabel(
            card,
            text=coffee_name,
            font=("Arial", 15, "bold"),
            text_color=CREAM
        ).grid(row=1, column=0, pady=(0, 1))

        ctk.CTkLabel(
            card,
            text=data.get("description", ""),
            font=("Arial", 10),
            text_color=GRAY,
            wraplength=180,
            height=24
        ).grid(row=2, column=0, pady=(0, 1))

        ctk.CTkLabel(
            card,
            text=f"₹ {data['price']}",
            font=("Arial", 14, "bold"),
            text_color=GOLD
        ).grid(row=3, column=0, pady=(0, 3))

        # ADD TO CART is now always visible and stays inside the card.
        ctk.CTkButton(
            card,
            text="+  ADD TO CART",
            width=150,
            height=36,
            corner_radius=11,
            fg_color=COFFEE_BROWN,
            hover_color=LIGHT_BROWN,
            font=("Arial", 12, "bold"),
            command=lambda name=coffee_name: self.add_to_cart(name)
        ).grid(row=4, column=0, pady=(1, 8))

    # ======================================================
    # IMAGE LOADER
    # ======================================================

    def create_image_label(self, parent, image_name, coffee_name):
        cache_key = f"{coffee_name}:{image_name}"

        if cache_key in self.image_cache:
            photo = self.image_cache[cache_key]
            return ctk.CTkLabel(parent, text="", image=photo)

        image_path = find_image_file(image_name, coffee_name)

        if image_path:
            try:
                image = Image.open(image_path)
                image.load()

                # Copy image so the file handle is not needed afterwards.
                image = image.convert("RGBA")

                photo = ctk.CTkImage(
                    light_image=image,
                    dark_image=image,
                    size=(125, 90)
                )

                self.image_cache[cache_key] = photo

                return ctk.CTkLabel(
                    parent,
                    text="",
                    image=photo
                )
            except Exception:
                pass

        # Fallback only if an image really cannot be opened.
        return ctk.CTkLabel(
            parent,
            text="☕",
            font=("Segoe UI Emoji", 50),
            text_color=LIGHT_BROWN,
            width=125,
            height=90
        )

    # ======================================================
    # CART SECTION
    # ======================================================

    def create_cart_section(self, parent):
        self.cart_frame = ctk.CTkFrame(
            parent,
            width=335,
            corner_radius=18,
            fg_color=CARD_COLOR
        )
        self.cart_frame.pack(
            side="right",
            fill="y",
            padx=(8, 0),
            pady=0
        )
        self.cart_frame.pack_propagate(False)

        ctk.CTkLabel(
            self.cart_frame,
            text="🛒  YOUR CART",
            font=("Arial", 21, "bold"),
            text_color=CREAM
        ).pack(pady=(14, 7))

        ctk.CTkFrame(
            self.cart_frame,
            height=2,
            fg_color="#4A3328"
        ).pack(fill="x", padx=20)

        self.cart_items_frame = ctk.CTkScrollableFrame(
            self.cart_frame,
            fg_color="transparent",
            scrollbar_button_color="#5A3A2A",
            scrollbar_button_hover_color=COFFEE_BROWN
        )
        self.cart_items_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=5
        )

        self.total_label = ctk.CTkLabel(
            self.cart_frame,
            text="TOTAL: ₹ 0",
            font=("Arial", 21, "bold"),
            text_color=GOLD
        )
        self.total_label.pack(pady=(6, 7))

        self.pay_button = ctk.CTkButton(
            self.cart_frame,
            text="💳  PROCEED TO PAYMENT",
            width=285,
            height=46,
            corner_radius=13,
            fg_color=GREEN,
            hover_color="#279653",
            text_color=WHITE,
            font=("Arial", 14, "bold"),
            command=self.open_payment
        )
        self.pay_button.pack(padx=20, pady=4)

        ctk.CTkButton(
            self.cart_frame,
            text="🗑  CLEAR CART",
            width=285,
            height=35,
            corner_radius=12,
            fg_color="#49332A",
            hover_color=RED,
            font=("Arial", 12, "bold"),
            command=self.new_order
        ).pack(padx=20, pady=(4, 12))

    # ======================================================
    # CART OPERATIONS
    # ======================================================

    def add_to_cart(self, coffee_name):
        play_project_sound("click")

        self.cart[coffee_name] = self.cart.get(coffee_name, 0) + 1
        self.update_cart()

    def remove_from_cart(self, coffee_name):
        play_project_sound("click")

        if coffee_name in self.cart:
            self.cart[coffee_name] -= 1
            if self.cart[coffee_name] <= 0:
                del self.cart[coffee_name]

        self.update_cart()

    def update_cart(self):
        if not hasattr(self, "cart_items_frame"):
            return

        for widget in self.cart_items_frame.winfo_children():
            widget.destroy()

        total = 0

        if not self.cart:
            ctk.CTkLabel(
                self.cart_items_frame,
                text="☕\n\nYour cart is empty\nAdd your favorite coffee!",
                font=("Arial", 14),
                text_color=GRAY,
                justify="center"
            ).pack(pady=55)
        else:
            for coffee_name, quantity in self.cart.items():
                price = coffees[coffee_name]["price"]
                item_total = price * quantity
                total += item_total

                item_frame = ctk.CTkFrame(
                    self.cart_items_frame,
                    height=62,
                    corner_radius=12,
                    fg_color="#2A1B15"
                )
                item_frame.pack(fill="x", padx=3, pady=5)
                item_frame.pack_propagate(False)

                # Minus button first on the right.
                ctk.CTkButton(
                    item_frame,
                    text="−",
                    width=30,
                    height=30,
                    corner_radius=8,
                    fg_color="#49332A",
                    hover_color=RED,
                    font=("Arial", 16, "bold"),
                    command=lambda name=coffee_name: self.remove_from_cart(name)
                ).pack(side="right", padx=(2, 7))

                ctk.CTkLabel(
                    item_frame,
                    text=f"₹{item_total}",
                    font=("Arial", 12, "bold"),
                    text_color=GOLD
                ).pack(side="right", padx=5)

                ctk.CTkLabel(
                    item_frame,
                    text=f"{coffee_name}\n₹{price} × {quantity}",
                    font=("Arial", 12, "bold"),
                    text_color=CREAM,
                    anchor="w",
                    justify="left"
                ).pack(side="left", padx=10)

        self.current_total = total
        self.total_label.configure(text=f"TOTAL: ₹ {total}")

    # ======================================================
    # PAYMENT WINDOW
    # ======================================================

    def open_payment(self):
        if not self.cart:
            play_project_sound("error")
            messagebox.showwarning(
                "Empty Cart",
                "Please select a coffee first.",
                parent=self
            )
            return

        total = calculate_total(self.cart, coffees)

        payment_window = ctk.CTkToplevel(self)
        payment_window.title("💳 Payment")
        payment_window.geometry("470x500")
        payment_window.resizable(False, False)
        payment_window.configure(fg_color=BG_COLOR)
        payment_window.transient(self)
        payment_window.grab_set()

        ctk.CTkLabel(
            payment_window,
            text="💳  PAYMENT",
            font=("Arial", 29, "bold"),
            text_color=CREAM
        ).pack(pady=(30, 15))

        payment_card = ctk.CTkFrame(
            payment_window,
            width=380,
            height=280,
            corner_radius=20,
            fg_color=CARD_COLOR
        )
        payment_card.pack(padx=30, pady=5)
        payment_card.pack_propagate(False)

        ctk.CTkLabel(
            payment_card,
            text=f"Amount to Pay\n₹ {total}",
            font=("Arial", 23, "bold"),
            text_color=GOLD,
            justify="center"
        ).pack(pady=(25, 8))

        ctk.CTkLabel(
            payment_card,
            text="Enter cash amount",
            font=("Arial", 14),
            text_color=GRAY
        ).pack(pady=3)

        amount_entry = ctk.CTkEntry(
            payment_card,
            placeholder_text="Enter amount",
            width=280,
            height=45,
            corner_radius=12,
            font=("Arial", 16)
        )
        amount_entry.pack(pady=12)
        amount_entry.focus()

        def make_payment():
            try:
                amount = float(amount_entry.get().strip())
            except ValueError:
                play_project_sound("error")
                messagebox.showerror(
                    "Invalid Amount",
                    "Please enter a valid amount.",
                    parent=payment_window
                )
                return

            success, change = check_payment(total, amount)

            if not success:
                play_project_sound("error")
                messagebox.showerror(
                    "Insufficient Amount",
                    f"Please pay at least ₹ {total}.",
                    parent=payment_window
                )
                return

            # Exact payment sound from the user's sounds folder.
            # Play it first and wait for it to finish before the coffee
            # making sound starts, so the two sounds do not overlap.
            play_project_sound("payment")
            payment_sound_duration = self.get_sound_duration_ms("payment")

            payment_window.destroy()

            self.after(
                max(payment_sound_duration + 100, 500),
                lambda: self.process_order(total, amount, change)
            )

        ctk.CTkButton(
            payment_card,
            text="✓  PAY NOW",
            width=280,
            height=48,
            corner_radius=13,
            fg_color=GREEN,
            hover_color="#279653",
            font=("Arial", 15, "bold"),
            command=make_payment
        ).pack(pady=10)

        ctk.CTkLabel(
            payment_window,
            text="Secure payment • Thank you for your order ☕",
            font=("Arial", 12),
            text_color=GRAY
        ).pack(pady=20)

        payment_window.bind("<Return>", lambda event: make_payment())

    # ======================================================
    # PROCESS ORDER
    # ======================================================

    def process_order(self, total, amount, change):
        order_id = uuid.uuid4().hex[:12].upper()

        # Database has order_id as PRIMARY KEY.
        # Therefore each cart item receives its own unique DB id.
        item_number = 0

        for coffee_name, quantity in self.cart.items():
            item_number += 1
            db_order_id = f"{order_id}-{item_number}"

            try:
                save_order(
                    db_order_id,
                    coffee_name,
                    quantity,
                    coffees[coffee_name]["price"] * quantity
                )
            except Exception as exc:
                # Do not crash the GUI if an old database contains a conflict.
                print("Database save error:", exc)

        try:
            bill_file = generate_bill(
                order_id,
                self.cart,
                coffees,
                total,
                amount,
                change
            )
            self.last_bill_path = os.path.abspath(
                os.path.join(BASE_DIR, bill_file)
            )
        except Exception as exc:
            print("Bill generation error:", exc)
            self.last_bill_path = None

        # Start the coffee-making sound immediately when preparation starts.
        self.show_processing_page(order_id, total, change)

    # ======================================================
    # PROCESSING PAGE
    # ======================================================

    def get_sound_duration_ms(self, kind):
        """Return the sound duration so success text appears after the sound ends."""
        path = find_sound_file(kind)
        if not path:
            return 0

        try:
            if path.lower().endswith(".wav"):
                with wave.open(path, "rb") as audio:
                    frames = audio.getnframes()
                    rate = audio.getframerate()
                    if rate:
                        return int((frames / float(rate)) * 1000)
        except Exception:
            pass

        # Fallback when duration cannot be read.
        return 2500

    def show_processing_page(self, order_id, total, change):
        self.clear_screen()

        frame = ctk.CTkFrame(self, fg_color=BG_COLOR)
        frame.pack(fill="both", expand=True)

        ctk.CTkLabel(
            frame,
            text="☕",
            font=("Segoe UI Emoji", 100),
            text_color=CREAM
        ).pack(pady=(120, 10))

        ctk.CTkLabel(
            frame,
            text="Preparing your coffee...",
            font=("Arial", 30, "bold"),
            text_color=CREAM
        ).pack(pady=10)

        ctk.CTkLabel(
            frame,
            text=f"Order ID: {order_id}\nPlease wait a moment ☕",
            font=("Arial", 15),
            text_color=GRAY,
            justify="center"
        ).pack(pady=8)

        progress = ctk.CTkProgressBar(
            frame,
            width=450,
            height=18,
            progress_color=COFFEE_BROWN
        )
        progress.pack(pady=25)
        progress.set(0)

        def animate(value=0):
            if not progress.winfo_exists():
                return
            value += 0.02
            if value <= 1:
                progress.set(value)
                self.after(100, lambda: animate(value))

        animate()

        # Play coffee-making sound as soon as the preparation screen appears.
        play_project_sound("making")

        # IMPORTANT: success screen waits for the coffee sound to finish.
        sound_duration = self.get_sound_duration_ms("making")
        wait_time = max(sound_duration + 300, 1200)

        self.after(
            wait_time,
            lambda: self.show_success_page(order_id, total, change)
        )

    # ======================================================
    # SUCCESS PAGE
    # ======================================================

    def show_success_page(self, order_id, total, change):
        self.clear_screen()

        frame = ctk.CTkFrame(self, fg_color=BG_COLOR)
        frame.pack(fill="both", expand=True)

        ctk.CTkLabel(
            frame,
            text="✓",
            font=("Arial", 100, "bold"),
            text_color=GREEN
        ).pack(pady=(85, 0))

        ctk.CTkLabel(
            frame,
            text="ORDER SUCCESSFUL!",
            font=("Arial", 32, "bold"),
            text_color=CREAM
        ).pack(pady=10)

        ctk.CTkLabel(
            frame,
            text="Your coffee is ready ☕",
            font=("Arial", 20),
            text_color=LIGHT_BROWN
        ).pack(pady=5)

        details = ctk.CTkFrame(
            frame,
            width=500,
            height=145,
            corner_radius=18,
            fg_color=CARD_COLOR
        )
        details.pack(pady=20)
        details.pack_propagate(False)

        ctk.CTkLabel(
            details,
            text=(
                f"Order ID: {order_id}\n"
                f"Total Paid: ₹ {total}\n"
                f"Change: ₹ {change}"
            ),
            font=("Arial", 15, "bold"),
            text_color=CREAM,
            justify="center"
        ).pack(expand=True)

        button_frame = ctk.CTkFrame(frame, fg_color="transparent")
        button_frame.pack(pady=5)

        ctk.CTkButton(
            button_frame,
            text="📄  OPEN BILL",
            width=180,
            height=45,
            corner_radius=12,
            fg_color=COFFEE_BROWN,
            hover_color=LIGHT_BROWN,
            font=("Arial", 14, "bold"),
            command=self.open_bill
        ).pack(side="left", padx=8)

        ctk.CTkButton(
            button_frame,
            text="☕  NEW ORDER",
            width=180,
            height=45,
            corner_radius=12,
            fg_color=GREEN,
            hover_color="#279653",
            font=("Arial", 14, "bold"),
            command=self.new_order
        ).pack(side="left", padx=8)

        ctk.CTkLabel(
            frame,
            text="Thank you for choosing our Coffee Vending Machine ❤️",
            font=("Arial", 13),
            text_color=GRAY
        ).pack(side="bottom", pady=25)

    # ======================================================
    # OPEN BILL
    # ======================================================

    def open_bill(self):
        if not self.last_bill_path:
            messagebox.showwarning(
                "Bill Not Found",
                "The bill could not be generated.",
                parent=self
            )
            return

        if not os.path.exists(self.last_bill_path):
            messagebox.showwarning(
                "Bill Not Found",
                "The bill file does not exist.",
                parent=self
            )
            return

        try:
            webbrowser.open("file:///" + self.last_bill_path.replace("\\", "/"))
        except Exception as exc:
            print("Could not open bill:", exc)
            messagebox.showinfo(
                "Bill Ready",
                f"Bill saved at:\n{self.last_bill_path}",
                parent=self
            )

    # ======================================================
    # NEW ORDER / CLEAR CART
    # ======================================================

    def new_order(self):
        play_project_sound("click")
        self.cart.clear()
        self.current_total = 0
        self.last_bill_path = None
        self.show_menu_page()


# ==========================================================
# RUN APPLICATION
# ==========================================================

if __name__ == "__main__":
    app = CoffeeVendingMachine()
    app.mainloop()

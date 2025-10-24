from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


SHIFT = 17  # Caesar cipher shift


def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


class CipherLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=15, **kwargs)

        self.add_widget(Label(text="Caesar Cipher (Shift = 17)", font_size=22, bold=True))

        self.input_box = TextInput(hint_text="Enter text here", multiline=True, size_hint_y=None, height=150)
        self.add_widget(self.input_box)

        btn_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        encrypt_btn = Button(text="Encrypt", background_color=(0.2, 0.6, 0.9, 1))
        decrypt_btn = Button(text="Decrypt", background_color=(0.9, 0.4, 0.3, 1))
        encrypt_btn.bind(on_press=self.encrypt_text)
        decrypt_btn.bind(on_press=self.decrypt_text)
        btn_layout.add_widget(encrypt_btn)
        btn_layout.add_widget(decrypt_btn)
        self.add_widget(btn_layout)

        self.output_box = TextInput(readonly=True, hint_text="Result will appear here", multiline=True)
        self.add_widget(self.output_box)

    def encrypt_text(self, instance):
        text = self.input_box.text
        encrypted = caesar_cipher(text, SHIFT)
        self.output_box.text = encrypted

    def decrypt_text(self, instance):
        text = self.input_box.text
        decrypted = caesar_cipher(text, -SHIFT)
        self.output_box.text = decrypted


class CaesarCipherApp(App):
    def build(self):
        return CipherLayout()


if __name__ == '__main__':
    CaesarCipherApp().run()
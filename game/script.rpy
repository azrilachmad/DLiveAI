# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
image model happy = "images/Model/base_model.png"

# Deklarasikan karakter yang digunakan di game.
define e = Character('Hanami', color="#00AFF0")

# Game dimulai disini.
label start:

    scene bg blck with dissolve
    e "Kamu telah Memprogram game Ren'Py (Project L: 001) baru."

    e "Setelah kamu menambahkan cerita, gambar, dan musik, kamu bisa merilis nya ke dunia!"

    return

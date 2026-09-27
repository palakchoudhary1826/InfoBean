import os
import winsound


def play_sound(file_name):

    file_path = os.path.join("sounds", file_name)

    if os.path.exists(file_path):

        try:
            winsound.PlaySound(
                file_path,
                winsound.SND_FILENAME | winsound.SND_ASYNC
            )

        except Exception:
            pass


def click_sound():
    play_sound("click.wav")


def success_sound():
    play_sound("success.wav")


def error_sound():
    play_sound("error.wav")


def making_sound():
    play_sound("making.wav")


def ready_sound():
    play_sound("ready.wav")
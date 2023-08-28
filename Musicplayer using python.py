import os
import pygame
import tkinter as tk
from tkinter import filedialog, messagebox

class MusicPlayer:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.root = tk.Tk()
        self.root.title("Music Player")
        self.root.geometry("300x100")
        self.root.configure(bg='light blue')

        self.playlist = []
        self.current_index = 0

        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        self.add_button = tk.Button(self.root, text="Add Songs",height= 1, command=self.add_songs)
        self.add_button.pack(fill=tk.X)

        self.play_button = tk.Button(self.root, text="Play",height= 2, command=self.play_song)
        self.play_button.pack(fill=tk.X)

        self.stop_button = tk.Button(self.root, text="Stop",height= 2, command=self.stop_song)
        self.stop_button.pack(fill=tk.X)

    def add_songs(self):
        songs = filedialog.askopenfilenames(title="Select Songs", filetypes=[("Audio Files", "*.mp3")])
        if songs:
            self.playlist.extend(songs)
            messagebox.showinfo("Songs Added", f"{len(songs)} songs added to the playlist!")

    def play_song(self):
        if not self.playlist:
            messagebox.showwarning("No Songs", "Please add songs to the playlist first.")
            return

        if pygame.mixer.music.get_busy():
            pygame.mixer.music.unpause()
        else:
            song_path = self.playlist[self.current_index]
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()

    def stop_song(self):
        pygame.mixer.music.stop()

if __name__ == "__main__":
    music_player = MusicPlayer()

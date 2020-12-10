import tkinter as tk


class GameObject(object):
    def __init__(self, cenv, root, tag, texture):
        self.tag = tag
        self.texture = texture
    
    def update(self):
        pass


class Player(GameObject):
    pass


class Enemy(GameObject):
    pass

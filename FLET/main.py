import flet as ft
from flet_core import ScrollMode
from flet_core.types import AppView

from CONTROLLER import FletGPT

from data import *


def main(page: ft.page):
 #   text = ft.Text('This is kcemma')
    page.title = 'KC EMMA CHAT BOT'
#    page.add(text)
    page.bg = PAGE_BG_COLOR
    page.scroll = ScrollMode.HIDDEN
    page.padding = 0

    page.update()
    fletgpt = FletGPT(page)
    page.add(fletgpt)


ft.app(target=main, view=ft.AppView.FLET_APP_WEB)

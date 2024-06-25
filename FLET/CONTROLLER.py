from data import  search_word_information
from data import *
from flet import *
from data import Default_prompts ,my_IMAGE_URL,chat_gpt ,search_word_information


class FletGPT(UserControl):
    def __init__(self, page):
        self.page = page
        self.prompts = []
        self.appname = self.page.title  # Consider removing if not used
        super().__init__()

    def new_chat(self, event):
        chat = Row(controls=[
            Icon(icons.MODE_COMMENT_OUTLINED, color=colors.GREEN_500),
            Text("New Chat", color=colors.WHITE),
        ])
        self.chat_history.controls.insert(0, chat)
        self.update()

    def send_message(self, e):
        pass

    def input_focus(self, e):
        self.send_message_btn.icon_color = colors.GREEN_400 if self.input.value else colors.GREY_500
        self.update()

# submit button
    def submit(self, e):
        self.applogo.visible = False
        self.responsive_prompt.visible = False
        self.conversations.visible = True

        if isinstance(e, ContainerTapEvent):
            prompt_value = f"{e.control.content.controls[0].value} {e.control.content.controls[0].spans[0].text[1:]}"
            message = Text(value=prompt_value)
        else:
            input_value = self.input.value
            message = Text(value=input_value)
        query_prompt = Container(
                alignment=alignment.top_left,
                padding=padding.symmetric(horizontal=50, vertical=30),
                content=Row(
                    wrap=True,
                    controls=[
                        Image(
                            src=my_IMAGE_URL,
                            height=25,
                            width=30
                        ),
                        message
                    ]
                )
        )
        self.input.value = ""
        self.update()
        api_response =search_word_information(message.value)

        response = Container(
            alignment=alignment.top_left,
            bgcolor=colors.SURFACE_VARIANT,
            padding=padding.symmetric(horizontal=50, vertical=30),
            content=Row(
                wrap=True,
                controls=[
                    Image(
                        src=chat_gpt,
                        height=25,
                        width=30
                    ),
                    Text(value=api_response)  # Replace "some" with actual response handling logic
                ]
            )
        )


        self.conversations.controls.append(response)
        self.update()

    def close_sidebar(self, e):
        self.left_navbar.visible = False
        self.applogo.margin = margin.only(bottom=200, top=50, left=500)
        self.text_interface.col = {"lg": 12}
        self.sidebar.visible = True
        self.update()

    def open_sidebar(self, e):
        self.left_navbar.visible = True
        self.applogo.margin = margin.only(bottom=200, top=50, left=300)
        self.text_interface.col = {"lg": 10}
        self.sidebar.visible = False
        self.update()

    def prompt_hover(self, event):
        event.control.bgcolor = colors.SURFACE_VARIANT if event.data == "true" else colors.WHITE
        event.control.content.controls[-1].visible = True if event.data == "true" else False
        self.update()

    def build(self):
        self.action_buttons = Row(
            controls=[
                Container(
                    padding=padding.symmetric(vertical=5),
                    border=border.all(1, colors.GREEN_400),
                    border_radius=1,
                    content=TextButton(
                        text="New Chat",
                        icon=icons.ADD,
                        icon_color=colors.WHITE,
                        style=ButtonStyle(color=colors.WHITE),
                        on_click=self.new_chat
                    )
                ),
                Container(
                    padding=padding.only(top=5, bottom=1),
                    border=border.all(1, colors.GREEN_400),
                    border_radius=5,
                    on_click=self.close_sidebar,
                    content=TextButton(
                        icon=icons.ADD,
                        icon_color=colors.WHITE,
                        style=ButtonStyle(color=colors.RED_200)
                    ),
                    tooltip='Close Sidebar'
                )
            ]
        )

        self.chat_history = ListView(width=200, height=450, expand=True, spacing=10)

        self.button_sheet = Column(
            controls=[
                Divider(thickness=2, height=2, color=colors.GREEN_500),
                Row(controls=[
                    Icon(icons.ACCOUNT_CIRCLE_OUTLINED, color=colors.WHITE),
                    Text("Upgrade to Plus", color=colors.WHITE)
                ]),
                Row(controls=[
                    Image(src="ass", width=23, height=25),
                    Text("KCEMMA", color=colors.WHITE)
                ])
            ]
        )

        self.applogo = Container(
            margin=margin.only(bottom=250, top=50, left=300),
            content=Text("KCEMMA GPT", color=colors.GREY_400, weight=FontWeight.BOLD, size=30)
        )

        self.sidebar = Container(
            border=border.all(1, colors.GREEN_400),
            border_radius=10,
            on_click=self.open_sidebar,
            content=TextButton(
                icon=icons.VIEW_SIDEBAR_OUTLINED,
                icon_color=colors.RED_100,
                style=ButtonStyle(color=colors.WHITE),
                tooltip='Open Sidebar'
            ),
            visible=False
        )

        self.input = TextField(
            hint_text="Send a message",
            border=InputBorder.NONE,
            cursor_color=colors.BLACK54,
            cursor_height=30,
            cursor_width=1,
            on_focus=self.input_focus,
            on_submit=self.submit
        )

        self.send_message_btn = IconButton(
            icon=icons.SEND,
            tooltip='Send message',
            icon_color=colors.BLACK54,
            on_click=self.submit
        )

        self.send_stack = Stack(
            controls=[
                Container(
                    height=50,
                    margin=margin.only(top=5),
                    padding=padding.symmetric(vertical=15, horizontal=5),
                    bgcolor=colors.WHITE,
                    border_radius=10,
                    content=self.input,
                    shadow=BoxShadow(
                        spread_radius=1,
                        blur_radius=15,
                        offset=Offset(0, 0),
                        color=colors.with_opacity(0.4, colors.BLACK54)
                    )
                ),
                Container(
                    content=self.send_message_btn,
                    margin=margin.only(left=800, top=10),
                    height=40,
                    width=30,
                    padding=2
                )
            ]
        )

        for button in Default_prompts:
            prompt = Container(
                padding=padding.symmetric(vertical=5, horizontal=10),
                border=border.all(1, color=colors.GREEN_500),
                border_radius=10,
                height=60,
                width=20,
                col={"lg": 6},
                on_click=self.submit,
                on_hover=self.prompt_hover,
                content=Row(
                    controls=[
                        Text(
                            value=button[0],
                            weight=FontWeight.BOLD,
                            style=TextThemeStyle.BODY_MEDIUM,
                            spans=[
                                TextSpan(
                                    text=button[1],
                                    style=TextStyle(size=12, weight=FontWeight.NORMAL)
                                )
                            ]
                        ),
                        Icon(icons.SEND_ROUNDED, color=colors.GREY_500, visible=False)
                    ]
                )
            )
            self.prompts.append(prompt)

        self.responsive_prompt = ResponsiveRow(
            controls=self.prompts
        )

        self.conversations = ListView(height=500, width=1000,expand=True,visible=False,spacing=20,auto_scroll=True)



        self.left_navbar = Container(
            bgcolor=colors.GREY_900,
            padding=5,
            width=450,
            height=620,
            col={"lg": 2},
            content=Column(
                expand=True,
                alignment=MainAxisAlignment.START,
                controls=[self.action_buttons, self.chat_history, self.button_sheet]
            )
        )

        self.text_interface = Container(
            height=620,
            width=1000,
            col={"lg": 10},
            padding=padding.symmetric(vertical=30, horizontal=100),
            bgcolor=colors.WHITE,
            content=Column(
                controls=[self.sidebar, self.applogo, self.responsive_prompt, self.conversations, self.send_stack]
            )
        )

        self.top_row = ResponsiveRow(
            alignment=MainAxisAlignment.START,
            controls=[self.left_navbar, self.text_interface]
        )

        return self.top_row

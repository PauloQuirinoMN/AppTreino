import flet as ft

def main(page: ft.Page):
    #page.bgcolor=ft.colors.BLUE
    

    perfil = ft.Container(
        bgcolor=ft.colors.WHITE,
        expand=3,
        content=ft.Column(
            [
                ft.Image(
                    src='perfil.jpeg',
                    border_radius=50,
                    height=80,
                    width=60,
                ),
                ft.Row([
                    ft.Column([
                        ft.Text('ACADEMIA:'),
                        ft.Text('Selft Parangaba')
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    horizontal_alignment=ft.CrossAxisAlignment.START),

                    ft.Column([
                        ft.Text('INSTRUTOR:'),
                        ft.Text('Zulu')
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    horizontal_alignment=ft.CrossAxisAlignment.START),

                    ft.Column([
                        ft.Text('INÍCIO:'),
                        ft.Text('29/05/2024')
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    horizontal_alignment=ft.CrossAxisAlignment.START),

                    ft.IconButton(icon=ft.icons.SETTINGS, icon_size=40)
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    fichas = ft.Container(
        bgcolor=ft.colors.WHITE,
        expand=2,
        content=ft.Row(
            [
                ft.Column([
                    ft.Image(src='a.png', height=50, width=50, color=ft.colors.BLACK),
                    ft.Text('Per/Pant', size=12, color=ft.colors.BLACK),
                ],
                alignment=ft.MainAxisAlignment.CENTER,),

                ft.Column([
                    ft.Image(src='b.png', height=50, width=50, color=ft.colors.BLACK),
                    ft.Text('Peit/Ombr', size=12, color=ft.colors.BLACK),
                ],
                alignment=ft.MainAxisAlignment.CENTER,),

                ft.Column([
                    ft.Image(src='c.png', height=50, width=50, color=ft.colors.BLACK),
                    ft.Text('Per/Post', size=12, color=ft.colors.BLACK),
                ],
                alignment=ft.MainAxisAlignment.CENTER,),

                ft.Column([
                    ft.Image(src='d.png', height=50, width=50, color=ft.colors.BLACK),
                    ft.Text('Cost/Bisc', size=12, color=ft.colors.BLACK),
                ],
                alignment=ft.MainAxisAlignment.CENTER,),

                ft.Column([
                    ft.Image(src='e.png', height=50, width=50, color=ft.colors.BLACK),
                    ft.Text('Peit/Tríc', size=12, color=ft.colors.BLACK),
                ],
                alignment=ft.MainAxisAlignment.CENTER,)
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND
        )
    )

    corpo = ft.Container(
        bgcolor=ft.colors.WHITE,
        expand=6,
        content=ft.Column(
            [
                ft.Container(
                    #border=ft.Border(2),
                    bgcolor=ft.colors.WHITE,
                    content=ft.Row(
                        [
                            ft.Column([
                                ft.TextButton('INICÍAR TREINO', style=ft.ButtonStyle(color=ft.colors.AMBER, bgcolor=ft.colors.WHITE),),
                                ft.TextButton('Leg Press 45º + Agachamento    P.C 4 x 12 + 10', style=ft.ButtonStyle(color=ft.colors.AMBER, bgcolor=ft.colors.WHITE), disabled=True),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                            horizontal_alignment=ft.CrossAxisAlignment.START,),


                            ft.Column([
                                ft.Text('SÉRIE:', style=ft.TextStyle(size=15, color=ft.colors.AMBER, bgcolor=ft.colors.WHITE)),
                                ft.Text('2', color=ft.colors.AMBER)
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,),
                        ]
                    ),
                ),

                ft.Container(
                    bgcolor=ft.colors.WHITE,
                    content=ft.Column([
                            ft.Row(
                                [
                                    ft.TextButton('Agachamento guiado + Afundo  4 x 10 + 10', style=ft.ButtonStyle(color=ft.colors.AMBER, bgcolor=ft.colors.WHITE)),
                                    ft.Checkbox(),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            ft.Row(
                                [
                                    ft.TextButton('Leg horizontal unilateral  4 x 12+ S.I', style=ft.ButtonStyle(color=ft.colors.AMBER, bgcolor=ft.colors.WHITE)),
                                    ft.Checkbox(),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            ft.Row(
                                [
                                    ft.TextButton('Adutoa   4 x 12 + 10', style=ft.ButtonStyle(color=ft.colors.AMBER, bgcolor=ft.colors.WHITE)),
                                    ft.Checkbox(),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            ft.Row(
                                [
                                    ft.TextButton('Passada 1 x 60 passos', style=ft.ButtonStyle(color=ft.colors.AMBER, bgcolor=ft.colors.WHITE)),
                                    ft.Checkbox(),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            ft.Row(
                                [
                                    ft.TextButton('Panturrilha Sentado + em pé  4 x 20 + 8+8+12', style=ft.ButtonStyle(color=ft.colors.AMBER, bgcolor=ft.colors.WHITE)),
                                    ft.Checkbox(),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                        ]
                    )
                )
            ]
        )
    )


    rodape = ft.Container(
        bgcolor=ft.colors.WHITE,
        expand=2,
        content=ft.Column([
            ft.Row(
                [
                    ft.Text('00:00:00', size=40),
                    ft.Column([
                        ft.TextButton(icon=ft.icons.PLAY_CIRCLE),
                        ft.TextButton(icon=ft.icons.PAUSE_CIRCLE)
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),

            ft.Row([
                ft.TextButton(text='sair', width=100)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.START,)
        ],)
    )


    layout = ft.Container(
        alignment=ft.alignment.center, 
        border_radius=30,       
        height=700,
        width=400,
        bgcolor=ft.colors.BLACK,
        shadow=ft.BoxShadow(
            spread_radius=0,
            blur_radius=10,
            color=ft.colors.BLUE,
            blur_style=ft.ShadowBlurStyle.OUTER,
        ),
        content=ft.Column(
            [
                perfil,
                fichas,
                corpo,
                rodape
            ],
            spacing=1,
        )
    )


    page.add(layout)

if __name__ ==  '__main__':
    ft.app(target=main, view=ft.AppView.FLET_APP, assets_dir='assets')
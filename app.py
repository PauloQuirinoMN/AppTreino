import flet as ft

def main(page: ft.Page):
    #page.bgcolor=ft.colors.BLUE
    

    perfil = ft.Container(
        bgcolor=ft.colors.TRANSPARENT,
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
                        ft.Text('ACADEMIA:', color=ft.colors.WHITE),
                        ft.Text('Selft Parangaba', color=ft.colors.WHITE)
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    horizontal_alignment=ft.CrossAxisAlignment.START),

                    ft.Column([
                        ft.Text('INSTRUTOR:', color=ft.colors.WHITE),
                        ft.Text('Zulu', color=ft.colors.WHITE)
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    horizontal_alignment=ft.CrossAxisAlignment.START),

                    ft.Column([
                        ft.Text('INÍCIO:', color=ft.colors.WHITE),
                        ft.Text('29/05/2024', color=ft.colors.WHITE)
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
        bgcolor=ft.colors.TRANSPARENT,
        expand=2,
        content=ft.Row(
            [
                ft.Column([
                    ft.Image(src='a.png', height=50, width=50, color=ft.colors.WHITE),
                    ft.Text('Per/Pant', size=12, color=ft.colors.WHITE),
                ],
                alignment=ft.MainAxisAlignment.CENTER,),

                ft.Column([
                    ft.Image(src='b.png', height=50, width=50, color=ft.colors.WHITE),
                    ft.Text('Peit/Ombr', size=12, color=ft.colors.WHITE),
                ],
                alignment=ft.MainAxisAlignment.CENTER,),

                ft.Column([
                    ft.Image(src='c.png', height=50, width=50, color=ft.colors.WHITE),
                    ft.Text('Per/Post', size=12, color=ft.colors.WHITE),
                ],
                alignment=ft.MainAxisAlignment.CENTER,),

                ft.Column([
                    ft.Image(src='d.png', height=50, width=50, color=ft.colors.WHITE),
                    ft.Text('Cost/Bisc', size=12, color=ft.colors.WHITE),
                ],
                alignment=ft.MainAxisAlignment.CENTER,),

                ft.Column([
                    ft.Image(src='e.png', height=50, width=50, color=ft.colors.WHITE),
                    ft.Text('Peit/Tríc', size=12, color=ft.colors.WHITE),
                ],
                alignment=ft.MainAxisAlignment.CENTER,)
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND
        )
    )

    corpo = ft.Container(
        bgcolor=ft.colors.TRANSPARENT,
        expand=6,
        content=ft.Column(
            [
                ft.Container(
                    border_radius=10,
                    border=ft.Border(top=ft.border.all(width=2.0)), #color=ft.colors.BLUE)),
                    bgcolor=ft.colors.TRANSPARENT,
                    content=ft.Row(
                        [
                            ft.Column([
                                ft.Text('  INICÍAR', color=ft.colors.GREEN, size=18),
                                ft.TextButton('Leg Press 45º + Agachamento    P.C 4 x 12 + 10', height=35, style=ft.ButtonStyle(color=ft.colors.BLUE_100, bgcolor=ft.colors.BLACK, side=ft.BorderSide(width=0.5, color=ft.colors.WHITE)), disabled=True),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                            horizontal_alignment=ft.CrossAxisAlignment.START,),


                            ft.Column([
                                ft.Text('SÉRIE:', style=ft.TextStyle(size=15, color=ft.colors.WHITE, bgcolor=ft.colors.TRANSPARENT)),
                                ft.Text('2', color=ft.colors.AMBER)
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,),
                        ],
                        spacing=20,
                        
                    ),
                ),

                ft.Container(
                    bgcolor=ft.colors.TRANSPARENT,
                    content=ft.Column([
                            ft.Row(
                                [
                                    ft.TextButton('Leg Press 45º + Agachamento    P.C 4 x 12 + 10', style=ft.ButtonStyle(color=ft.colors.WHITE, bgcolor=ft.colors.BLACK)),
                                    ft.Checkbox(),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            ),

                            ft.Row(
                                [
                                    ft.TextButton('Agachamento guiado + Afundo  4 x 10 + 10', style=ft.ButtonStyle(color=ft.colors.WHITE, bgcolor=ft.colors.BLACK)),
                                    ft.Checkbox(),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            ),

                            ft.Row(
                                [
                                    ft.TextButton('Leg horizontal unilateral  4 x 12+ S.I', style=ft.ButtonStyle(color=ft.colors.WHITE, bgcolor=ft.colors.BLACK)),
                                    ft.Checkbox(),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            ),

                            ft.Row(
                                [
                                    ft.TextButton('Adutoa   4 x 12 + 10', style=ft.ButtonStyle(color=ft.colors.WHITE, bgcolor=ft.colors.BLACK)),
                                    ft.Checkbox(),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            ),

                            ft.Row(
                                [
                                    ft.TextButton('Passada 1 x 60 passos', style=ft.ButtonStyle(color=ft.colors.WHITE, bgcolor=ft.colors.BLACK)),
                                    ft.Checkbox(),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            ),

                            ft.Row(
                                [
                                    ft.TextButton('Panturrilha Sentado + em pé  4 x 20 + 8+8+12', style=ft.ButtonStyle(color=ft.colors.WHITE, bgcolor=ft.colors.BLACK)),
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
        bgcolor=ft.colors.TRANSPARENT,
        expand=2,
        content=ft.Column([
            ft.Row(
                [
                    ft.Text('       00:00:00', size=50, color=ft.colors.WHITE),
                    ft.Column([
                        ft.TextButton(icon=ft.icons.PLAY_CIRCLE),
                        ft.TextButton(icon=ft.icons.PAUSE_CIRCLE)
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                run_spacing=(20)
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
            spacing=0,
        )
    )


    page.add(layout)

if __name__ ==  '__main__':
    ft.app(target=main, view=ft.AppView.FLET_APP, assets_dir='assets')
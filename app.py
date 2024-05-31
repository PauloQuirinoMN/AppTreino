import flet as ft

def main(page: ft.Page):
    #page.bgcolor=ft.colors.BLUE
    

    perfil = ft.Container(
        bgcolor=ft.colors.TRANSPARENT,
        #expand=2,
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

                    ft.IconButton(icon=ft.icons.MENU, icon_size=40)
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
        padding=5,
        content=ft.Row(
            [
                ft.Container(
                    border=ft.border.all(0.5, color=ft.colors.BLUE),
                    border_radius=ft.border_radius.all(10),
                    padding=ft.padding.all(5),
                    content=ft.Column([
                    ft.Image(src='a.png', height=50, width=50, color=ft.colors.WHITE),
                    ft.Text('Per/Pant', size=12, color=ft.colors.WHITE),
                ],
                alignment=ft.MainAxisAlignment.CENTER,)
                ),

                ft.Container(
                    border=ft.border.all(0.5, color=ft.colors.BLUE),
                    border_radius=ft.border_radius.all(10),
                    padding=ft.padding.all(5),
                    content=ft.Column([
                    ft.Image(src='b.png', height=50, width=50, color=ft.colors.WHITE),
                    ft.Text('Per/Pant', size=12, color=ft.colors.WHITE),
                ],
                alignment=ft.MainAxisAlignment.CENTER,)
                ),

                ft.Container(
                    border=ft.border.all(0.5, color=ft.colors.BLUE),
                    border_radius=ft.border_radius.all(10),
                    padding=ft.padding.all(5),
                    content=ft.Column([
                    ft.Image(src='c.png', height=50, width=50, color=ft.colors.WHITE),
                    ft.Text('Per/Pant', size=12, color=ft.colors.WHITE),
                ],
                alignment=ft.MainAxisAlignment.CENTER,)
                ),

                ft.Container(
                    border=ft.border.all(0.5, color=ft.colors.BLUE),
                    border_radius=ft.border_radius.all(10),
                    padding=ft.padding.all(5),
                    content=ft.Column([
                    ft.Image(src='d.png', height=50, width=50, color=ft.colors.WHITE),
                    ft.Text('Per/Pant', size=12, color=ft.colors.WHITE),
                ],
                alignment=ft.MainAxisAlignment.CENTER,)
                ),

                ft.Container(
                    border=ft.border.all(0.5, color=ft.colors.BLUE),
                    border_radius=ft.border_radius.all(10),
                    padding=ft.padding.all(5),
                    content=ft.Column([
                    ft.Image(src='e.png', height=50, width=50, color=ft.colors.WHITE),
                    ft.Text('Per/Pant', size=12, color=ft.colors.WHITE),
                ],
                alignment=ft.MainAxisAlignment.CENTER,)
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
        )
    )
    mostrador = ft.Container(
        border_radius=10,
        border=ft.border.all(width=1.5, color=ft.colors.BLUE),
        margin=ft.margin.all(10),
        bgcolor=ft.colors.WHITE10,
        padding=5,
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.ElevatedButton('INICÍAR', height=20, width=100, bgcolor=ft.colors.TRANSPARENT, ),
                        ft.Text('00:00:00', height=20, weight=100, color=ft.colors.WHITE),
                        ft.ElevatedButton('finalizar', height=20, width=100, bgcolor=ft.colors.TRANSPARENT),
                        ft.Text('SÉRIE:', style=ft.TextStyle(size=15, color=ft.colors.WHITE, bgcolor=ft.colors.TRANSPARENT)),
                       
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),

                ft.Divider(color=ft.colors.BLUE, height=10),

                ft.Row(
                    [
                        ft.Text('Leg Press 45º + Agachamento    P.C 4 x 12 + 10', size=13, color=ft.colors.WHITE),
                        ft.Text('3  ', color=ft.colors.AMBER, size=25),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
            ]         
        ),
    )
    
    corpo = ft.Container(
        bgcolor=ft.colors.TRANSPARENT,
        padding=0,
        #expand=6,
        content=ft.Column(
            [
                ft.Container(
                    border=ft.border.all(1.5, color=ft.colors.BLUE),
                    border_radius=ft.border_radius.all(10),
                    margin=ft.margin.all(10),
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
        alignment=ft.alignment.center,
        border=ft.border.all(1.5, color=ft.colors.BLUE),
        border_radius=ft.border_radius.all(10),
        bgcolor=ft.colors.TRANSPARENT,
        padding=ft.Padding(left=90, top=5, bottom=5, right=1),
        margin=10,
        #expand=2,
        content=ft.Column([
            ft.Row(
                [
                    ft.Text('00:00:00', size=40, color=ft.colors.WHITE),
                    ft.Column([
                        ft.TextButton(icon=ft.icons.PLAY_CIRCLE),
                        ft.TextButton(icon=ft.icons.PAUSE_CIRCLE)
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
        horizontal_alignment=ft.CrossAxisAlignment.START,
        )
    )

    sair = ft.Container(
        content=ft.Row([
            ft.TextButton(text='sair', width=60, height=20, )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )


    layout = ft.Container(
        alignment=ft.alignment.center,
        margin=ft.margin.all(5),
        border_radius=30,
        border=ft.border.all(1.5, color=ft.colors.GREEN),
        padding=ft.padding.all(5),     
        height=750,
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
                mostrador,
                corpo,
                rodape,
                sair,
            ]
        ),
    )


    page.add(layout)

if __name__ ==  '__main__':
    ft.app(target=main, view=ft.AppView.FLET_APP, assets_dir='assets')
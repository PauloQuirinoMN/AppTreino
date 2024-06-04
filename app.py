import flet as ft

def main(page: ft.Page):
    page.bgcolor=ft.colors.BLACK87
    page.scroll=True

    perfil = ft.Container(
        border_radius=ft.border_radius.all(5),
        expand=2,
        content=ft.Column(
            [
                ft.Image(
                    src='perfil.jpeg',
                    border_radius=15,
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

                    ft.PopupMenuButton(items=[
                        ft.PopupMenuItem(text='Editar Perfil'),
                        ft.PopupMenuItem(text='Adicionar Treino')
                    ])
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ) 
    )
    
    fichas = ft.Container(
        border_radius=ft.border_radius.all(5),
        expand=1,
        content=ft.Row(
            [
                ft.Container(
                    bgcolor=ft.colors.WHITE10,
                    border_radius=10,
                    border=ft.border.all(5),
                    content=ft.Column([
                    ft.Image(src='a.png', height=25, width=30, color=ft.colors.WHITE),
                    ft.Text('Per/Pant', size=12, color=ft.colors.WHITE),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,)
                ),

                ft.Container(
                    bgcolor=ft.colors.WHITE10,
                    border_radius=10,
                    border=ft.border.all(5),
                    content=ft.Column([
                    ft.Image(src='b.png', height=25, width=30, color=ft.colors.WHITE),
                    ft.Text('Per/Pant', size=12, color=ft.colors.WHITE),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER)
                ),

                ft.Container(
                    bgcolor=ft.colors.WHITE10,
                    border_radius=10,
                    border=ft.border.all(5),
                    content=ft.Column([
                    ft.Image(src='c.png', height=25, width=30, color=ft.colors.WHITE),
                    ft.Text('Per/Pant', size=12, color=ft.colors.WHITE),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER)
                ),

                ft.Container(
                    bgcolor=ft.colors.WHITE10,
                    border_radius=10,
                    border=ft.border.all(5),
                    content=ft.Column([
                    ft.Image(src='d.png', height=25, width=30, color=ft.colors.WHITE),
                    ft.Text('Per/Pant', size=12, color=ft.colors.WHITE),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER)
                ),

                ft.Container(
                    bgcolor=ft.colors.WHITE10,
                    border_radius=10,
                    border=ft.border.all(5),
                    content=ft.Column([
                    ft.Image(src='e.png', height=25, width=30, color=ft.colors.WHITE),
                    ft.Text('Per/Pant', size=12, color=ft.colors.WHITE),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER)
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        )
    )
    mostrador = ft.Container(
        expand=2,
        border_radius=10,
        border=ft.border.all(5),
        bgcolor=ft.colors.WHITE10,
        padding=5,
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.ElevatedButton('INICÍAR', height=20, width=100, bgcolor=ft.colors.TRANSPARENT, color=ft.colors.GREEN_100),
                        ft.Text('00:00:00', height=20, weight=100, color=ft.colors.WHITE),
                        ft.ElevatedButton('finalizar', height=20, width=100, bgcolor=ft.colors.TRANSPARENT, color=ft.colors.RED_100),                   
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),

                ft.Divider(color=ft.colors.BLUE_100, height=1),

                ft.Row(
                    [
                        ft.Text('SÉRIE:', color=ft.colors.WHITE),
                        ft.Text('2', size=25, color=ft.colors.WHITE),
                        ft.Text('CARGA: ', color=ft.colors.WHITE),
                        ft.TextField('110', text_size=25,height=50, width=80, color=ft.colors.RED_300, border_radius=ft.border_radius.all(0)),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),

                ft.Row(
                    [
                        ft.Text('Leg Press 45º + Agachamento    P.C 4 x 12 + 10', size=16, color=ft.colors.WHITE),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),   
            ]         
        ),
    )
    
    corpo = ft.Container(
        border_radius=ft.border_radius.all(10),
        expand=3,
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

   


    cronometro = ft.Container(
        expand=1,
        border_radius=ft.border_radius.all(5),
        alignment=ft.alignment.center,
        padding=ft.Padding(left=90, top=5, bottom=5, right=1),
        content=ft.Column([
            ft.Row(
                [
                    ft.Text('00:00:00', size=40, color=ft.colors.WHITE),
                    ft.Column([
                        ft.IconButton(icon=ft.icons.PLAY_CIRCLE, icon_color=ft.colors.GREEN_100),
                        ft.IconButton(content=ft.Image(src='reset.png', height=30, width=25, color=ft.colors.AMBER)),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
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
        margin=ft.Margin(left=1, top=0, right=1, bottom=8),
        border_radius=ft.border_radius.all(5),
        content=ft.Row([
            ft.TextButton(text='sair', width=60, height=20)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.START,
        ),
    )


    layout = ft.Container(
        border=ft.border.all(1, color=ft.colors.WHITE),
        #image_src='bgcinza.jpg',
        image_repeat=ft.ImageRepeat.REPEAT,
        alignment=ft.alignment.center,
        border_radius=5,
        height=750,
        width=400,
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
                cronometro,
                corpo,
                sair,
            ],
            spacing=1,
        ),
    )


    page.add(layout)

if __name__ ==  '__main__':
    ft.app(target=main, view=ft.AppView.FLET_APP, assets_dir='assets')
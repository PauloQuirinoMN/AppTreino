import flet as ft

def main(page: ft.Page):
    page.bgcolor=ft.colors.BLACK

    perfil = ft.Container(
        bgcolor=ft.colors.WHITE38,
        border=ft.Border(top=ft.BorderSide(width=1, color=ft.colors.GREEN), bottom=ft.BorderSide(width=1, color=ft.colors.GREEN), left=ft.BorderSide(1, color=ft.colors.GREEN), right=ft.BorderSide(1, color=ft.colors.GREEN)),
        margin=8,
        border_radius=5,
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
                        ft.Text('ACADEMIA:', color=ft.colors.BLACK),
                        ft.Text('Selft Parangaba', color=ft.colors.BLACK),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    ),
            
                    ft.Column([
                        ft.Text('INSTRUTOR:', color=ft.colors.BLACK),
                        ft.Text('Zulu', color=ft.colors.BLACK)
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    horizontal_alignment=ft.CrossAxisAlignment.START),

                    ft.Column([
                        ft.Text('INÍCIO:', color=ft.colors.BLACK),
                        ft.Text('29/05/2024', color=ft.colors.BLACK)
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    horizontal_alignment=ft.CrossAxisAlignment.START),

                    ft.PopupMenuButton(
                        icon_size=35,
                        icon_color=ft.colors.GREEN_100,
                        items=[
                        ft.PopupMenuItem(text='Editar Perfil'),
                        ft.PopupMenuItem(text='Adicionar Treino'),
                        ft.PopupMenuItem(text='Editar Treino'),
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
                    height=50,
                    width=50,
                    bgcolor='#CBCBC7',
                    border_radius=100,
                    border=ft.Border(top=ft.BorderSide(2, color=ft.colors.GREEN), right=ft.BorderSide(2, color=ft.colors.GREEN),left=ft.BorderSide(2, color=ft.colors.GREEN),bottom=ft.BorderSide(2, color=ft.colors.GREEN)),
                    content=ft.Row(
                        [
                            ft.Image(src='a.png', height=25, width=30, color=ft.colors.BLACK),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    )
                ),
                
                ft.Container(
                    height=50,
                    width=50,
                    bgcolor='#CBCBC7',
                    border_radius=100,
                    border=ft.Border(top=ft.BorderSide(2, color=ft.colors.GREEN), right=ft.BorderSide(2, color=ft.colors.GREEN),left=ft.BorderSide(2, color=ft.colors.GREEN),bottom=ft.BorderSide(2, color=ft.colors.GREEN)),
                    content=ft.Row(
                        [
                            ft.Image(src='b.png', height=25, width=30, color=ft.colors.BLACK),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    )
                ),

                ft.Container(
                    height=50,
                    width=50,
                    bgcolor='#CBCBC7',
                    border_radius=100,
                    border=ft.Border(top=ft.BorderSide(2, color=ft.colors.GREEN), right=ft.BorderSide(2, color=ft.colors.GREEN),left=ft.BorderSide(2, color=ft.colors.GREEN),bottom=ft.BorderSide(2, color=ft.colors.GREEN)),
                    content=ft.Row(
                        [
                            ft.Image(src='c.png', height=25, width=30, color=ft.colors.BLACK),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    )
                ),

                ft.Container(
                    height=50,
                    width=50,
                    bgcolor='#CBCBC7',
                    border_radius=100,
                    border=ft.Border(top=ft.BorderSide(2, color=ft.colors.GREEN), right=ft.BorderSide(2, color=ft.colors.GREEN),left=ft.BorderSide(2, color=ft.colors.GREEN),bottom=ft.BorderSide(2, color=ft.colors.GREEN)),
                    content=ft.Row(
                        [
                            ft.Image(src='d.png', height=25, width=30, color=ft.colors.BLACK),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    )
                ),

                ft.Container(
                    height=50,
                    width=50,
                    bgcolor='#CBCBC7',
                    border_radius=100,
                    border=ft.Border(top=ft.BorderSide(2, color=ft.colors.GREEN), right=ft.BorderSide(2, color=ft.colors.GREEN),left=ft.BorderSide(2, color=ft.colors.GREEN),bottom=ft.BorderSide(2, color=ft.colors.GREEN)),
                    content=ft.Row(
                        [
                            ft.Image(src='e.png', height=25, width=30, color=ft.colors.BLACK),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    )
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        )
    )

    mostrador = ft.Container(
        border_radius=5,
        padding=5,
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.ElevatedButton('INICÍAR', height=20, width=100, bgcolor=ft.colors.BLACK12, color=ft.colors.WHITE),
                        ft.Text('00:00:00', height=20, weight=100, color=ft.colors.BLACK),
                        ft.ElevatedButton('FINALIZAR', height=20, width=120, bgcolor=ft.colors.BLACK38, color=ft.colors.WHITE),                   
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),

                ft.Row(
                    [
                        ft.Text('SÉRIE:', color=ft.colors.BLACK),
                        ft.Text('2', size=25, color=ft.colors.BLACK),
                        ft.Text('CARGA: ', color=ft.colors.BLACK),
                        ft.TextField('110', text_size=25,height=50, width=80, text_align=ft.TextAlign.CENTER ,color=ft.colors.BLACK, border_radius=ft.border_radius.all(15)),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),

                ft.Divider(color=ft.colors.GREEN_100, height=2),

                ft.Row(
                    [
                        ft.Text('Leg Press 45º + Agachamento    P.C 4 x 12 + 10', size=15, color=ft.colors.BLACK, text_align=ft.TextAlign.CENTER),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ), 

                ft.Divider(color=ft.colors.GREEN_100, height=2),  
            ]         
        ),
    )
    
    corpo = ft.Container(
        #border=ft.Border(bottom=ft.BorderSide(width=0.5, color=ft.colors.WHITE), top=ft.BorderSide(0.5, color=ft.colors.WHITE)),
        margin=0,
        padding=5,
        border_radius=ft.BorderRadius(top_left=5, top_right=5, bottom_left=5, bottom_right=5),
        #expand=3,
            content=ft.Column([
                ft.Row(
                    [
                        ft.TextButton('Leg Press 45º + Agachamento    P.C 4 x 12 + 10', style=ft.ButtonStyle(color=ft.colors.BLACK, bgcolor=ft.colors.TRANSPARENT)),
                        ft.Checkbox(),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),

                ft.Row(
                    [
                        ft.TextButton('Agachamento guiado + Afundo  4 x 10 + 10', style=ft.ButtonStyle(color=ft.colors.BLACK, bgcolor=ft.colors.TRANSPARENT)),
                        ft.Checkbox(),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),

                ft.Row(
                    [
                        ft.TextButton('Leg horizontal unilateral  4 x 12+ S.I', style=ft.ButtonStyle(color=ft.colors.BLACK, bgcolor=ft.colors.TRANSPARENT)),
                        ft.Checkbox(),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),

                ft.Row(
                    [
                        ft.TextButton('Adutoa   4 x 12 + 10', style=ft.ButtonStyle(color=ft.colors.BLACK, bgcolor=ft.colors.TRANSPARENT)),
                        ft.Checkbox(),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),

                ft.Row(
                    [
                        ft.TextButton('Passada 1 x 60 passos', style=ft.ButtonStyle(color=ft.colors.BLACK, bgcolor=ft.colors.TRANSPARENT)),
                        ft.Checkbox(),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),

                ft.Row(
                    [
                        ft.TextButton('Panturrilha Sentado + em pé  4 x 20 + 8+8+12', style=ft.ButtonStyle(color=ft.colors.BLACK, bgcolor=ft.colors.TRANSPARENT)),
                        ft.Checkbox(),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ],
            spacing=2,
        )
    )

   


    cronometro = ft.Container(
        expand=1.3,
        padding=5,
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Text('         00:00:00', size=40, color=ft.colors.WHITE),
                        ft.IconButton(icon=ft.icons.PLAY_CIRCLE, icon_color='#CBCBC7'),
                        ft.IconButton(content=ft.Image(src='reset.png', height=30, width=25, color='#9B6A44')),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),

                ft.Container(
                    margin=ft.Margin(left=5, top=3, bottom=0, right=5),
                    bgcolor='#CBCBC7',
                    border_radius=ft.BorderRadius(top_left=5, top_right=5, bottom_left=5, bottom_right=5),
                    border=ft.Border(top=ft.BorderSide(1, color=ft.colors.BLUE), right=ft.BorderSide(1, color=ft.colors.BLUE), left=ft.BorderSide(1, color=ft.colors.BLUE), bottom=ft.BorderSide(1, color=ft.colors.BLUE)),
                    content=ft.Row(
                        [
                            ft.Text('TREINO: ', color=ft.colors.BLACK),
                            ft.Image(src='a.png', height=20, width=15, color=ft.colors.BLACK),
                            ft.Text('Pern/Pant', color=ft.colors.BLACK, size=18),
                            ft.Text('Qt:', color=ft.colors.BLACK, size=18),
                            ft.Text('0', color=ft.colors.BLACK, size=18)
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    )
                ),
            ],
            alignment=ft.alignment.center,
        )
    )

    sair = ft.Container(
        expand=0.5,
        margin=ft.Margin(left=1, top=3, right=1, bottom=3),
        border_radius=ft.border_radius.all(5),
        content=ft.Row([
            ft.TextButton(text='sair', width=60, height=20, style=ft.ButtonStyle(bgcolor=ft.colors.WHITE38, color=ft.colors.BLACK))
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.START,
        ),
    )

    ficha = ft.Container(
        bgcolor=ft.colors.WHITE38,
        margin=ft.Margin(left=10, top=0, right=10, bottom=0),
        expand=5,
        border=ft.border.all(1, color=ft.colors.GREEN),
        border_radius=ft.border_radius.all(10),
        content=ft.Column(
            [
                mostrador,
                corpo
            ],
            spacing=3,
        )
    )

    layout = ft.Container(
        bgcolor=ft.colors.WHITE10,
        border=ft.border.all(1, color=ft.colors.GREEN),
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
                cronometro,
                ficha,
                sair,
            ],
            spacing=0,
        ),
    )


    page.add(layout)

if __name__ ==  '__main__':
    ft.app(target=main, view=ft.AppView.FLET_APP, assets_dir='assets')
import flet as ft

def main(page: ft.Page):
    

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
        bgcolor=ft.colors.BLACK,
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
            alignment=ft.MainAxisAlignment.SPACE_AROUND,


        )
    )

    corpo = ft.Container(
        bgcolor=ft.colors.WHITE12,
        expand=6,
    )

    rodape = ft.Container(
        bgcolor=ft.colors.WHITE24,
        expand=2
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
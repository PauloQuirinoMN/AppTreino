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
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER),

                    ft.Column([
                        ft.Text('INSTRUTOR:'),
                        ft.Text('Zulu')
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER),

                    ft.Column([
                        ft.Text('INÍCIO:'),
                        ft.Text('29/05/2024')
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER),

                    ft.IconButton(icon=ft.icons.SETTINGS, icon_size=40)
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    fichas = ft.Container(
        bgcolor=ft.colors.WHITE10,
        expand=2,
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
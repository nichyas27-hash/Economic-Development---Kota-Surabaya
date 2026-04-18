from dash import html, Input, Output, callback, ctx

info_card = {
    "title": "SDG 8: Decent Work and Economic Growth",
    "desc": "Mendorong pertumbuhan ekonomi yang inklusif dan menyediakan pekerjaan yang layak.",
    "example": "Pengembangan UMKM dan pelatihan kerja."
}

@callback(
    Output("info_card", "is_open"),
    Output("modal-content", "children"),
    Input("indicator_cards", "n_clicks"),
    prevent_initial_call=True
)
def open_modal(n):

    if n:
        return True, html.Div([
            html.H5(info_card["title"]),
            html.Br(),
            html.B("Deskripsi:"),
            html.P(info_card["desc"]),
            html.Br(),
            html.B("Contoh:"),
            html.P(info_card["example"]),
        ], style={"textAlign": "justify"})

    return False, ""
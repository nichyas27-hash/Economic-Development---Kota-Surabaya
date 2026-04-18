from dash import html, Input, Output, callback, ctx
import urllib.parse
import dash

@callback(
    Output("redirect", "href"),
    Input("search-box", "n_submit"),
    Input("search-box", "value"),
    prevent_initial_call=True
)

def search(n_submit, value):
    if n_submit and value:
        query = urllib.parse.quote(value)
        return f"https://www.google.com/search?q={query}"

    return dash.no_update
import ipywidgets as ipw


def get_start_widget(appbase, jupbase, notebase):
    return ipw.HTML(
        f"""
    <div align="center">
        <a href="{appbase}/main.ipynb" target="_blank">
            <img src="https://www.anti-bias.eu/wp-content/webp-express/webp-images/uploads/2015/01/shutterstock_92612287-e1420280083718.jpg.webp" width="240px">
        </a>
    </div>"""
    )


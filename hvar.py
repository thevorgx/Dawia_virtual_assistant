"""This file contains the HTML/css variables used in the app.py file for streamlit."""

from source.tools_manager import img_to_base64

dawia_logo = img_to_base64("./assets/img/dawia.png")
ghub_logo = img_to_base64("./assets/img/git.png")

page_title = f'''
    <div style="display: flex; align-items: center;">
        <img src="data:image/png;base64,{dawia_logo}" width="80" style="margin-right: 10px;"/>
        <h1 style="margin: 0;">Dawia Assist</h1>
    </div>
    '''

github_link = f'''
    <div style="display: flex; align-items: center;">
        <img src="data:image/png;base64,{ghub_logo}" width="30"/>
        <span style="margin-left: 30px; font-size: 20px;">
            This project is open source, and it will always be. If you have any ideas or suggestions, feel free to open an issue or submit a pull request. <a href="https://github.com/thevorgx/Dawia_virtual_assistant" target="_blank" style="color:#ff4b4b;">here</a>
        </span>
    </div>
'''

get_key = f"""Don\'t have an API key? <a href="https://www.youtube.com/watch?v=PMVXDzXd-2c" target="_blank" style="color:#60b4ff;">click here</a>"""

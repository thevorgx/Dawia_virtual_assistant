from source.tools_manager import img_to_base64

dawia_logo = img_to_base64("./assets/img/dawia.png")

page_title = f'''
    <div style="display: flex; align-items: center;">
        <img src="data:image/png;base64,{dawia_logo}" width="80" style="margin-right: 10px;"/>
        <h1 style="margin: 0;">Dawia Assist</h1>
    </div>
    '''

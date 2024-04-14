# pip install tk
# pip install pywebview
# url https://www.ysense.com/?rb=151997709

import webview

url = 'https://www.ysense.com/?rb=151997709'

webview.create_window('Test', url=url)
webview.start()

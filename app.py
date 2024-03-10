import gradio as gr

def greet(name):
    return 'Work in progress, come back later 😴️'

iface = gr.Interface(fn=greet, inputs="text", outputs="text")
iface.launch()

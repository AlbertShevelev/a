import gradio as gr

# def greet(name, intensity):
#     return "Hello, " + name + "!" * int(intensity)

def greet(image):
    return "Hello world!"

demo = gr.Interface(
    fn=greet,
    inputs=["image"],
    outputs=["text"],
    api_name="predict"
)

demo.launch()
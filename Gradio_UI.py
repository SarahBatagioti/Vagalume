import gradio as gr

class GradioUI:
    def __init__(self, agent):
        self.agent = agent

    def launch(self):
        def resposta_gradio(mensagem):
            return self.agent.chat(mensagem)

        gr.Interface(
            fn=resposta_gradio,
            inputs=gr.Textbox(label="Digite sua mensagem"),
            outputs=gr.Textbox(label="Resposta do Vagalume"),
            title="Vagalume - Facilitador de Candidaturas"
        ).launch()

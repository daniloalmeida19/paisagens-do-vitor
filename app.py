from flask import Flask, request, render_template_string
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        mensagem = request.form["mensagem"]

        # Configuração do e-mail
        msg = EmailMessage()
        msg["Subject"] = "Novo contato do site"
        msg["From"] = "seuemail@gmail.com"
        msg["To"] = "destino@gmail.com"
        msg.set_content(f"Nome: {nome}\nEmail: {email}\nMensagem: {mensagem}")

        # Envio do e-mail (exemplo usando Gmail)
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login("seuemail@gmail.com", "sua_senha")
            smtp.send_message(msg)

        return "Mensagem enviada com sucesso!"

    # Exibe o formulário (pode usar render_template se quiser um arquivo HTML separado)
    return render_template_string("""
    <form method="post">
      <label>Nome:</label><br>
      <input type="text" name="nome"><br>
      <label>Email:</label><br>
      <input type="email" name="email"><br>
      <label>Mensagem:</label><br>
      <textarea name="mensagem"></textarea><br>
      <input type="submit" value="Enviar">
    </form>
    """)

if __name__ == "__main__":
    app.run(debug=True)    pip install flask
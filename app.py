from http.server import HTTPServer, BaseHTTPRequestHandler
import subprocess


def obter_hash_commit():
    try:
        resultado = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            capture_output=True,
            text=True,
            check=True
        )
        return resultado.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "Commit ainda não criado"


class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        hash_commit = obter_hash_commit()

        html = f"""
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <title>Hello World - Marcelo</title>
        </head>
        <body>
            <h1>Hello World!</h1>
            <p>Desenvolvido por Marcelo & CARINA</p>
            <p>Versão do código: {hash_commit}</p>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header(
            "Content-Type",
            "text/html; charset=utf-8"
        )
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))


server = HTTPServer(("127.0.0.1", 8000), HelloHandler)
print("Servidor iniciado em http://127.0.0.1:8000")
server.serve_forever()

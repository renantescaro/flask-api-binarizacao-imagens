from PIL import Image

class BinarizacaoSv:
    def __init__(self, linha, coluna, imagem_original, limiar):
        self._pillow_obj = Image.new("RGB", (coluna, linha))
        self._linha      = linha
        self._coluna     = coluna
        self._imagem     = imagem_original
        self._limiar     = limiar
        
        self.processar()


    def processar(self):
        # linha
        for i in range(self._linha):
            # coluna
            for j in range(self._coluna):
                rgb_imagem = self._imagem.convert('RGB')
                r, _, _ = rgb_imagem.getpixel((j, i))

                cor = 0
                if int(r) > int(self._limiar):
                    cor = 255

                self._pillow_obj.putpixel((j, i), (cor, cor, cor))
        self._pillow_obj.save('static/uploads/teste.png')
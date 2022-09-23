from phone_field import PhoneField
from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File

class categoria_habilitacao(models.Model):
    
    a = models.BooleanField(default= False, max_length = 1, verbose_name="Habilitação tipo A")
    b = models.BooleanField(default= False, max_length = 1, verbose_name="Habilitação tipo B")
    c = models.BooleanField(default= False, max_length = 1, verbose_name="Habilitação tipo C")
    d = models.BooleanField(default= False, max_length = 1, verbose_name="Habilitação tipo D")
    e = models.BooleanField(default= False, max_length = 1, verbose_name="Habilitação tipo E")
    f = models.BooleanField(default= False, max_length = 1, verbose_name="Habilitação tipo F")
    
    class Meta:
        verbose_name_plural = "Registro de inscrições"
    def __str__(self):
        return self.a

def compress(image):
    im = Image.open(image)
    #verifica se a imagem não ta no formato JPEG e converte caso seja necessário
    if im.mode != "RGB":
        im = im.convert("RGB")
    # cria o objeto BytesIO 
    im_io = BytesIO() 
    # salva imagem como um objeto BytesIO 
    im.save(im_io, 'JPEG', optimize=True, quality=20) 
    # cria o objeto image do django
    new_image = File(im_io, name=image.name)
    return new_image

class registerCandidate(models.Model):
      
    UF_CHOICES = (
        ('AC', 'Acre'),
        ('RO', 'Rondônia'),
        ('AM', 'Amazonas'),
        ('RR', 'Roraima'),
        ('AP', 'Amapá'),
        ('TO', 'Tocantins'),
        ('MA', 'Maranhão'),
        ('PI', 'Piauí'),
        ('CE', 'Ceará'),
        ('RN', 'Rio Grande do Norte'),
        ('PB', 'Paraíba'),
        ('PE', 'Pernambuco'),
        ('AL', 'Alagoas'),
        ('SE', 'Sergipe'),
        ('BA', 'Bahia'),
        ('MG', 'Minas Gerais'),
        ('ES', 'Espírito Santo'),
        ('RJ', 'Rio de Janeiro'),
        ('SP', 'São Paulo'),
        ('PR', 'Paraná'),
        ('SC', 'Santa Catarina	'),
        ('RS', 'Rio Grande do Sul (*)'),
        ('MS', 'Mato Grosso do Sul'),
        ('MT', 'Mato Grosso'),
        ('GO', 'Goiás'),
        ('DF', 'Distrito Federal'),
        
    )
    
    cargo= models.CharField(max_length = 255, verbose_name="Cargo de Interesse?")
    nome_completo = models.CharField(max_length = 255, verbose_name="Nome Completo")
    sexo = models.CharField(max_length = 255, null=True, verbose_name='Sexo')
    naturalidade = models.CharField(max_length = 255, null=True, verbose_name='Naturalidade')
    nacionalidade = models.CharField(max_length = 255, null=True, verbose_name='Nacionalidade')
    altura = models.FloatField(max_length = 4, verbose_name="Altura")
    peso = models.CharField(max_length = 50, verbose_name="Peso")
    data_aniversario = models.DateField(verbose_name="Data de Nascimento")
    idade = models.IntegerField(max_length = 3, verbose_name="Idade")
    celular = PhoneField(verbose_name='Celular')
    nome_pai = models.CharField(max_length = 255, null=True, verbose_name="Nome do pai")
    nome_mae = models.CharField(max_length = 255, verbose_name="Nome da mãe")
    endereco = models.CharField(max_length = 255, verbose_name="Endereço")
    bairro = models.CharField(max_length = 255, verbose_name="Bairro")
    cep = models.IntegerField(max_length = 8, verbose_name="Cep")
    necessidade_especial = models.BooleanField(default = False, verbose_name="Possui necessidades especiais?")
    necessidade_especial_descricao = models.TextField(null=True, max_length = 3000, verbose_name="Possui necessidades especiais?")
    
    habilitacao = models.BooleanField(verbose_name="Habilitação")
    categoria_habilitacao = models.CharField(max_length=255, null=True, verbose_name="Tipo de habilitação")
    reservista = models.BooleanField(default = True, verbose_name="Reservista?")
    cpf = models.CharField(max_length=11, unique=True, verbose_name="Cpf?")
    rg = models.CharField(max_length=30, unique=True, verbose_name="Rg?")
    orgao_expedidor = models.CharField(max_length=20, verbose_name="Orgão expedidor")
    uf = models.CharField(choices=UF_CHOICES, max_length=4, verbose_name="UF")
    escolaridade = models.CharField(max_length=255, verbose_name="Escolaridade")
    status_escolaridade = models.CharField(max_length=255, verbose_name="Status")
    data_conclusao_escolaridade = models.DateField(verbose_name="Ano de conclusao")
    instituicao = models.CharField(max_length=255, verbose_name="Instituição")
    estado_civil = models.CharField(max_length=255, verbose_name="Estado civil")
    estado_civil_conjulgue = models.CharField(null=True, max_length=255, verbose_name="Estado civil")
    filhos = models.BooleanField(verbose_name="Filhos?")
    filhos_quantidade = models.IntegerField(null=True, max_length=2, verbose_name="Quantidade de filhos")
    filhos_moram = models.BooleanField(null= True,verbose_name="Moram com você?")
    filhos_maior_idade = models.IntegerField(null= True,verbose_name="Quantos acima de 18?")
    instagram = models.CharField(max_length=255, verbose_name="Instagram")
    facebook = models.CharField(max_length=255, verbose_name="Facebook")
    linkedIn = models.CharField(null= True, max_length=255, verbose_name="LinkedIn")
    
    rendas = models.IntegerField(max_length=3, verbose_name="Quantas rendas além da sua?")
    conta_em_banco =  models.BooleanField(verbose_name="Possui conta em banco?")
    bancos = models.CharField(max_length=255, verbose_name="Quais bancos?")
    imovel = models.BooleanField(verbose_name="Possui imóvel?")
    residencia = models.CharField(max_length=255, verbose_name="Mora em residencia")
    transporte = models.BooleanField(verbose_name="Possui transporte?")
    transporte_descricao = models.CharField(null= True, max_length=255, verbose_name="Qual tipo de transporte?")
    parentes = models.BooleanField(verbose_name="Parentes na empresa?")
    parentes_descricao = models.CharField(null= True, max_length=255, verbose_name="Quem é o parente?")
    cursos = models.BooleanField(verbose_name="Possui cursos?")
    cursos_descricao = models.TextField(null= True, verbose_name="Informe os cursos")
    
    primeiro_emprego = models.BooleanField(verbose_name="Primeiro emprego?")
    curriculo = models.FileField(null= True, upload_to='curriculo/%Y%m%d', verbose_name="Curriculo")
    foto = models.ImageField(upload_to='foto/%Y%m%d', verbose_name="Foto")
    
    class Meta:
        verbose_name_plural = "Registro de inscrições"
    def __str__(self):
        return f'Inscrição de: {self.fullname}'

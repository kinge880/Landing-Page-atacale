from phone_field import PhoneField
from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File

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

class gerenciadeVagas(models.Model):
    GERENTE_LOJA = models.BooleanField(default=True, verbose_name="Gerente de loja")
    SUB_GERENTE = models.BooleanField(default=True, verbose_name="Sub gerente de loja")
    SUPERVISORA_E_COMERCE = models.BooleanField(default=True, verbose_name="Supervisora de E-comerce")
    SEPRADOR_DE_MERCADORIA = models.BooleanField(default=True, verbose_name="Separador de mercadorias")
    CARTAZISTA = models.BooleanField(default=True, verbose_name="Cartazista")
    TESOURARIA = models.BooleanField(default=True, verbose_name="Tesouraria")
    ENCARREGADA_DE_TELEVENDAS = models.BooleanField(default=True, verbose_name="Encarregado de televendas")
    TELEVENDAS = models.BooleanField(default=True, verbose_name="Televendas")
    ENCARREGADA_DE_CREDIARIO = models.BooleanField(default=True, verbose_name="Encarregado de crediário")
    CREDIARIO = models.BooleanField(default=True, verbose_name="Crediário")
    ATENDIMENTO_AO_CLIENTE = models.BooleanField(default=True, verbose_name="Atendimento ao cliente")
    ENCARREGADO_DE_FRENTE_DE_CAIXA = models.BooleanField(default=True, verbose_name="Encarregado de frente de caixa")
    FISCAL_DE_CAIXA = models.BooleanField(default=True, verbose_name="Fiscal de caixa")
    OPERADOR_DE_CAIXA = models.BooleanField(default=True, verbose_name="Operador de caixa")
    EMBALADOR = models.BooleanField(default=True, verbose_name="Embalador")
    ENCARREGADO_DE_PREVENÇAO = models.BooleanField(default=True, verbose_name="Encarregado de prevenção")
    PREVENÇAO = models.BooleanField(default=True, verbose_name="Prevenção")
    CFTV = models.BooleanField(default=True, verbose_name="Cftv")
    CFTV_NOTURNO = models.BooleanField(default=True, verbose_name="Cftv noturno")
    AUX_LIMPEZA = models.BooleanField(default=True, verbose_name="Aux de limpeza")
    ENCARREGADO_DE_HORTI_FRUTI = models.BooleanField(default=True, verbose_name="Encarregado de horti fruti")
    REPOSITOR_DE_HORTI_FRUTI = models.BooleanField(default=True, verbose_name="Repositor de horti fruti")
    ENCARREGADO_DE_FRIOS = models.BooleanField(default=True, verbose_name="Encarregado de frios")
    REPOSITOR_DE_FRIOS = models.BooleanField(default=True, verbose_name="Repositor de frios")
    ENCARREGADO_DE_ACOUGUE = models.BooleanField(default=True, verbose_name="Encarregado do açougue")
    AÇOUGUEIRO = models.BooleanField(default=True, verbose_name="Açougueiro")
    PEIXEIRO = models.BooleanField(default=True, verbose_name="Peixeiro")
    SUSHIMAN = models.BooleanField(default=True, verbose_name="Sushiman")
    ENCARREGADO_MERCEARIA = models.BooleanField(default=True, verbose_name="Encarregado de mercearia")
    REPOSITOR_DE_MERCEARIA = models.BooleanField(default=True, verbose_name="Repositor de mercearia")
    ATENDENTE_DE_ADEGA = models.BooleanField(default=True, verbose_name="Atendente de adega")
    ENCARREGADO_DA_PADARIA = models.BooleanField(default=True, verbose_name="Encarregado da padaria")
    PADARIA = models.BooleanField(default=True, verbose_name="Padaria")
    ENCARREGADO_DA_ROTISSERIA = models.BooleanField(default=True, verbose_name="Encarregado da rotisseria")
    ROTISSERIA = models.BooleanField(default=True, verbose_name="Rotisseria")
    COZINHEIRA = models.BooleanField(default=True, verbose_name="Cozinheira")
    AUX_DE_COZINHA = models.BooleanField(default=True, verbose_name="Aux de cozinha")
    ECARREGADO_DEPOSITO = models.BooleanField(default=True, verbose_name="Encarregado do deposito")
    RM = models.BooleanField(default=True, verbose_name="RM")
    AUXILIAR_DE_DEPOSITO = models.BooleanField(default=True, verbose_name="Aux de deposito")
    AUX_DE_DEPOSITO_TRANSFERENCIA = models.BooleanField(default=True, verbose_name="Aux de deposito - transferência")
    AVARIA = models.BooleanField(default=True, verbose_name="Avaria")
    CONFERENTE_DE_MERCDORIA = models.BooleanField(default=True, verbose_name="Conferente de mercadoria")
    CONFERENTE_DE_MERCADORIA_SAIDA = models.BooleanField(default=True, verbose_name="Conferente de mercadoria - saida")
    CONFERENTE_DE_MERCADORIA_ENTRADA = models.BooleanField(default=True, verbose_name="Conferente de mercadoria - entrada")
    EMPILHADEIRA_GRANDE = models.BooleanField(default=True, verbose_name="Empilhadeira grande")
    SUPERVISOR_DE_CD = models.BooleanField(default=True, verbose_name="Supervisor de CD")
    CONFERENTE = models.BooleanField(default=True, verbose_name="Conferente")
    AUX_DE_DEPOSITO = models.BooleanField(default=True, verbose_name="Aux de deposito")
    CONTROLADOR_DE_ESTOQUE = models.BooleanField(default=True, verbose_name="Controlador de estoque")
    OPERADOR_DE_EMPILHADEIRA = models.BooleanField(default=True, verbose_name="Operador de empilhadeira")
    FISCAL_DE_PREVENÇÃO = models.BooleanField(default=True, verbose_name="Fiscal de prevenção")
    MOTORISTA = models.BooleanField(default=True, verbose_name="Motorista")
    
    class Meta:
        verbose_name_plural = "Vagas abertas"
    def __str__(self):
        
        return 'Controle de vagas'
    
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
    altura = models.CharField(max_length = 4, verbose_name="Altura")
    peso = models.CharField(max_length = 10, verbose_name="Peso")
    data_aniversario = models.DateField(verbose_name="Data de Nascimento")
    idade = models.IntegerField(verbose_name="Idade")
    celular = PhoneField(verbose_name='Celular')
    nome_pai = models.CharField(max_length = 255, null=True, verbose_name="Nome do pai")
    nome_mae = models.CharField(max_length = 255, verbose_name="Nome da mãe")
    endereco = models.CharField(max_length = 255, verbose_name="Endereço")
    bairro = models.CharField(max_length = 255, verbose_name="Bairro")
    cep = models.CharField(max_length = 10, verbose_name="Cep")
    necessidade_especial = models.BooleanField(verbose_name="Possui necessidades especiais?")
    necessidade_especial_descricao = models.TextField(null=True, blank=True, max_length = 3000, verbose_name="Possui necessidades especiais?")
    
    habilitacao = models.BooleanField(verbose_name="Habilitação")
    categoria_habilitacao = models.TextField(null=True, verbose_name="Tipo de habilitação")
    reservista = models.BooleanField(default = True, verbose_name="Reservista?")
    cpf = models.CharField(max_length=14, verbose_name="Cpf?")
    rg = models.CharField(max_length=30, verbose_name="Rg?")
    orgao_expedidor = models.CharField(max_length=50, verbose_name="Orgão expedidor")
    uf = models.CharField(choices=UF_CHOICES, max_length=4, verbose_name="UF")
    escolaridade = models.CharField(max_length=255, verbose_name="Escolaridade")
    status_escolaridade = models.CharField(max_length=255, verbose_name="Status")
    data_conclusao_escolaridade = models.DateField(verbose_name="Ano de conclusao")
    instituicao = models.CharField(max_length=255, verbose_name="Instituição")
    estado_civil = models.CharField(max_length=255, verbose_name="Estado civil")
    estado_civil_conjulgue = models.CharField(null=True, max_length=255, verbose_name="Estado civil")
    filhos = models.BooleanField(verbose_name="Filhos?")
    filhos_quantidade = models.IntegerField(null=True, verbose_name="Quantidade de filhos")
    filhos_moram = models.BooleanField(null= True,verbose_name="Moram com você?")
    filhos_maior_idade = models.IntegerField(null= True, default=0, verbose_name="Quantos acima de 18?")
    instagram = models.CharField(null= True, max_length=255, verbose_name="Instagram")
    facebook = models.CharField(null= True, max_length=255, verbose_name="Facebook")
    linkedIn = models.CharField(null= True, max_length=255, verbose_name="LinkedIn")
    
    rendas = models.IntegerField(verbose_name="Quantas rendas além da sua?")
    conta_em_banco =  models.BooleanField(verbose_name="Possui conta em banco?")
    bancos = models.CharField(null= True, max_length=255, verbose_name="Quais bancos?")
    imovel = models.BooleanField(verbose_name="Possui imóvel?")
    residencia = models.CharField(max_length=255, verbose_name="Mora em residencia")
    transporte = models.BooleanField(verbose_name="Possui transporte?")
    transporte_descricao = models.CharField(null= True, max_length=255, verbose_name="Qual tipo de transporte?")
    parentes = models.BooleanField(verbose_name="Parentes na empresa?")
    parentes_descricao = models.CharField(null= True, max_length=255, verbose_name="Quem é o parente?")
    cursos = models.BooleanField(verbose_name="Possui cursos?")
    cursos_descricao = models.TextField(null= True, verbose_name="Informe os cursos")
    
    primeiro_emprego = models.BooleanField(verbose_name="Primeiro emprego?")
    nome_ultima_empresa = models.CharField(null= True, max_length=255, verbose_name="Ultima empresa")
    responsavel_ultima_empresa = models.CharField(null= True, max_length=255, verbose_name="Responsável")
    endereco_ultima_empresa = models.CharField(null= True, max_length=255, verbose_name="Endereço da última empresa")
    telefone_ultima_empresa = models.CharField(null= True, max_length=255, verbose_name="Telefone da última empresa")
    cargo_ultima_empresa = models.CharField(null= True, max_length=255, verbose_name="Cargo da última empresa")
    ultimo_salario_ultima_empresa = models.IntegerField(null= True, blank= True, verbose_name="Ultimo Salário")
    ctps_assinada_ultima_empresa = models.BooleanField(null= True, verbose_name="CTPS assinada")
    motivo_saida_ultima_empresa = models.TextField(null= True, verbose_name="Motivo da saida")
    data_admisao_ultima_empresa = models.DateField(null= True, blank= True, verbose_name="Data de Admissão")
    emprego_atual_ultima_empresa = models.BooleanField(null= True, verbose_name="Emprego atual")
    data_demissao_ultima_empresa = models.DateField(null= True, blank= True, verbose_name="Data de demissão")
    atividade_ultima_empresa = models.TextField(null=True, max_length = 3000, verbose_name="Principais atividades na empresa")
    pis = models.CharField(null = True, max_length = 50, verbose_name="Principais atividades na empresa")
    outro_emprego = models.BooleanField(null= True, verbose_name="Outro emprego?")
    
    nome_penultima_empresa = models.CharField(null= True, max_length=255, verbose_name="Penúltima empresa")
    responsavel_penultima_empresa = models.CharField(null= True, max_length=255, verbose_name="Responsável Penúltima empresa")
    endereco_penultima_empresa = models.CharField(null= True, max_length=255, verbose_name="Endereço da Penúltima empresa")
    telefone_penultima_empresa = models.CharField(null= True, max_length=255, verbose_name="Telefone da Penúltima empresa")
    cargo_penultima_empresa = models.CharField(null= True, max_length=255, verbose_name="Cargo da Penúltima empresa")
    ultimo_salario_penultima_empresa = models.IntegerField(null= True, blank= True, verbose_name="Ultimo Salário Penúltima empresa")
    ctps_assinada_penultima_empresa = models.BooleanField(null= True, verbose_name="CTPS assinada Penúltima empresa")
    motivo_saida_penultima_empresa = models.TextField(null= True, verbose_name="Motivo da saida Penúltima empresa")
    data_admisao_penultima_empresa = models.DateField(null= True, blank= True, verbose_name="Data de Admissão Penúltima empresa")
    data_demissao_penultima_empresa = models.DateField(null= True, verbose_name="Data de demissão Penúltima empresa")
    atividade_penultima_empresa = models.TextField(null=True, max_length = 3000, verbose_name="Principais atividades na penúltima empresa ")
    
    empresa_destaque = models.CharField(null= True, max_length=255, verbose_name="Empresa destaque?")    
    curriculo = models.FileField(null= True, upload_to='curriculo/%Y%m%d', verbose_name="Curriculo")
    foto = models.ImageField(upload_to='foto/%Y%m%d', verbose_name="Foto")
    date = models.DateField(null= True, verbose_name="Data da inscrição")
    
    def save(self, *args, **kwargs):
        # chama a função de comp ressão
        new_image = compress(self.foto)
        # seta self.image com a nova imagem
        self.foto = new_image
        # salva
        super().save(*args, **kwargs)
        
    class Meta:
        verbose_name_plural = "Registro de inscrições"
    def __str__(self):
        
        return self.cargo


class registerEmails(models.Model):
    to = models.CharField(max_length = 255, verbose_name="Destino")
    subject = models.CharField(max_length = 255, verbose_name="Título")
    emailId = models.IntegerField( verbose_name="idcandidato")
    body = models.TextField( verbose_name="corpoemail")
    
    class Meta:
        verbose_name_plural = "Registro de emails"
    def __str__(self):
        
        return self.subject
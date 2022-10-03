from django.shortcuts import render, redirect
from landpage.models import registerCandidate
from django.db.models.signals import post_save
from django.core.mail import send_mail, BadHeaderError, EmailMultiAlternatives
from django.http import HttpResponse
import os
from django.conf import settings
from django.template.defaultfilters import filesizeformat
from django.template import loader
from django.utils import timezone

def success(request):
    
    return render(request, 'landpage/sucesso.html')

def falha(request):
    
    return render(request, 'landpage/falha.html')

def land(request):
    
    if(request.method == "POST"):
        cargoInput = request.POST['cargo']
        nome_completoInput = request.POST['nome_completo']
        sexoInput = request.POST['sexo']
        naturalidadeInput = request.POST['naturalidade']
        nacionalidadeInput = request.POST['nacionalidade']
        alturaInput = request.POST['altura']
        pesoInput = request.POST['peso']
        data_aniversarioInput = request.POST['data_aniversario']
        idadeInput = request.POST['idade']
        celularInput = request.POST['celular']
        nome_paiInput = request.POST['nome_pai']
        nome_maeInput = request.POST['nome_mae']
        enderecoInput = request.POST['endereco']
        bairroInput = request.POST['bairro']
        cepInput = request.POST['cep']
        necessidade_especialInput = request.POST['necessidade_especial']
        necessidade_especial_descricaoInput = request.POST['necessidade_especial_descricao']
        
        habilitacaoInput = request.POST['habilitacao']
        categoria_habilitacaoInput = request.POST.getlist('categoria_habilitacao', '')
            
        reservistaInput = request.POST.get('reservista', False)
        cpfInput = request.POST['cpf']
        rgInput = request.POST['rg']
        orgao_expedidorInput = request.POST['orgao_expedidor']
        ufInput = request.POST['uf']
        pisInput = request.POST['pis']
        escolaridadeInput = request.POST['escolaridade']
        status_escolaridadeInput = request.POST['status_escolaridade']
        data_conclusao_escolaridadeInput = request.POST['data_conclusao_escolaridade']
        instituicaoInput = request.POST['instituicao']
        estado_civilInput = request.POST['estado_civil']
        estado_civil_conjulgueInput = request.POST['estado_civil_conjulgue']
        filhosInput = request.POST['filhos']
        
        if request.POST['filhos_quantidade'] == '':
            filhos_quantidadeInput = None
        else:     
            filhos_quantidadeInput = request.POST['filhos_quantidade']
       
        if request.POST.get('filhos_moram', '') == '':
            filhos_moramInput = None
        else:     
            filhos_moramInput = request.POST.get('filhos_moram', '')
        
        if request.POST['filhos_maior_idade'] == '':
            filhos_maior_idadeInput = None
        else:     
            filhos_maior_idadeInput = request.POST['filhos_maior_idade']
        
        instagramInput = request.POST['instagram']
        facebookInput = request.POST['facebook']
        linkedInInput = request.POST['linkedIn']
        
        if request.POST['rendas'] == '':
            rendasInInput = None
        else:     
            rendasInInput = request.POST['rendas']
        conta_em_bancoInInput = request.POST['conta_em_banco']
        bancosInInput = request.POST['bancos']
        imovelInput = request.POST['imovel']
        residenciaInput = request.POST['residencia']
        transporteInput = request.POST['transporte']
        transporte_descricaoInput = request.POST.getlist('transporte_descricao', '')
        parentesInput = request.POST['parentes']
        parentes_descricaoInput = request.POST['parentes_descricao']
        cursosInput = request.POST['cursos']
        cursos_descricaoInput = request.POST['cursos_descricao']
        
        primeiro_empregoInput = request.POST['primeiro_emprego']
        nome_ultima_empresaInput = request.POST['nome_ultima_empresa']
        responsavel_ultima_empresaInput = request.POST['responsavel_ultima_empresa']
        endereco_ultima_empresaInput = request.POST['endereco_ultima_empresa']
        telefone_ultima_empresaInput = request.POST['telefone_ultima_empresa']
        cargo_ultima_empresaInput = request.POST['cargo_ultima_empresa']    
            
        if request.POST['ultimo_salario_ultima_empresa'] == '':
            ultimo_salario_ultima_empresaInput = None
        else:
            ultimo_salario_ultima_empresaInput = request.POST['ultimo_salario_ultima_empresa']
        ctps_assinada_ultima_empresaInput = request.POST['ctps_assinada_ultima_empresa']
        motivo_saida_ultima_empresaInput = request.POST['motivo_saida_ultima_empresa']
        
        if request.POST['data_admisao_ultima_empresa'] == '':
            data_admisao_ultima_empresaInput = None
        else:
            data_admisao_ultima_empresaInput = request.POST['data_admisao_ultima_empresa']
            
        emprego_atual_ultima_empresaInput = request.POST['emprego_atual_ultima_empresa']
        
        if request.POST['data_demissao_ultima_empresa'] == '':
            data_demissao_ultima_empresaInput = None
        else:
            data_demissao_ultima_empresaInput = request.POST['data_demissao_ultima_empresa']
            
        atividade_ultima_empresaInput = request.POST['atividade_ultima_empresa']
        outro_empregoInput = request.POST['outro_emprego']
        nome_penultima_empresaInput = request.POST['nome_penultima_empresa']
        responsavel_penultima_empresaInput = request.POST['responsavel_penultima_empresa']
        endereco_penultima_empresaInput = request.POST['endereco_penultima_empresa']
        telefone_penultima_empresaInput = request.POST['telefone_penultima_empresa']
        cargo_penultima_empresaInput = request.POST['cargo_penultima_empresa']
        if request.POST['ultimo_salario_penultima_empresa'] == '':
            ultimo_salario_penultima_empresaInput = None
        else:
            ultimo_salario_penultima_empresaInput = request.POST['ultimo_salario_penultima_empresa']
        ctps_assinada_penultima_empresaInput = request.POST['ctps_assinada_penultima_empresa']
        motivo_saida_penultima_empresaInput = request.POST['motivo_saida_penultima_empresa']
        
        if request.POST['data_admisao_penultima_empresa'] == '':
            data_admisao_penultima_empresaInput = None
        else:
            data_admisao_penultima_empresaInput = request.POST['data_admisao_penultima_empresa']
        
        if request.POST['data_demissao_penultima_empresa'] == '':
            data_demissao_penultima_empresaInput = None
        else:
            data_demissao_penultima_empresaInput = request.POST['data_demissao_penultima_empresa']
            
        atividade_penultima_empresaInput = request.POST['atividade_penultima_empresa']
        empresa_destaqueInput = request.POST['empresa_destaque']
        
        curriculoInput = request.FILES.get('curriculo', '')
        fotoInput = request.FILES.get('foto', '')
        now = timezone.localtime(timezone.now())
        
        
        teste_size = True

        if curriculoInput:
            curriculocontent_type = curriculoInput.content_type.split('/')[0]
            if curriculocontent_type in 'application/pdf':
                if curriculoInput.size > settings.MAX_UPLOAD_PDF_SIZE:
                    context = {"cirruculo_erro": ('O tamanho máximo do curriculo deve ser %s, mas o tamanho atual é %s. Clique em voltar e envie um curriculo menor') % (filesizeformat(settings.MAX_UPLOAD_PDF_SIZE), filesizeformat(curriculoInput.size))}
                    teste_size = False
            else:
                context = {"foto_cirruculo_erroerro": 'Somente arquivos no formato PDF são aceitos. Clique em voltar e envie uma foto no formato correto'}
                teste_size = False
        
        if fotoInput:
            fotocontent_type = fotoInput.content_type.split('/')[0]
            if fotocontent_type in 'image/png' or fotocontent_type in 'image/jpg' :
                if fotoInput.size > settings.MAX_UPLOAD_IMAGE_SIZE:
                    context = {"foto_erro": ('Tamanho máximo da foto deve ser %s, mas o tamanho atual é %s. Clique em voltar e envie uma foto no formato correto') % (filesizeformat(settings.MAX_UPLOAD_IMAGE_SIZE).replace(u'\xa0', u' '), filesizeformat(curriculoInput.size).replace(u'\xa0', u' '))}
                    teste_size = False
            else:
                context = {"foto_erro": 'Somente imagens no formato PNG ou JPG são aceitas. Clique em voltar e envie uma foto no formato correto'}
                teste_size = False
            
        if teste_size:
            candidate = registerCandidate.objects.create(cargo = cargoInput,
                                                nome_completo = nome_completoInput,
                                                sexo = sexoInput,
                                                naturalidade = naturalidadeInput,
                                                nacionalidade = nacionalidadeInput,
                                                altura = alturaInput,
                                                peso = pesoInput,
                                                data_aniversario = data_aniversarioInput,
                                                idade = idadeInput,
                                                celular = celularInput,
                                                nome_pai = nome_paiInput,
                                                nome_mae = nome_maeInput,
                                                endereco = enderecoInput,
                                                bairro = bairroInput,
                                                cep = cepInput,
                                                necessidade_especial = necessidade_especialInput,
                                                necessidade_especial_descricao = necessidade_especial_descricaoInput,
                                                habilitacao = habilitacaoInput,
                                                categoria_habilitacao = categoria_habilitacaoInput,
                                                reservista = reservistaInput,
                                                cpf = cpfInput,
                                                rg = rgInput,
                                                orgao_expedidor = orgao_expedidorInput,
                                                uf = ufInput,
                                                pis = pisInput,
                                                escolaridade = escolaridadeInput,
                                                status_escolaridade = status_escolaridadeInput,
                                                data_conclusao_escolaridade = data_conclusao_escolaridadeInput,
                                                instituicao = instituicaoInput,
                                                estado_civil = estado_civilInput,
                                                estado_civil_conjulgue = estado_civil_conjulgueInput,
                                                filhos = filhosInput,
                                                filhos_quantidade = filhos_quantidadeInput,
                                                filhos_moram = filhos_moramInput,
                                                filhos_maior_idade = filhos_maior_idadeInput,
                                                instagram = instagramInput,
                                                facebook = facebookInput,
                                                linkedIn = linkedInInput,
                                                rendas = rendasInInput,
                                                conta_em_banco = conta_em_bancoInInput,
                                                bancos = bancosInInput,
                                                imovel = imovelInput,
                                                residencia = residenciaInput,
                                                transporte = transporteInput,
                                                transporte_descricao = transporte_descricaoInput,
                                                parentes = parentesInput,
                                                parentes_descricao = parentes_descricaoInput,
                                                cursos = cursosInput,
                                                cursos_descricao = cursos_descricaoInput,
                                                primeiro_emprego = primeiro_empregoInput,
                                                nome_ultima_empresa = nome_ultima_empresaInput,
                                                responsavel_ultima_empresa = responsavel_ultima_empresaInput,
                                                endereco_ultima_empresa = endereco_ultima_empresaInput,
                                                telefone_ultima_empresa = telefone_ultima_empresaInput,
                                                cargo_ultima_empresa = cargo_ultima_empresaInput,
                                                ultimo_salario_ultima_empresa = ultimo_salario_ultima_empresaInput,
                                                ctps_assinada_ultima_empresa = ctps_assinada_ultima_empresaInput,
                                                motivo_saida_ultima_empresa = motivo_saida_ultima_empresaInput,
                                                data_admisao_ultima_empresa = data_admisao_ultima_empresaInput,
                                                emprego_atual_ultima_empresa = emprego_atual_ultima_empresaInput,
                                                data_demissao_ultima_empresa = data_demissao_ultima_empresaInput,
                                                atividade_ultima_empresa = atividade_ultima_empresaInput,
                                                outro_emprego = outro_empregoInput,
                                                nome_penultima_empresa = nome_penultima_empresaInput,
                                                responsavel_penultima_empresa = responsavel_penultima_empresaInput,
                                                endereco_penultima_empresa = endereco_penultima_empresaInput,
                                                telefone_penultima_empresa = telefone_penultima_empresaInput,
                                                cargo_penultima_empresa = cargo_penultima_empresaInput,
                                                ultimo_salario_penultima_empresa = ultimo_salario_penultima_empresaInput,
                                                ctps_assinada_penultima_empresa = ctps_assinada_penultima_empresaInput,
                                                motivo_saida_penultima_empresa = motivo_saida_penultima_empresaInput,
                                                data_admisao_penultima_empresa = data_admisao_penultima_empresaInput,
                                                data_demissao_penultima_empresa = data_demissao_penultima_empresaInput,
                                                atividade_penultima_empresa = atividade_penultima_empresaInput,
                                                empresa_destaque = empresa_destaqueInput,
                                                
                                                curriculo = curriculoInput,
                                                foto = fotoInput,
                                                date = now.date())
            #candidate.save()
            context = {"nome": nome_completoInput}
            return render(request, '/sucesso', context)
        else:
            return render(request, 'landpage/falha.html', context)
    
    return render(request, 'landpage/index.html',{})

def my_callback(sender, **kwargs):
    
    c = {
    "cargo": kwargs.get('instance').cargo,
    'nome_completo': kwargs.get('instance').nome_completo,
    'idade': kwargs.get('instance').idade,
    'altura': kwargs.get('instance').altura,
    'peso': kwargs.get('instance').peso,
    'sexo': kwargs.get('instance').sexo,
    'naturalidade': kwargs.get('instance').naturalidade,
    'uf': kwargs.get('instance').uf,
    'endereco': kwargs.get('instance').endereco,
    'bairro': kwargs.get('instance').bairro,
    'cep': kwargs.get('instance').cep,
    'celular': kwargs.get('instance').celular,
    'nome_pai': kwargs.get('instance').nome_pai,
    'nome_mae': kwargs.get('instance').nome_mae,
    'endereco': kwargs.get('instance').endereco,
    'bairro': kwargs.get('instance').bairro,
    'cep': kwargs.get('instance').cep,
    'necessidade_especial': kwargs.get('instance').necessidade_especial,
    'necessidade_especial_descricao': kwargs.get('instance').necessidade_especial_descricao,
    'habilitacao': kwargs.get('instance').habilitacao,
    'categoria_habilitacao': kwargs.get('instance').categoria_habilitacao,
    'reservista': kwargs.get('instance').reservista,
    'rg': kwargs.get('instance').rg,
    'orgao_expedidor': kwargs.get('instance').orgao_expedidor,
    'uf': kwargs.get('instance').uf,
    'pis': kwargs.get('instance').pis,
    'escolaridade': kwargs.get('instance').escolaridade,
    'status_escolaridade': kwargs.get('instance').status_escolaridade,
    'data_conclusao_escolaridade': kwargs.get('instance').data_conclusao_escolaridade,
    'instituicao': kwargs.get('instance').instituicao,
    'estado_civil': kwargs.get('instance').estado_civil,
    'estado_civil_conjulgue': kwargs.get('instance').estado_civil_conjulgue,
    'filhos': kwargs.get('instance').filhos,
    'filhos_quantidade': kwargs.get('instance').filhos_quantidade,
    'filhos_moram': kwargs.get('instance').filhos_moram,
    'filhos_maior_idade': kwargs.get('instance').filhos_maior_idade,
    'instagram': kwargs.get('instance').instagram,
    'facebook': kwargs.get('instance').facebook,
    'linkedIn': kwargs.get('instance').linkedIn,
    'rendas': kwargs.get('instance').rendas,
    'conta_em_banco': kwargs.get('instance').conta_em_banco,
    'bancos': kwargs.get('instance').bancos,
    'imovel': kwargs.get('instance').imovel,
    'residencia': kwargs.get('instance').residencia,
    'transporte': kwargs.get('instance').transporte,
    'transporte_descricao': kwargs.get('instance').transporte_descricao,
    'parentes': kwargs.get('instance').parentes,
    'parentes_descricao': kwargs.get('instance').parentes_descricao,
    'cursos': kwargs.get('instance').cursos,
    'cursos_descricao': kwargs.get('instance').cursos_descricao,
    'primeiro_emprego': kwargs.get('instance').primeiro_emprego,
    'nome_ultima_empresa': kwargs.get('instance').nome_ultima_empresa,
    'responsavel_ultima_empresa': kwargs.get('instance').responsavel_ultima_empresa,
    'endereco_ultima_empresa': kwargs.get('instance').endereco_ultima_empresa,
    'telefone_ultima_empresa': kwargs.get('instance').telefone_ultima_empresa,
    'cargo_ultima_empresa': kwargs.get('instance').cargo_ultima_empresa,
    'ultimo_salario_ultima_empresa': kwargs.get('instance').ultimo_salario_ultima_empresa,
    'ctps_assinada_ultima_empresa': kwargs.get('instance').ctps_assinada_ultima_empresa,
    'motivo_saida_ultima_empresa': kwargs.get('instance').motivo_saida_ultima_empresa,
    'data_admisao_ultima_empresa': kwargs.get('instance').data_admisao_ultima_empresa,
    'emprego_atual_ultima_empresa': kwargs.get('instance').emprego_atual_ultima_empresa,
    'data_demissao_ultima_empresa': kwargs.get('instance').data_demissao_ultima_empresa,
    'atividade_ultima_empresa': kwargs.get('instance').atividade_ultima_empresa,
    'outro_emprego': kwargs.get('instance').outro_emprego,
    'nome_penultima_empresa': kwargs.get('instance').nome_penultima_empresa,
    'responsavel_penultima_empresa': kwargs.get('instance').responsavel_penultima_empresa,
    'endereco_penultima_empresa': kwargs.get('instance').endereco_penultima_empresa,
    'telefone_penultima_empresa': kwargs.get('instance').telefone_penultima_empresa,
    'cargo_penultima_empresa': kwargs.get('instance').cargo_penultima_empresa,
    'ultimo_salario_penultima_empresa': kwargs.get('instance').ultimo_salario_penultima_empresa,
    'ctps_assinada_penultima_empresa': kwargs.get('instance').ctps_assinada_penultima_empresa,
    'motivo_saida_penultima_empresa': kwargs.get('instance').motivo_saida_penultima_empresa,
    'data_admisao_penultima_empresa': kwargs.get('instance').data_admisao_penultima_empresa,
    'data_demissao_penultima_empresa': kwargs.get('instance').data_demissao_penultima_empresa,
    'atividade_penultima_empresa': kwargs.get('instance').atividade_penultima_empresa,
    'empresa_destaque': kwargs.get('instance').empresa_destaque,
    'curriculo': kwargs.get('instance').curriculo,
    'foto': kwargs.get('instance').foto,
    }
    email_template_name = "landpage/emailtemplate.html"
    subject = kwargs.get('instance').cargo
    email = loader.render_to_string(email_template_name, c)
    message = 'text version of HTML message'
    
    try:
        mail = EmailMultiAlternatives(subject, message, 'mercaleemails@gmail.com',
        ['mercaleemails@gmail.com', 'vagas@atacale.com.br'])
        mail.attach_alternative(email, "text/html")
        if kwargs.get('instance').curriculo:
            mail.attach(os.path.basename(kwargs.get('instance').curriculo.name), kwargs.get('instance').curriculo.read())
        mail.attach(os.path.basename(kwargs.get('instance').foto.name), kwargs.get('instance').foto.read())
        mail.send()
        
    except BadHeaderError as e:
        return HttpResponse('Invalid header found.')
    
    if kwargs.get('instance').curriculo:
        kwargs.get('instance').curriculo.delete(save=False)
    if kwargs.get('instance').foto:
        kwargs.get('instance').foto.delete(save=False)
    
post_save.connect(my_callback, registerCandidate, dispatch_uid="landpage")


def privacidade(request):
    
    return render(request, 'privacidade/privacidade.html',{})
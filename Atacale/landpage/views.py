from django.shortcuts import render, redirect
from landpage.models import registerCandidate

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
        categoria_habilitacaoInput = request.POST['categoria_habilitacao']
        reservistaInput = request.POST['reservista']
        cpfInput = request.POST['cpf']
        rgInput = request.POST['rg']
        orgao_expedidorInput = request.POST['orgao_expedidor']
        ufInput = request.POST['uf']
        escolaridadeInput = request.POST['escolaridade']
        status_escolaridadeInput = request.POST['status_escolaridade']
        data_conclusao_escolaridadeInput = request.POST['data_conclusao_escolaridade']
        instituicaoInput = request.POST['instituicao']
        estado_civilInput = request.POST['estado_civil']
        estado_civil_conjulgueInput = request.POST['estado_civil_conjulgue']
        filhosInput = request.POST['filhos']
        filhos_quantidadeInput = request.POST['filhos_quantidade']
        filhos_moramInput = request.POST['filhos_moram']
        filhos_maior_idadeInput = request.POST['filhos_maior_idade']
        instagramInput = request.POST['instagram']
        facebookInput = request.POST['facebook']
        linkedInInput = request.POST['linkedIn']
        
        rendasInInput = request.POST['rendas']
        conta_em_bancoInInput = request.POST['conta_em_banco']
        bancosInInput = request.POST['bancos']
        imovelInput = request.POST['imovel']
        residenciaInput = request.POST['residencia']
        transporteInput = request.POST['transporte']
        transporte_descricaoInput = request.POST['transporte_descricao']
        parentesInput = request.POST['parentes']
        parentes_descricaoInput = request.POST['parentes_descricao']
        cursosInput = request.POST['cursos']
        cursos_descricaoInput = request.POST['cursos_descricao']
        
        primeiro_empregoInput = request.POST['primeiro_emprego']
        curriculoInput = request.POST['curriculo']
        fotoInput = request.POST['foto']
         

        candidate = registerCandidate.objects.create(cargo = cargoInput,
                                            nome_completo = nome_completoInput,
                                            sexoInput = sexoInput,
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
                                            curriculo = curriculoInput,
                                            foto = fotoInput,)
        candidate.save()
        return redirect('/accounts/login')
    
    return render(request, 'landpage/index.html',{})


"""
Gerador de Currículo em formato ABNT.

Este módulo permite a criação automática de currículos profissionais
formatados seguindo as normas ABNT para documentos acadêmicos e profissionais.
Utiliza a biblioteca FPDF para geração do PDF.

Exemplo de uso:
    >>> python curriculo_abnt.py
    PDF gerado com sucesso: curriculo_petshop_exemplo.pdf
"""

from fpdf import FPDF


class PDF(FPDF):
    """
    Classe personalizada que estende FPDF para adicionar funcionalidades específicas.
    
    Esta classe adiciona um rodapé personalizado com numeração de páginas
    e mantém todas as funcionalidades originais da classe FPDF.
    
    Attributes:
        Herda todos os atributos da classe FPDF.
    """
    
    def footer(self):
        """
        Adiciona rodapé personalizado com numeração de páginas.
        
        O rodapé é posicionado a 15mm da borda inferior e centralizado,
        mostrando o número da página atual no formato 'Página X'.
        
        Returns:
            None
        """
        # Rodapé com numeração de página
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')


def create_resume():
    """
    Cria e formata um currículo profissional no padrão ABNT.
    
    Esta função configura o documento PDF, adiciona todas as seções
    do currículo (dados pessoais, formação, experiência, etc.) e
    salva o arquivo final.
    
    As margens seguem o padrão ABNT:
    - Margem superior: 3cm
    - Margem esquerda: 3cm  
    - Margem direita: 2cm
    - Margem inferior: 2cm
    
    Returns:
        None. O PDF é salvo como 'curriculo_petshop_exemplo.pdf'.
        
    Raises:
        IOError: Se houver problema ao salvar o arquivo PDF.
    """
    # Configuração Inicial (A4, mm)
    pdf = PDF(orientation='P', unit='mm', format='A4')
    
    # Margens ABNT: 3cm sup/esq, 2cm inf/dir
    pdf.set_margins(left=30, top=30, right=20)
    pdf.set_auto_page_break(auto=True, margin=20)
    
    pdf.add_page()
    
    # --- DADOS PESSOAIS ---
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'ANA LUIZA COSTA SANTOS', ln=True, align='C')
    
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 6, 'Veterinária | Gerência de Petshop | Atendimento ao Cliente | Gestão de Estoque', ln=True, align='C')
    pdf.ln(2)
    
    # Contatos
    pdf.set_font('Arial', '', 10)
    contato_texto = 'Curitiba, PR | (99) 99999-99999 | ana.costa.petshop@email.com'
    pdf.cell(0, 6, contato_texto.encode('latin-1', 'replace').decode('latin-1'), ln=True, align='C')
    
    linkedin = 'www.linkedin.com/in/ana-costa-petshop'
    pdf.cell(0, 6, linkedin.encode('latin-1', 'replace').decode('latin-1'), ln=True, align='C')
    
    pdf.ln(5)
    pdf.line(30, pdf.get_y(), 190, pdf.get_y())
    pdf.ln(5)

    # --- FUNÇÃO AUXILIAR PARA TÍTULOS ---
    def section_title(label):
        """
        Cria um título de seção formatado.
        
        Args:
            label (str): Texto do título que será convertido para maiúsculas.
            
        Returns:
            None. Adiciona o título ao documento PDF.
        """
        pdf.set_font('Arial', 'B', 12)
        pdf.set_fill_color(240, 240, 240) 
        pdf.cell(0, 8, label.upper().encode('latin-1', 'replace').decode('latin-1'), ln=True, fill=False)
        pdf.ln(2)

    # --- RESUMO PROFISSIONAL ---
    section_title('Resumo Profissional')
    pdf.set_font('Arial', '', 11)
    
    resumo = (
        "Profissional da área veterinária com mais de 5 anos de experiência em gestão de petshops, "
        "atenção clínica a animais de pequeno porte e atendimento especializado ao cliente. "
        "Especialista em cuidados com animais exóticos, nutrição animal e comportamento pet. "
        "Experiência sólida em gestão de equipes, controle de estoque de produtos veterinários "
        "e implementação de sistemas de agendamento digital. Comprometida com o bem-estar animal "
        "e a excelência no atendimento, buscando sempre atualizar conhecimentos na área."
    )
              
    pdf.multi_cell(0, 6, resumo.encode('latin-1', 'replace').decode('latin-1'), align='J')
    pdf.ln(5)

    # --- FORMAÇÃO ACADÊMICA ---
    section_title('Formação Acadêmica')
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 6, 'Bacharelado em Medicina Veterinária', ln=True)
    pdf.set_font('Arial', '', 11)
    pdf.cell(0, 6, 'Universidade Federal do Paraná (UFPR) | 2016 - 2021', ln=True)
    pdf.ln(3)
    
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 6, 'Pós-Graduação em Gestão de Negócios Pet', ln=True)
    pdf.set_font('Arial', '', 11)
    pdf.cell(0, 6, 'Instituto de Ensino Veterinário | 2022 - 2023', ln=True)
    pdf.ln(5)

    # --- EXPERIÊNCIA PROFISSIONAL ---
    section_title('Experiência Profissional')

    # Exp 1 - PetShop Premium
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 6, 'PetShop Premium Curitiba', ln=True)
    pdf.set_font('Arial', 'I', 10)
    pdf.cell(0, 6, 'Gerente Veterinária | Março 2022 - Atualmente', ln=True)
    pdf.set_font('Arial', '', 10)
    desc_petshop = (
        "- Gestão completa do petshop incluindo equipe de 8 funcionários\n"
        "- Atendimento clínico a cães, gatos e animais exóticos\n"
        "- Controle de estoque e compras de produtos veterinários\n"
        "- Implementação de sistema digital de agendamento\n"
        "- Organização de eventos comunitários sobre posse responsável\n"
        "- Treinamento de novos funcionários em técnicas de manejo animal"
    )
    pdf.multi_cell(0, 6, desc_petshop.encode('latin-1', 'replace').decode('latin-1'))
    pdf.ln(3)

    # Exp 2 - Clínica Animal Feliz
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 6, 'Clínica Animal Feliz', ln=True)
    pdf.set_font('Arial', 'I', 10)
    pdf.cell(0, 6, 'Veterinária Clínica | Janeiro 2021 - Fevereiro 2022', ln=True)
    pdf.set_font('Arial', '', 10)
    desc_clinica = (
        "- Atendimento clínico geral e emergencial\n"
        "- Realização de cirurgias de rotina (castrações, etc.)\n"
        "- Orientação nutricional e programas de prevenção\n"
        "- Acompanhamento de animais crônicos e geriátricos\n"
        "- Elaboração de protocolos de biossegurança"
    )
    pdf.multi_cell(0, 6, desc_clinica.encode('latin-1', 'replace').decode('latin-1'))
    pdf.ln(3)

    # Exp 3 - PetShop Cão e Gato
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 6, 'PetShop Cão e Gato', ln=True)
    pdf.set_font('Arial', 'I', 10)
    pdf.cell(0, 6, 'Assistente Veterinária | Agosto 2019 - Dezembro 2020', ln=True)
    pdf.set_font('Arial', '', 10)
    desc_assistente = (
        "- Auxílio em consultas e procedimentos clínicos\n"
        "- Responsável pelo setor de banho e tosa\n"
        "- Controle de vacinação e vermifugação\n"
        "- Atendimento ao cliente e vendas de produtos\n"
        "- Organização do estoque de medicamentos"
    )
    pdf.multi_cell(0, 6, desc_assistente.encode('latin-1', 'replace').decode('latin-1'))
    pdf.ln(5)

    # --- ESPECIALIZAÇÕES ---
    section_title('Especializações e Competências')
    pdf.set_font('Arial', '', 10)
    
    especializacoes = [
        "- Clínica de animais exóticos (aves, roedores, répteis)",
        "- Nutrição animal e dietas especiais",
        "- Comportamento animal e treinamento básico",
        "- Primeiros socorros veterinários",
        "- Gestão financeira de estabelecimentos pet",
        "- Marketing digital para petshops",
        "- Biossegurança em ambientes veterinários"
    ]

    for esp in especializacoes:
        pdf.multi_cell(0, 6, esp.encode('latin-1', 'replace').decode('latin-1'))
    pdf.ln(5)

    # --- HABILIDADES TÉCNICAS ---
    section_title('Habilidades Técnicas')
    pdf.set_font('Arial', '', 10)
    skills = [
        "Atendimento clínico a pequenos animais",
        "Realização de exames laboratoriais básicos",
        "Administração de medicamentos e fluidoterapia",
        "Técnicas de contenção e manejo animal",
        "Gestão de estoque e controle de produtos",
        "Sistemas de agendamento digital (PetSharp, ClinicPet)",
        "Elaboração de planos de saúde animal",
        "Microsoft Office (Excel para controle de estoque)",
        "Inglês técnico para leitura de artigos"
    ]
    for skill in skills:
        pdf.cell(0, 6, f"- {skill}".encode('latin-1', 'replace').decode('latin-1'), ln=True)
    pdf.ln(5)

    # --- CURSOS E CERTIFICAÇÕES ---
    section_title('Cursos e Certificações')
    cursos = [
        "Curso Avançado em Animais Exóticos - CRMV-PR (2023)",
        "Gestão Financeira para Petshops - Sebrae (2022)",
        "Primeiros Socorros Veterinários - Instituto Pet Care (2021)",
        "Nutrição Clínica de Cães e Gatos - Universidade Pet (2020)",
        "Comportamento Animal - ABRAVET (2019)",
        "Marketing Digital para Clínicas Veterinárias - Digital Vet (2022)",
        "Biossegurança em Ambientes Veterinários - ANCLIVEPA (2021)"
    ]
    
    for curso in cursos:
        pdf.cell(0, 6, f"- {curso}".encode('latin-1', 'replace').decode('latin-1'), ln=True)
    
    pdf.ln(10)
    
    # --- INFORMAÇÕES ADICIONAIS ---
    section_title('Informações Adicionais')
    pdf.set_font('Arial', '', 10)
    adicional = (
        "Disponibilidade para trabalho em finais de semana e feriados (escalas)\n"
        "Habilitação categoria B\n"
        "Participação em eventos beneficentes de adoção animal\n"
        "Membro ativo da Associação Brasileira de Veterinários (ABV)"
    )
    pdf.multi_cell(0, 6, adicional.encode('latin-1', 'replace').decode('latin-1'))

    # Salvar arquivo
    pdf.output("curriculo_petshop_exemplo.pdf")
    print("PDF gerado com sucesso: curriculo_petshop_exemplo.pdf")


if __name__ == '__main__':
    """
    Ponto de entrada principal do script.
    
    Quando executado diretamente, chama a função create_resume()
    para gerar o currículo em formato PDF.
    """
    create_resume()
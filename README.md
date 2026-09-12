# Scholarship Eligibility Evaluator - Testes e Mutação

Este projeto contém a suíte de testes automatizados e as configurações de injeção de falhas para o sistema de avaliação de bolsas de estudo, desenvolvido em Python[cite: 1].

## 1. Instalação das Ferramentas

Para rodar a suíte de testes e a análise de mutação, é necessário instalar o framework de testes e a ferramenta de injeção de falhas compatível[cite: 1]. Execute o comando no seu terminal:

`python -m pip install pytest cosmic-ray`

## 2. Como Executar os Testes Funcionais

A validação do código é feita pelo framework `pytest`[cite: 1]. Para rodar todos os cenários projetados e garantir a reprodutibilidade, utilize o seguinte comando principal no terminal[cite: 1]:

`python -m pytest test_ScholarshipEligibilityEvaluator.py`

## 3. Como Executar a Análise de Mutação

A análise de mutação sobre o sistema-base utiliza o `Cosmic Ray`[cite: 1]. Execute os comandos abaixo na ordem para inicializar a sessão, rodar as mutações e extrair os relatórios finais[cite: 1]:

1. **Inicializar a sessão e o banco de dados local:**
   `cosmic-ray init cosmic-ray.toml session.sqlite`

2. **Executar a injeção de mutantes contra a suíte de testes:**
   `cosmic-ray exec cosmic-ray.toml session.sqlite`

3. **Visualizar o score de mutação no terminal:**
   `cr-report session.sqlite`

4. **Gerar o relatório visual (HTML) para análise dos sobreviventes:**
   `cr-html session.sqlite relatorio_mutacao`

## 4. Configuração Necessária (cosmic-ray.toml)

Para a correta execução da ferramenta de mutação, é obrigatória a presença do arquivo de configuração `cosmic-ray.toml` na raiz do projeto[cite: 1]. O arquivo deve conter a seguinte estrutura:

```toml
[cosmic-ray]
module-path = "ScholarshipEligibilityEvaluator.py"
test-command = "python -m pytest test_ScholarshipEligibilityEvaluator.py"
timeout = 10.0

[cosmic-ray.distributor]
name = "local"
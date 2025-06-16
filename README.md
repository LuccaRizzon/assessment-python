# 🐍 Desafio de Python

Este repositório contém a solução do desafio de Python proposto, com foco em lógica de programação, estruturação em Flask e boas práticas de desenvolvimento.

## 🧱 Estrutura do Projeto
app/
├── controllers/
├── forms/
├── scripts/
├── templates/
└── init.py

## ✅ Funcionalidades Extras Implementadas

1. **Cabeçalhos CSP (Content Security Policy)**  
   Adicionados via `after_request` para prevenir a execução de scripts maliciosos.

2. **Sanitização com Regex**  
   Campos como `name`, `category` e `search` aceitam apenas letras (A-Z, a-z) e espaços, prevenindo entradas indevidas.

3. **Validação de Campos no Frontend**  
   Limites de tamanho e valores foram definidos para evitar estouros de inteiros e submissão de dados inválidos (ex: `max=2147483647` para inteiros).

4. **Código em Inglês**  
   Toda a base de código segue nomenclaturas, comentários e estrutura em inglês, alinhando-se com padrões globais da indústria de software.

5. **Segurança Adicional com Headers HTTP**  
   Os seguintes headers foram implementados para reforçar a segurança da aplicação:

   - **X-Content-Type-Options: nosniff**  
     Impede que o navegador tente adivinhar o tipo de conteúdo, evitando ataques de tipo MIME.

   - **X-Frame-Options: DENY**  
     Bloqueia o carregamento da aplicação dentro de `<iframe>`, prevenindo ataques de clickjacking.

   - **Referrer-Policy: no-referrer**  
     Garante que o navegador não envie o referer (URL de origem) nas requisições, evitando vazamento de informações sensíveis.

---

## 🛠️ Como Rodar o Projeto

### 📦 Requisitos
- git clone https://github.com/LuccaRizzon/assessment-python.git
- Docker

---

### 🔄 Rodando com Docker

```bash
docker compose up --build
```

Acesse via: [http://localhost:5000/](http://localhost:5000/)

---

Esse foi meu primeiro contato com Flask e com o uso de Python voltado ao desenvolvimento de APIs.  
Até então, eu havia utilizado Python principalmente com Scrapy e scripts puros para decodificação de rastreadores, mas nunca havia trabalhado com frameworks web. Apesar disso, achei a curva de aprendizado agradável e gostei bastante da simplicidade e clareza que o Flask oferece para estruturar aplicações.

💡 Sugestões de Perguntas Técnicas para Entrevistas
1. Abordagem para Resolução de Problemas Reais
"Conte sobre um desafio técnico relevante enfrentado na empresa. Como você o abordaria em termos de análise, arquitetura, tecnologias envolvidas e processo de tomada de decisão?"

2. Exploração de Arquitetura e Estratégia Técnica
"Dada uma stack definida pelo time (ex: Flask + PostgreSQL + Redis), como você projetaria uma solução para um sistema de complexidade moderada? Quais etapas arquiteturais e lógicas seguiria? Onde aplicaria boas práticas e otimizações? Quais trade-offs consideraria ao longo do processo?"

Embora os desafios de código sejam uma boa etapa inicial — como neste caso —, eles não conseguem avaliar por completo as habilidades de um candidato nem suas vivências técnicas. O código é apenas a ponta do iceberg; o que define um desenvolvedor maduro é sua capacidade de tomada de decisão, visão arquitetural e experiência prática.

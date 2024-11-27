# UDP Time Sync Client
Este repositório contém uma implementação simples de um cliente SNTP (Simple Network Time Protocol) usando Python. O projeto foi desenvolvido como parte de um trabalho acadêmico para a disciplina de Redes de Computadores, com o objetivo de explorar a comunicação por meio do protocolo UDP e a sincronização de horários com servidores NTP.

O cliente SNTP desenvolvido realiza as seguintes ações:

- Envia uma mensagem SNTP para um servidor NTP especificado pelo usuário.
- Recebe e interpreta a resposta do servidor, exibindo a data e a hora sincronizadas no console.
- Gerencia o tempo limite (timeout) e retentativas, avisando caso não seja possível contatar o servidor.

A implementação utiliza a biblioteca nativa de sockets do Python para criar a comunicação com o servidor por meio do protocolo UDP, na porta 123.

## Funcionalidades

- Enviar requisições SNTP a servidores NTP via UDP.
- Interpretar mensagens SNTP de 48 bytes para exibir a data e hora atuais.
- Gerenciar falhas de comunicação com timeout e tentativas automáticas.
- Saída formatada no console com a data e hora no padrão:
- Data/hora: Qui Mar 28 23:11:16 2019

## Detalhes Técnicos

A mensagem SNTP consiste em uma estrutura de 48 bytes, conforme a RFC 1769. Apenas o campo txTm_s (timestamp de transmissão) é essencial para determinar a hora atual.

Estrutura da mensagem SNTP:
Implementada com um struct no formato especificado:

```bash
typedef struct {
    uint8_t li_vn_mode;
    uint8_t stratum;
    uint8_t poll;
    uint8_t precision;
    uint32_t rootDelay;
    uint32_t rootDispersion;
    uint32_t refId;
    uint32_t refTm_s;
    uint32_t refTm_f;
    uint32_t origTm_s;
    uint32_t origTm_f;
    uint32_t rxTm_s;
    uint32_t rxTm_f;
    uint32_t txTm_s;
    uint32_t txTm_f;
} ntp_packet;
```

# Linux Mint Customizer 🎨

Um conjunto de scripts bash para personalizar e otimizar seu sistema Linux Mint com facilidade.

## 📋 Tabela de Conteúdos

- [Visão Geral](#visão-geral)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Scripts Disponíveis](#scripts-disponíveis)
- [Configuração](#configuração)
- [Troubleshooting](#troubleshooting)
- [Contribuindo](#contribuindo)
- [Licença](#licença)

## 🎯 Visão Geral

O **Linux Mint Customizer** oferece uma solução automatizada para personalizar seu ambiente Linux Mint, incluindo:

- Instalação e configuração de temas
- Personalização de ícones e fontes
- Otimização de performance
- Configuração de áreas de trabalho virtuais
- Instalação de aplicativos essenciais
- Customização do shell e ambiente

Este projeto foi desenvolvido para economizar tempo e facilitar a criação de um ambiente de trabalho personalizado.

## 📦 Requisitos

- **Sistema Operacional**: Linux Mint 20+ (Cinnamon, MATE ou Xfce)
- **Bash**: versão 4.0 ou superior
- **Conexão com a internet**: para download de pacotes
- **Privilégios sudo**: necessário para instalações de sistema
- **Git** (opcional): para clonar o repositório

## 🚀 Instalação

### Via Git

```bash
git clone https://github.com/matheusbecaridias/linux-mint-customizer.git
cd linux-mint-customizer
chmod +x *.sh
```

### Via Download Direto

```bash
wget https://github.com/matheusbecaridias/linux-mint-customizer/archive/main.zip
unzip main.zip
cd linux-mint-customizer-main
chmod +x *.sh
```

## 💻 Uso

### Menu Interativo (Recomendado)

```bash
./customize.sh
```

Este comando abre um menu interativo onde você pode selecionar quais personalizações deseja aplicar.

### Executar Scripts Individuais

```bash
./install-essentials.sh      # Instala aplicativos essenciais
./setup-theme.sh             # Configura temas
./optimize-system.sh         # Otimiza performance
./configure-shell.sh         # Configura shell e terminal
```

## 📚 Scripts Disponíveis

### 1. `customize.sh` 🎮
**Menu principal interativo**

Oferece uma interface amigável para selecionar múltiplas personalizações.

```bash
./customize.sh
```

### 2. `install-essentials.sh` 📥
**Instala aplicativos essenciais**

Instala uma seleção curada de ferramentas úteis:
- Editor de texto: VS Code, Sublime Text
- Ferramentas de desenvolvimento: Git, Docker, Node.js
- Utilidades: VLC, GIMP, Blender
- Ferramentas de sistema: htop, curl, wget

```bash
./install-essentials.sh
```

### 3. `setup-theme.sh` 🎨
**Personaliza temas e aparência**

Permite escolher entre diversos temas:
- Temas Cinnamon pré-configurados
- Pacotes de ícones
- Fontes personalizadas
- Wallpapers

```bash
./setup-theme.sh
```

### 4. `optimize-system.sh` ⚡
**Otimiza performance do sistema**

- Desativa efeitos visuais desnecessários
- Limpa cache desnecessário
- Otimiza swap
- Desativa bloatware
- Configura power management

```bash
./optimize-system.sh
```

### 5. `configure-shell.sh` 🐚
**Configura shell e terminal**

- Instala Zsh com Oh My Zsh
- Configura aliases úteis
- Instala plugins (syntax highlighting, auto-completion)
- Personaliza prompt
- Configura .bashrc/.zshrc

```bash
./configure-shell.sh
```

### 6. `backup-config.sh` 💾
**Faz backup de configurações**

Cria backup de suas configurações personalizadas.

```bash
./backup-config.sh
```

### 7. `restore-config.sh` 🔄
**Restaura configurações anteriores**

Restaura suas configurações de um backup anterior.

```bash
./restore-config.sh
```

## ⚙️ Configuração

### Arquivo de Configuração

Edite `config.conf` para personalizar o comportamento dos scripts:

```bash
# config.conf
THEME_NAME="Mint-Y-Dark"
ICON_THEME="Mint-X"
FONT_NAME="Ubuntu"
FONT_SIZE=10
ENABLE_EFFECTS=false
AUTO_UPDATE=true
```

### Variáveis de Ambiente

```bash
# Adicione ao seu ~/.bashrc ou ~/.zshrc
export CUSTOMIZER_HOME="$HOME/.local/share/customizer"
export CUSTOMIZER_BACKUP_DIR="$HOME/.customizer-backups"
```

## 🔧 Exemplos de Uso

### Personalização Completa

```bash
# Executar personalização interativa
./customize.sh

# Ou executar tudo automaticamente
./install-essentials.sh && ./setup-theme.sh && ./configure-shell.sh
```

### Instalar Apenas Aplicativos

```bash
./install-essentials.sh --only-apps
```

### Testar Sem Aplicar Mudanças

```bash
./customize.sh --dry-run
```

### Ver Ajuda

```bash
./customize.sh --help
```

## 🐛 Troubleshooting

### Erro: "Permission denied"

```bash
chmod +x *.sh
```

### Scripts não encontram diretórios

```bash
# Execute a partir do diretório correto
cd linux-mint-customizer
./customize.sh
```

### Problemas de Conexão

Verifique sua conexão com a internet:

```bash
ping google.com
```

### Reversão de Mudanças

Use o backup para restaurar:

```bash
./restore-config.sh
```

### Logs de Erro

Verifique os logs detalhados:

```bash
cat ~/.customizer/logs/latest.log
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Siga os passos abaixo:

1. **Fork** o repositório
2. **Crie** uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. **Push** para a branch (`git push origin feature/AmazingFeature`)
5. **Abra** um Pull Request

### Diretrizes

- Sempre teste seus scripts antes de submeter
- Adicione comentários explicativos
- Atualize a documentação
- Siga o estilo de código existente

## 📝 Licença

Este projeto está licenciado sob a [GPL v3.0](LICENSE) - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👨‍💻 Autor

**Matheus Becaridias**
- GitHub: [@matheusbecaridias](https://github.com/matheusbecaridias)

## 🙏 Agradecimentos

- Comunidade Linux Mint
- Inspiração em projetos similares
- Todos os contribuidores

## 📞 Suporte

Encontrou um problema? Abra uma [issue](https://github.com/matheusbecaridias/linux-mint-customizer/issues) no GitHub.

## 📖 Recursos Adicionais

- [Documentação Linux Mint](https://linuxmint.com/documentation.php)
- [Bash Scripting Guide](https://www.gnu.org/software/bash/manual/)
- [Temas Cinnamon](https://cinnamon-spices.linuxmint.com/themes/)

---

⭐ Se este projeto foi útil para você, considere dar uma estrela!

**Última atualização**: 2026-06-11

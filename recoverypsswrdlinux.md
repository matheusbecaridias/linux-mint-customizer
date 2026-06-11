## Usando `init=/bin/bash` (Método Clássico)
Este método é universal e funciona em praticamente todas as distribuições .

1.  Na tela do **GRUB**, pressione **`e`** para editar.
2.  Encontre a linha que começa com `linux`.
3.  **Substitua** o parâmetro `ro` (read-only) por **`rw`** (read-write). No final da linha, pressione **Espaço** e adicione:
    ```text
    init=/bin/bash
    ```
    *Exemplo: ... ro quiet splash -> rw init=/bin/bash*
4.  Pressione **`Ctrl + X`**.
5.  Você entrará diretamente em um shell **root** sem pedir login. Digite o comando para trocar a senha:
    ```bash
    passwd seu_usuario
    ```
6.  Após confirmar a nova senha, reinicie o sistema:
    ```bash
    reboot -f
    ```

## Usando "Recovery Mode" (Mais Simples para Ubuntu/Debian)
Se você usa Ubuntu, essa é a opção mais amigável .

1.  Reinicie o PC e mantenha pressionado **`Shift`** (ou tecle **`Esc`** repetidamente) para forçar a abertura do menu GRUB.
2.  Escolha **"Advanced options for Ubuntu"**.
3.  Selecione a opção que termina com **"(recovery mode)"**.
4.  No menu azul que aparece, escolha **"root - Drop to root shell prompt"**.
5.  Como o sistema vem em "somente leitura", digite para liberar escrita:
    ```bash
    mount -o remount,rw /
    ```
6.  Altere a senha:
    ```bash
    passwd seu_usuario
    ```
7.  Reinicie:
    ```bash
    reboot
    ```

## ⚠️ Pontos de Atenção
*   **Digitação**: O uso de letras maiúsculas/minúsculas nos comandos faz diferença.
*   **Teclado**: Dentro do shell de recuperação, o teclado pode estar em inglês (padrão US). Preste atenção ao digitar a senha.
*   **Criptografia**: Se o seu disco rígido for **criptografado (LUKS)** , você precisará digitar a senha de descriptografia antes de conseguir acessar essas opções de resgate.
*   **Secure Boot**: Em casos raros, o Secure Boot pode bloquear esses métodos. Você pode precisar desabilitá-lo temporariamente na BIOS/UEFI .

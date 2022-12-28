# Google Drive
  
Módulo de conexão do Google Drive  
  
![banner](imgs/Banner_gdrive.png)
## Como instalar este módulo
  
__Baixe__ e __instale__ o conteúdo na pasta 'modules' no caminho do Rocketbot  



## Como usar este módulo

Antes de usar este módulo, você deve registrar seu aplicativo no Google Cloud Portal.

1. Faça login com uma conta do Google no seguinte link: https://console.cloud.google.com/projectcreate?previousPage=%2Fhome%2Fdashboard
2. Preencha o formulário e pressione Criar
3. No Menu de Navegação (Esquerda), insira API e Serviços
4. Na seção superior, vá para "+ ATIVAR API E SERVIÇOS"
5. Pesquise "Google Drive API", selecione-o e, finalmente, ative-o
6. Novamente, vá para o Menu de Navegação (Esquerda) > API e Serviços > Credenciais
7. Pressione Create Credentials > OAuth Client ID, selecione Application Type: Desktop App, digite um nome e crie.
8. Baixe o arquivo JSON de credenciais.
9. Por fim, vá para o Menu de Navegação (Esquerda) > Tela de Consentimento e adicione um usuário na seção "Testar usuários"

Nota: Quando a primeira conexão for feita, um arquivo .pickle será criado na pasta raiz do Rocketbot, para conectar ao mesmo serviço de outra conta, você precisa deletar
esse arquivo Faça o mesmo procedimento caso as credenciais expirem.


## Descrição do comando

### Configurar credenciais do G-Suite
  
Configurar credenciais do Google Drive
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho do arquivo de credenciais||C:\Usuario\Desktop\credentials.json|

### Listar arquivos no Drive
  
Listar arquivos do Google Drive
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Filtro||mimeType = 'application/vnd.google-apps.folder'|
|Atribuir resultado à variável||var|

### Baixar arquivo
  
Baixar um arquivo do Drive
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID do Arquivo (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Caminho onde salvar o arquivo||C:\users\usuario\Downloads|

### Exportar arquivo
  
Exportar um arquivo do Drive para o tipo de formato solicitado
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID do Arquivo (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Formato de arquivo (Drive)||---- Select format ----|
|Caminho onde salvar o arquivo||C:\users\usuario\Downloads|

### Criar pasta
  
Criar pasta
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID do Arquivo (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|File path||New Folder|
|Atribuir resultado à variável||var|

### Copiar ou mover arquivo
  
Copiar ou mover um arquivo
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID do Arquivo (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Destiny Folder ID||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Mover ou Copiar||var|
|Atribuir resultado à variável||var|

### Subir arquivo
  
Carregar um arquivo para o Google Drive
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho de arquivo||C:\archivo.txt|
|Novo nome (opcional)||new_name.txt|
|Salvar na pasta - ID (opcional)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Atribuir resultado à variável||var|

### Excluir um arquivo ou pasta
  
Excluir um arquivo ou pasta do Google Drive
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID do Arquivo (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Atribuir resultado à variável||var|

### Compartilhar arquivo
  
Compartilhar um arquivo do Drive
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID do Arquivo (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Atribuir resultado à variável||var|

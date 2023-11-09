



# Google Drive
  
Módulo para conectar ao Google Drive e gerenciar seus arquivos. Você pode trabalhar com arquivos e pastas próprios ou compartilhados, mover, excluir, baixar, exportar e carregá-los.  

*Read this in other languages: [English](Manual_gdrive.md), [Português](Manual_gdrive.pr.md), [Español](Manual_gdrive.es.md)*
  
![banner](imgs/Banner_gdrive.png)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  



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

Nota: Quando a primeira conexão for feita, um arquivo .pickle será criado na pasta raiz do Rocketbot, para conectar ao mesmo serviço de outra conta, você precisa
 deletar
esse arquivo Faça o mesmo procedimento caso as credenciais expirem.
## Descrição do comando

### Configurar credenciais do G-Suite
  
Configurar credenciais do Google Drive
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho do arquivo de credenciais||C:\Usuario\Desktop\credentials.json|
|Session||session|

### Listar arquivos no Drive
  
Listar arquivos do Google Drive. Este comando retorna todos os arquivos por padrão, incluindo arquivos descartados. Se você não quiser que os arquivos da lixeira apareçam na lista, use trashed=false como filtro.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Filtro||mimeType = 'application/vnd.google-apps.folder' and trashed = false|
|Somente arquivos próprios||-|
|Somente arquivos compartilhados comigo||-|
|Mais dados||-|
|Atribuir resultado à variável||var|
|Session||session|

### Baixar arquivo
  
Baixar um arquivo do Drive
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID do Arquivo (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Caminho onde salvar o arquivo||C:\users\usuario\Downloads|
|Session||session|

### Exportar arquivo
  
Exportar um arquivo do Drive para o tipo de formato solicitado
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID do Arquivo (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Formato de arquivo (Drive)||---- Select format ----|
|Caminho onde salvar o arquivo||C:\users\usuario\Downloads|
|Session||session|

### Criar pasta
  
Criar pasta
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID do Arquivo (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|File path||New Folder|
|Atribuir resultado à variável||var|
|Session||session|

### Copiar ou mover arquivo
  
Copiar ou mover um arquivo
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID do Arquivo (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Destiny Folder ID||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Mover ou Copiar||var|
|Atribuir resultado à variável||var|
|Session||session|

### Subir arquivo
  
Carregar um arquivo para o Google Drive
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho de arquivo||C:\archivo.txt|
|Novo nome (opcional)||new_name.txt|
|Salvar na pasta - ID (opcional)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Converter para o formato Google|Se marcado, ele tentará fazer o upload do arquivo no formato equivalente do Google (se houver), caso contrário, fará o upload do arquivo original.||
|Atribuir resultado à variável||var|
|Session||session|

### Excluir um arquivo ou pasta
  
Excluir um arquivo ou pasta do Google Drive
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID do Arquivo (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Atribuir resultado à variável||var|
|Session||session|

### Compartilhar arquivo
  
Compartilhar um arquivo do Drive
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID do Arquivo (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Tipo||---- Select ----|
|Papel||---- Select ----|
|E-mail ou Domínio|||
|Enviar e-mail de notificação||-|
|Transferir propriedade||-|
|Mover arquivo para a pasta raiz do novo proprietário||-|
|Atribuir resultado à variável||var|
|Session||session|

### Listar permissões
  
Obtenha uma lista de permissões de um arquivo
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID do Arquivo (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Atribuir resultado à variável||var|
|Session||session|

### Excluir permissão
  
Excluir uma permissão de um arquivo
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID do Arquivo (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|ID do Permissão (Drive)||15224413836718185781|
|Atribuir resultado à variável||var|
|Session||session|

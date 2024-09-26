



# Google Drive
  
Módulo para conectar ao Google Drive e gerenciar seus arquivos. Você pode trabalhar com arquivos e pastas próprios ou compartilhados, mover, excluir, baixar, exportar e carregá-los.  

*Read this in other languages: [English](README.md), [Português](README.pr.md), [Español](README.es.md)*

## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Overview


1. Configurar credenciais do G-Suite  
Configurar credenciais do Google Drive

2. Login sem arquivo json  
Login no Google Drive sem arquivo json

3. Listar arquivos no Drive  
Listar arquivos do Google Drive. Este comando retorna todos os arquivos por padrão, incluindo arquivos descartados. Se você não quiser que os arquivos da lixeira apareçam na lista, use trashed=false como filtro.

4. Baixar arquivo  
Baixar um arquivo do Drive

5. Baixar pasta  
Baixar uma pasta do Drive

6. Exportar arquivo  
Exportar um arquivo do Drive para o tipo de formato solicitado

7. Criar pasta  
Criar pasta

8. Copiar ou mover arquivo  
Copiar ou mover um arquivo

9. Subir arquivo  
Carregar um arquivo para o Google Drive

10. Subir pasta  
Carregar uma pasta para o Google Drive

11. Excluir um arquivo ou pasta  
Excluir um arquivo ou pasta do Google Drive

12. Compartilhar arquivo  
Compartilhar um arquivo do Drive

13. Gerenciar permissoes da pasta  
Cria, atualiza ou exclui uma permissão da pasta. Os tipos de acesso são de usuários: User ou Group, e de acesso geral: Domain ou Anyone.

14. Listar permissões  
Obtenha uma lista de permissões de um arquivo

15. Excluir permissão  
Excluir uma permissão de um arquivo  




----
### OS

- windows
- mac
- linux
- docker

### Dependencies
- [**google-api-python-client**](https://pypi.org/project/google-api-python-client/)- [**google-auth-httplib2**](https://pypi.org/project/google-auth-httplib2/)- [**google-auth-oauthlib**](https://pypi.org/project/google-auth-oauthlib/)
### License
  
![MIT](https://camo.githubusercontent.com/107590fac8cbd65071396bb4d04040f76cde5bde/687474703a2f2f696d672e736869656c64732e696f2f3a6c6963656e73652d6d69742d626c75652e7376673f7374796c653d666c61742d737175617265)  
[MIT](http://opensource.org/licenses/mit-license.ph)
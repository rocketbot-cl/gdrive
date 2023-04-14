



# Google Drive
  
Módulo de conexão do Google Drive  

## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e 
descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos
 e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador 
para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção 
**Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  




## Como usar este módulo

Antes de usar este módulo, você deve registrar seu aplicativo no Google Cloud Portal.

1. 
Faça login com uma conta do Google no seguinte link: 
https://console.cloud.google.com/projectcreate?previousPage=%2Fhome%2Fdashboard
2. Preencha o formulário e pressione 
Criar
3. No Menu de Navegação (Esquerda), insira API e Serviços
4. Na seção superior, vá para "+ ATIVAR API E SERVIÇOS"

5. Pesquise "Google Drive API", selecione-o e, finalmente, ative-o
6. Novamente, vá para o Menu de Navegação (Esquerda) 
> API e Serviços > Credenciais
7. Pressione Create Credentials > OAuth Client ID, selecione Application Type: Desktop 
App, digite um nome e crie.
8. Baixe o arquivo JSON de credenciais.
9. Por fim, vá para o Menu de Navegação (Esquerda) >
 Tela de Consentimento e adicione um usuário na seção "Testar usuários"

Nota: Quando a primeira conexão for feita, um 
arquivo .pickle será criado na pasta raiz do Rocketbot, para conectar ao mesmo serviço de outra conta, você precisa 
deletar
esse arquivo Faça o mesmo procedimento caso as credenciais expirem.
## Overview


1. Configurar credenciais do G-Suite  
Configurar credenciais do Google Drive

2. Listar arquivos no Drive  
Listar arquivos do Google Drive

3. Baixar arquivo  
Baixar um arquivo do Drive

4. Exportar arquivo  
Exportar um arquivo do Drive para o tipo de formato solicitado

5. Criar pasta  
Criar pasta

6. Copiar ou mover arquivo  
Copiar ou mover um arquivo

7. Subir arquivo  
Carregar um arquivo para o Google Drive

8. Excluir um arquivo ou pasta  
Excluir um arquivo ou pasta do Google Drive

9. Compartilhar arquivo  
Compartilhar um arquivo do Drive  




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